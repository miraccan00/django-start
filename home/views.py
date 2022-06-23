from django.shortcuts import render,redirect
from .forms import ClientForm
from django.shortcuts import render
from .models import Client, Doctor, Document, ClientAndDocument

def home(request):
    datas = Client.objects.all()
    context = {'datas':datas}
    return render(request,'home/index.html',context)

def hastakayit(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST or None)
        if form.is_valid():
            
            form.save(commit=False)
            form.birthdate = '1'
            form.save()
            form = ClientForm()
            redirect("home:home1")
    return render(request,'home/hastakayit.html',{'form':form})

def hastaonay(request,id):
    hasta = Client.objects.get(id=id)
    documents = Document.objects.all()
    print(documents)
    doctors = Doctor.objects.all()
    context= {
        'documents':documents, 
        'hasta':hasta,
        'doctors':doctors
    }
    return render(request,'home/hastaonay.html',context)

def evrakkayitform(request):
    # doktor = request.get('doctors')
    name = request.POST.get('doctors')
    # evraknames = request.POST.get('documents')
    evraknames = request.POST.getlist('documents')
    myClientandDocObject = ClientAndDocument()
    for evrak in evraknames:
        myevrak = Document.objects.filter(document_name=evrak)
        myevrak[0].id
        
    print(evraknames)
    
    return render(request,'home/hastaform.html')

# def hastaform(request):
#     return render(request,'home/hastaform.html') #