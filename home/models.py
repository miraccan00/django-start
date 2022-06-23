from django.db import models

# Create your models here.
class Client(models.Model):
    #hastanumarası 
    #hastak.adı tc tel tcpass
    #hastasifre  
    name = models.CharField(max_length=40,blank=True, null=True)
    surname = models.CharField(max_length=40,blank=True, null=True)
    tcno = models.CharField(max_length=40,blank=True, null=True)
    birthdate = models.CharField(max_length=40,blank=True, null=True)
    telephone = models.CharField(max_length=40 ,blank=True, null=True)
    address = models.CharField(max_length=40)

    def __str__(self):
        return self.name + ' ' +self.surname
        
class Doctor(models.Model):
    name = models.CharField(max_length=40,)
    surname = models.CharField(max_length=40,blank=True, null=True)
    telephone = models.CharField(max_length=40 ,blank=True, null=True)

    def __str__(self):
        return self.name + ' ' +self.surname

class Document(models.Model):
    document_name = models.CharField(max_length=100)
    documentlink = models.CharField(max_length=250,blank=True, null=True) 
    
    def __str__(self):
        return self.document_name

class ClientAndDocument(models.Model):
    document_no = models.CharField(max_length=250)
    clientid = models.ForeignKey(Client, related_name='clients',on_delete=models.CASCADE, null=True, blank=True)
    documentid = models.ManyToManyField(Document)
    created_date= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.document_no