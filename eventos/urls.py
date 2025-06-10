from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacto/', views.contacto, name='contacto'),
    path('detalle/<int:id>', views.detalle, name='detalle'),
    path('buscar', views.buscar,name='buscar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)