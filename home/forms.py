from django import forms
from .models import Client,ClientAndDocument,Document
   

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name','surname','tcno','birthdate','telephone','address']
    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['surname'].widget.attrs.update({'class' : 'form-control'})
        self.fields['tcno'].widget.attrs.update({'class' : 'form-control'})
        self.fields['birthdate'].widget.attrs.update({'class' : 'form-control'})
        self.fields['telephone'].widget.attrs.update({'class' : 'form-control'})
        self.fields['address'].widget.attrs.update({'class' : 'form-control'})

class ClientAndDocumentForm(forms.ModelForm):
    class Meta:
        model = ClientAndDocument
        fields = ['document_no','clientid','documentid',]

    clientid = forms.ModelMultipleChoiceField(
        queryset=Client.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    documentid = forms.ModelMultipleChoiceField(
        queryset=Document.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    def __init__(self, *args, **kwargs):
        super(ClientAndDocumentForm, self).__init__(*args, **kwargs)
        self.fields['document_no'].widget.attrs.update({'class' : 'form-control'})
        self.fields['clientid'].widget.attrs.update({'class' : 'form-control'})
        self.fields['documentid'].widget.attrs.update({'class' : 'form-control'})
