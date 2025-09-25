from django.urls import path
from . import views

app_name = 'scraper'

urlpatterns = [
    path('refresh-rates/', views.scrape_rates, name='scrape_rates'),  # Trigger scraping
    path('khorasan_rates/', views.KhorasanRatesAPIView.as_view(), name='khorasan_rates'),
    path('sarai_rates/', views.SaraiRatesAPIView.as_view(), name='sarai_rates'),
    path('da_afg_rates/', views.DaAfgRatesAPIView.as_view(), name='da_afg_rates'),
]