from django.urls import path
from consumir_api.views import index, buscar

urlpatterns = [
    path('', index, name='index'),
    path('buscar', buscar, name='buscar')
]