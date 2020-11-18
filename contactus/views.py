from django.shortcuts import render
from .forms import ContactusForm
from .models import Contactusmodel
def contactus(request):
    context={}
    contactusformdata=ContactusForm(request.POST)
    if request.method=='POST':
        name=contactusformdata.data['name']
        email=contactusformdata.data['email']
        message=contactusformdata.data['message']
        subject=contactusformdata.data['subject']
        
        if contactusformdata.is_valid():
            contactus=Contactusmodel(name=name,message=message,subject=subject,email=email)
            contactus.save()          
        else:
            context['form']=contactusformdata 
    else:
        pass
   
    return render(request,'index.html',context=context)