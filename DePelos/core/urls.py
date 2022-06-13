from django.urls import path 
from .views import index , contacto , somos , galeria , registro , adminez  , form_producto , form_usuario , mostrar_usuario , form_del_usuario , form_mod_usuario , mostrar_producto , form_del_producto , form_mod_producto


urlpatterns = [
    path('', index, name="index"),
    path('contacto/', contacto, name="contacto"),
    path('somos/', somos, name="somos"),
    path('galeria/', galeria, name="galeria"),
    path('registro/', registro, name="registro"),
    path('adminez/', adminez, name="adminez"),
    path('mostrar_usuario/', mostrar_usuario, name="mostrar_usuario"),
    path('mostrar_producto/', mostrar_producto, name="mostrar_producto"),
    path('form_producto/', form_producto, name="form_producto"),
    path('form_usuario/', form_usuario, name="form_usuario"),
    path('form_del_usuario/<id>', form_del_usuario, name="form_del_usuario"),
    path('form_del_producto/<id>', form_del_producto, name="form_del_producto"),
    path('form_mod_usuario/<id>', form_mod_usuario, name="form_mod_usuario"),
    path('form_mod_producto/<id>', form_mod_producto, name="form_mod_producto"),

 ]