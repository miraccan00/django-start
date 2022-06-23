# This is our serializer page
from rest_framework import serializers
from home.models import Client, Doctor, Document, ClientAndDocument

class ClientSerializer(serializers.ModelSerializer):
    # id = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='author-detail')
    class Meta:
        model = Client
        fields = ('__all__')
        # fields = ('id', 'url', 'name', 'surname','tcno','birthdate','telephone','address')
        

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('__all__')
        # fields = ('id', 'url', 'name', 'surname','tcno','birthdate','telephone')

        # fields = ('id', 'url', 'name', 'slug')

class DocumentSerializer(serializers.ModelSerializer):
    # id = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='author-detail')
    class Meta:
        model = Document
        fields = ('__all__')
        # fields = ('id','document_name','documentlink',)
        

class ClientAndDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientAndDocument
        # fields = ('id','document_no','clientid','documentid','created_date')
        fields = ('__all__')
        depth = 1