from django.shortcuts import render,redirect
from .forms import ImageUploadForm
from django.contrib import messages
from PIL import Image
import copy
from .models import Task
from accounts.forms import Loginform
import os
import imghdr
from django.core.mail import EmailMessage
from commonauth.settings import EMAIL_FROM_ADDRESS, BASE_DIR
from django.contrib import sessions

def home(request):

    if request.method == 'POST':
        image = request.FILES['imageUpload']
        desired_size = int(request.POST.get("requiredSize", 100_000))
        size = image.size
        if request.user.is_authenticated:
            print(request.user,"is authneticted")
            task = Task(image=image, requiredSize=desired_size, user=request.user)
            task.save()
            ori_size = copy.deepcopy(size)
        else:

            print(request.user,"is not authneticted")
            messages.error(request,"redirect to login ")
            return  redirect("/")

        if size <= desired_size:
            messages.error(request, "image size is already less than required")
            imageuploadform = ImageUploadForm()
            context = {'imageuploadform': imageuploadform}
        else:
            i = Image.open(image)
            ori_pix = i.size
            newpath = os.path.join(BASE_DIR, f'media/tasks/reducedSize_{image.name}')
            quality = int(desired_size / size * 100)
            i.save(newpath, quality=quality)
            if not imghdr.what(newpath) == "jpeg" or imghdr.what(newpath) == "png" or imghdr.what(newpath) == "jpg" :
                messages.error(request, imghdr.what(newpath))
            while size > desired_size:
                i.save(newpath, quality=quality)
                print(desired_size, size, quality)
                size = os.path.getsize(newpath)
                quality -= 1
                if quality <= 0:
                    messages.info(request, "reduced to least possible size")
                    break
            messages.info(request, f"Image Size Reduced to {size}  Bytes from {ori_size}  {ori_pix} ")
        
            try:
                
                task = Task.objects.filter(user=request.user).filter(image__icontains=image.name)[0]
            except Exception as e:
                
                messages.error(request,f"error : {e} user :{request.user} ")



            context = {'task': task}
            context['user'] = request.user
            mail = EmailMessage(
                'Subject here',
                f'Hi {request.user.username} \n,PFA the File with Reduced size ',
                EMAIL_FROM_ADDRESS,
                [request.user.email]
            )
            mail.attach_file(newpath)
            try:
                mail.send()
            except Exception as error:
                messages.error(request,
                               f"Mail could not sent due to Error {error}some issue at server end Please try later")
            else:
                messages.info(request, "new file has been sent to your registered mail id")
    else:
        imageuploadform = ImageUploadForm()
        loginform = Loginform()
        request.session['user'] = request.user.username
        context = {'imageuploadform': imageuploadform}
        if request.user == "AnonymousUser":
            dir(request.session)
        context['user'] = request.user
        context['loginform'] = loginform
    print("before render")
    return render(request, "pixelhome.html", context=context)
