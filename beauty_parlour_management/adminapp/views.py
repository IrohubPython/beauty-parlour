from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from . models import *
from adminapp.models import*
from userapp.models import*
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from datetime import datetime, timedelta, time, date

# Create your views here.
def adminindex(request):
    obj1 = Checkout.objects.all().count()
    obj2 = Branche.objects.all().count()
    obj3 = Service.objects.all().count()
    context= {'obj1': obj1, 'obj2':obj2, 'obj3':obj3}
    print(context)
    return render(request, 'adminindex.html',context)

def adminlogin(request):
    return render(request, 'adminlogin.html')

def admin_login(request):
    username_r = request.POST.get('username')
    password_r = request.POST.get('password')
    print(username_r)
    print(password_r)
    if User.objects.filter(username__contains=username_r).exists():
        user = authenticate(username=username_r,password=password_r)
        if user is not None:
            login(request,user)
            request.session['username'] = username_r
            request.session['password'] = password_r
            print(user)
            return redirect('adminindex')
        else:
            return render(request,'adminlogin.html',{'msg':'Sorry....Invalid user credentials'})
    else:
        return render(request,'adminlogin.html',{'msg':'Sorry....Invalid user credentials'})


def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect('adminlogin')

def add_branches(request):
    if request.method == 'POST':
        name_r = request.POST.get('name')
        description_r = request.POST.get('description')
        image_r = request.FILES['image']
        obj = Branche(name=name_r,description=description_r,image=image_r)
        obj.save()
        return redirect('view_branches')
    else:
        return render(request, 'add_branches.html')

def view_branches(request):
     obj = Branche.objects.all()
     return render(request, 'view_branches.html',{'obj':obj})

def b_edit(request,eid):
    obj=Branche.objects.filter(id=eid)
    return render(request,'edit_branches.html',{'obj':obj})

def edit_branches(request,id):
    if request.method == 'POST':
        name_r = request.POST.get('name')
        description_r = request.POST.get('description')
        try:
            image_r = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(image_r.name, image_r)
        except MultiValueDictKeyError:
            file = Branche.objects.get(id=id).image
        
    Branche.objects.filter(id=id).update(name=name_r,description=description_r,image=file)
    return redirect('view_branches')

def delete_branches(request,id):
    Branche.objects.get(id=id).delete()
    return redirect('view_branches')

def add_services(request):
    obj = Branche.objects.all()
    return render(request, 'add_services.html', {'obj':obj})

def service_data(request):
    if request.method == 'POST':
        name_s = request.POST.get('name')
        branch_s = request.POST.get('branch')
        print(".................",branch_s)
        price_s = request.POST.get('price')
        image_s = request.FILES['image']
        obj = Service(branchname=Branche.objects.get(id=branch_s))
        x=obj.branchname.name
        print("x........",x)

        obj = Service(name=name_s,branch=x,price=price_s,image=image_s,
        branchname=Branche.objects.get(name=x))
       
        print("obj............", obj)
        obj.save()
    return HttpResponseRedirect('view_services')

def view_services(request):
    obj = Service.objects.all()
    return render(request, 'view_services.html',{'obj':obj})

def edit_service(request,id):
    if request.method == 'POST':
        name_s = request.POST.get('name')
        branch_s = request.POST.get('branch')
        price_s = request.POST.get('price')
        try:
            image_s = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(image_s.name, image_s)
        except MultiValueDictKeyError:
            file = Service.objects.get(id=id).image

    Service.objects.filter(id=id).update(name=name_s,branch=branch_s,price=price_s,image=file)
    return redirect('view_services')

def edit_s(request,eid):
    obj = Service.objects.filter(id=eid)
    obj1 =Branche.objects.all()
    return render(request,'edit_services.html',{'obj':obj,'obj1':obj1})

def delete_s(request,id):
    Service.objects.get(id=id).delete()
    return redirect('view_services')        

def view_users(request):
    obj = Register.objects.all()
    return render(request, 'view_users.html', {'obj':obj})    

def view_appointments(request):
    obj = Checkout.objects.all()
    today = datetime.today().date()
    print(today)
    obj2 = Checkout.objects.filter(date=today)
    print(obj2)

    return render(request, 'view_appointments.html',{'obj':obj, 'obj2':obj2})  

    

def view_messages(request):
    obj = Contact.objects.all()
    return render(request, 'view_messages.html', {'obj':obj})   
