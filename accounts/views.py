from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from travello.models import Destination
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid user') 
            return redirect('login')
    else:
        return render(request,'login.html')

def adminlogin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'adminlogin.html')
        else:
            messages.info(request,"Authentication Failed")
            return render(request,'base_login.html')
    else:
        return render(request,'admin_base_login.html')




def dynamicadd(request):
    if request.method=="POST":
        name=request.POST['city']
        img=request.FILES['picture']
        description=request.POST['description']
        price=request.POST['price']
        offer=request.POST.get('offer')=='on'
        dest=Destination.objects.create(name=name,img=img,description=description,offer=offer,price=price)
        dest.save();
        return redirect('/')
    else:
        pass





def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
        user.save();
        return redirect('login')
    else:
        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def sample(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        collage=request.POST['collage']
        placed=request.POST['placed']
        sample=Sample.objects.create(name=name, age= age,collage=collage,placed=placed)
        sample.save();
        sample3=Sample.objects.all()
        return render(request,'sample2.html',{'sample3':sample3})
    else:
        return render(request,'sample_form.html')