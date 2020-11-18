from django.shortcuts import render
from .forms import ContactusForm
from .models import Contactusmodel
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings

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
            try:
                send_mail(
                    'Auto Reply: Feedback ',
                    "thanks for your Messsage",
                    settings.EMAIL_HOST_USER,
                    [email,]
                )
            except Exception as err:
                messages.error(request,f"Error : {err}")
            else:
                messages.info(request,f"Thanks Mr. {name} for your Message")    

        else:
            context['form']=contactusformdata 
            print(contactusformdata)
    else:
        pass
   
    return render(request,'index.html',context=context)


