import logging
import datetime
import os
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from django.conf import settings
from django.utils import timezone as dj_timezone

logger = logging.getLogger(__name__)

# Idempotency flag to prevent multiple scheduler starts
_started = False

def start():
    global _started
    if _started:
        logger.info("Scheduler already started; skipping duplicate start")
        return
    # Use Django's configured timezone as a tzinfo object
    scheduler_tz = dj_timezone.get_default_timezone()
    scheduler = BackgroundScheduler(timezone=scheduler_tz)
    scheduler.add_jobstore(DjangoJobStore(), "default")

    # Example: run every 5 minutes (schedule from environment variable or default)
    cron_schedule = os.getenv("CRON_SCHEDULE", "*/5")  # Default to every 5 minutes

    # Remove any stale jobs from previous runs (e.g., jobs pointing to old callables)
    try:
        scheduler.remove_all_jobs(jobstore="default")
    except Exception:
        # If the store is empty or not initialized yet, ignore
        pass

    # Register job using textual reference so it can be serialized
    # Use module:function string path
    scheduler.add_job(
        "scraper.utils:scrape_rates",
        CronTrigger(minute=cron_schedule),
        id="scrape_rates_job",
        name="scrape_rates_job",
        jobstore="default",
        replace_existing=True,
    )
    logger.info("Scheduled job 'scrape_rates_job' to run with cron minute=%s", cron_schedule)

    register_events(scheduler)

    try:
        scheduler.start()
        logger.info("Scheduler started")
        _started = True
    except Exception as e:
        logger.error("Scheduler crashed: %s", e)
        # Optionally, implement a retry mechanism here
