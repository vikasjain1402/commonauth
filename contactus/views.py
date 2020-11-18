from django.shortcuts import render

def contactus(request):
    if request.method=='POST':
        pass
    else:
        pass
    context={}
    return render(request,'index.html',context=context)