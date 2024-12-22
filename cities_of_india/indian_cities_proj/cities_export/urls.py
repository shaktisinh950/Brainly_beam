from django.urls import path
from .views import export_indian_cities_to_csv, download_page

urlpatterns = [
    path('', download_page, name='download_page'),
    path('export-indian-cities/', export_indian_cities_to_csv, name='export_indian_cities'),
]