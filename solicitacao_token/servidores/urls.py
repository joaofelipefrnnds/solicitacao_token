from django.urls import path
from . import views

urlpatterns = [
    path('listagem/',views.listagem, name='listagem'),
    path('cadastro_servidor/',views.cadastro_servidor, name='cadastro_servidor'),
    path('update/<int:pk>/',views.update, name='url_update'),
    path('delete/<int:pk>/',views.delete, name='url_delete')
  
]