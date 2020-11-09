from django.shortcuts import render
from .forms import  ImageUploadForm
from django.contrib import messages
from PIL import Image
import copy
def home(request):
    if request.method=='POST':
        image=request.FILES['imageUpload']
        desired_size=int(request.POST.get("requiredSize",100000))
        size=image.size
        print(type(image))
        ori_size=copy.deepcopy(size)
        if size<= desired_size:
            messages.error(request,"image size is already less than required")
            imageuploadform = ImageUploadForm()
            context = {'imageuploadform': imageuploadform}
        else:
            import os
            fname, fext = os.path.splitext(image.name)
            if fext == ".jpeg" or fext == ".png" or fext == ".jpg":
                try:
                    i = Image.open(image)
                except Exception as e:
                    messages.error(request,e)
                else:
                    delta = 0
                    xpx, ypx = i.size
                    ori_pix= i.size
                    delta = 50
                    while size > desired_size:
                        i.thumbnail((xpx - delta, ypx - delta))
                        xpx, ypx = i.size
                        size = xpx* ypx
                        print(xpx,ypx,xpx*ypx,desired_size)
                        if xpx-delta<=0 or ypx-delta<=0:
                            messages.info(request, "reduced to least possible size")
                            break

                    messages.info(request,f"Image Size Reduced to {(xpx,ypx)}{size}  Bytes from {ori_pix} {ori_size}")
                    context={image:i}
            else:
                messages.info(request,"invlaid file type")
                imageuploadform = ImageUploadForm()
                context = {'imageuploadform': imageuploadform}

    else:
        imageuploadform = ImageUploadForm()
        context = {'imageuploadform': imageuploadform}
    return  render(request,"pixelhome.html",context=context)