from django . urls import path
from . import views # es para tener acceso a las vistas
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [    # el usuario va a poder acceder a la vista
    path('', views.index, name='index'),
    path('crear', views.crear, name='crear'),
    path('leer', views.leer, name='leer'),
    path('actualizar/<int:id>', views.actualizar, name='actualizar'),
    path('borrar/<int:id>', views.borrar, name='borrar'),
    path('contacto', views.contacto, name='contacto'),
    path('formulario', views.formulario, name='formulario'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
