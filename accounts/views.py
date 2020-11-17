from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from .forms import Loginform,Signupform,Updateform
from .models import User
from django.contrib.auth import authenticate,login as login_user,logout as logout_user,get_user_model
from django_email_verification import sendConfirm


def update(request):
    if request.method=="GET":
        try:
            loginform = Loginform(request.GET)
            email = loginform.data['email']
            user=User.objects.get(email=email)
            updateform = Updateform( initial={'username':user.username,'password':user.password,'phoneno':user.phoneno,'email':user.email,'profileimage':user.profileimage})
            context = {'updateform': updateform}
        except:
            messages.error(request,"Login Required to update")
            return HttpResponseRedirect("/accounts/")
    else:
        updateformdata = Updateform(request.POST)
        username = request.user.username
        oldemail=request.user.email
        password = updateformdata.data['password']
        dateofbirth = updateformdata.data['dateofbirth']
        profileimage = request.FILES['profileimage']
        phoneno = updateformdata.data['phoneno']
        email = updateformdata.data['email']
        if not User.objects.filter(email=oldemail,username=username).exists():
            user=User.objects.get(username=username,email=oldemail)
            user.phoneno=phoneno
            user.set_password(password)
            user.dateofbirth=dateofbirth
            user.profileimage=profileimage
            user.save()
            login_user(request,user)
            messages.info(request, "User updated")
            user = User.objects.get(username=username)
            context={'user':user}
        else:
            user = User.objects.get(username=username)
            if email==user.email:
                user.phoneno = phoneno
                user.set_password(password)
                user.dateofbirth = dateofbirth
                user.profileimage = profileimage
                user.save()
                login_user(request,user)
                messages.info(request, "User data updated  successfully")

            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,"Email already registered")
                else:
                    user.email=email
                    user.save()
                    sendConfirm(user)
                    messages.error(request, "Email sent for varification please click on activation link")

            context = {'user': request.user}

    return render(request, 'base.html', context)


def login(request):
    context={}
    if request.method=="POST":

        loginform =Loginform(request.POST)
        username=loginform.data['username']
        password=loginform.data['password']
        if  User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if user.is_active:
                if authenticate(username=username,password=password):
                    login_user(request, user)
                    messages.info(request, "Loged in successfully")
                    context['user'] =user
                else:
                    messages.info(request, "Password not matching")
            else:
                messages.info(request, "Please click on actvation link sent on your corresponding mail id")
        else:
            messages.error(request, "Username does not exits")
        loginform = Loginform()
        context['loginform'] = loginform
        return render(request, 'base.html', context)

    else:
        loginform=Loginform()
        context={'loginform':loginform}
    return render(request,'base.html',context)


def logout(request):
    print("logout")
    logout_user(request)
    loginform = Loginform()
    context = {'loginform': loginform}
    return render(request, 'base.html', context)


def signup(request):
    if request.method=='POST':
        signupformdata=Signupform(request.POST)
        username=signupformdata.data['username']
        password=signupformdata.data['password']
        dateofbirth=signupformdata.data['dateofbirth']
        profileimage=request.FILES['profileimage']
        phoneno=signupformdata.data['phoneno']
        email=signupformdata.data['email']
        user=User.objects.filter(username=username).exists()
        if not user :
            if not User.objects.filter(email=email).exists():
                user = get_user_model().objects.create(username=username,password=password,email=email,phoneno=phoneno,profileimage=profileimage,dateofbirth=dateofbirth,is_active=False)
                user.set_password(password)
                sendConfirm(user)
                logout_user(request)
                messages.info(request,"User created successfully ,please check your mail tp confirm")
            else:
                messages.error(request, "email already exists")
                context = {"user": None}
                return HttpResponseRedirect ('/accounts/views/signup/')
        else:
            messages.error(request,"username already exists")
            context={"user":None}
            return HttpResponseRedirect('/accounts/views/signup')
        loginform = Loginform()
        context={'loginform' :loginform}
    else:
        print("signup")
        logout_user(request)
        signupform=Signupform()
        context={'signupform':signupform}
    return render(request,'base.html',context)