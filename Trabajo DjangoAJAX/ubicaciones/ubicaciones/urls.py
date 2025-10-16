from django.urls import path
from . import views

app_name = 'ubicaciones'

urlpatterns = [
    path('', views.form_view, name='form_view'),
    path('get-municipios/', views.get_municipios, name='get_municipios'),
]
