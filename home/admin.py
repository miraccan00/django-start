from django.contrib import admin
from .models import Client, Doctor, Document, ClientAndDocument
# Register your models here.
admin.site.register(Client)
admin.site.register(Doctor)
admin.site.register(Document)
admin.site.register(ClientAndDocument)

