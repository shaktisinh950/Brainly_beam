from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from file_upload import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
