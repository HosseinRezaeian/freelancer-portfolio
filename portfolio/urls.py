from django.urls import path
from .views import Portfolio
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', Portfolio.as_view(), name='profile')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
