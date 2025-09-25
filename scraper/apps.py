from django.apps import AppConfig


class ScraperConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scraper'

    def ready(self):
        """Start the APScheduler when the app is ready.
        Use Django's autoreloader guard to prevent duplicate starts in development.
        """
        import os
        from django.conf import settings
        from django.db.models.signals import post_migrate
        from django.core.signals import request_started

        # In development, Django's autoreloader imports apps twice.
        # Only connect/start the scheduler in the reloader's main process.
        if settings.DEBUG and os.environ.get("RUN_MAIN") != "true":
            return

        def _start_scheduler_after_migrate(sender, **kwargs):
            # Import here to avoid side effects during module import
            from . import scheduler
            scheduler.start()

        # Defer scheduler start until after all migrations are applied
        post_migrate.connect(_start_scheduler_after_migrate, sender=self)

        # Also add a lazy-start mechanism on the first incoming request
        # to ensure the scheduler starts even if no migrations run on this boot.
        # Use a module-level flag to avoid multiple starts.
        from . import scheduler as _scheduler_module
        if not hasattr(_scheduler_module, "_started"):
            _scheduler_module._started = False

        def _lazy_start_scheduler(**kwargs):
            if not _scheduler_module._started:
                from . import scheduler
                scheduler.start()
                _scheduler_module._started = True

        request_started.connect(_lazy_start_scheduler, dispatch_uid="scraper_lazy_start_scheduler")
