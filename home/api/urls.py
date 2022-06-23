from django.urls import path, include
from .views import ClientViewSet,DoctorViewSet,DocumentViewSet,ClientAndDocumentViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('client', ClientViewSet,basename='client')
router.register('doctor',DoctorViewSet,basename='doctor')
router.register('document',DocumentViewSet,basename='document')
router.register('clientdocument',ClientAndDocumentViewSet,basename='clientdocument')

urlpatterns = [
    path('', include(router.urls)),
]
