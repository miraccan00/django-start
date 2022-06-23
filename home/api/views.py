from rest_framework import routers, serializers, viewsets, status
from home.models import Client, Doctor, Document, ClientAndDocument
from .serializers import ClientSerializer,DoctorSerializer, DocumentSerializer,ClientAndDocumentSerializer

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    def get_queryset(self):
        client = Client.objects.all() 
        return client
    
class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    def get_queryset(self):
        doctor = Doctor.objects.all() 
        return doctor

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class ClientAndDocumentViewSet(viewsets.ModelViewSet):
    serializer_class = ClientAndDocumentSerializer
    def get_queryset(self):
        clientanddocument = ClientAndDocument.objects.all() 
        return clientanddocument