from django.urls import path, include
from .views import home,hastakayit,hastaonay,evrakkayitform
# hastaform
from rest_framework import routers

app_name = 'home'

urlpatterns = [
    path('',home,name='home1'),
    path('home/',home,name='home2'),
    path('hastakayit/',hastakayit,name='hastakayit'),
    path('<int:id>',hastaonay ,name='hastaonay'),
    path('hastaform/',evrakkayitform,name="evrakkayitform"),
]
