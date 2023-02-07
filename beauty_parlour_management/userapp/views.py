from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import *
from . views import *
from adminapp.models import *
from django.db.models.aggregates import Sum
from django.contrib import messages

# Create your views here.

def index(request):
    obj = Branche.objects.all()
    return render(request,'index.html',{'obj':obj})


def about(request):
    return render(request,'about.html')

def userlogin(request):
    return render(request,'userlogin.html')

def user_login(request):
    username = request.POST.get('name')
    print("username...", username)
    password = request.POST.get('password')
    print("password....", password)
    if Register.objects.filter(name=username,password1=password).exists():
        data = Register.objects.filter(name=username,password1=password).values('email','mobile','password2','id').first()
        request.session['name'] = username
        request.session['email'] = data['email']
        request.session['mobile'] = data['mobile']
        request.session['password1'] = password
        request.session['password2'] = data['password2']
        request.session['id'] = data['id']
        return redirect('index')
    else:
        return redirect('userlogin')


def userlogout(request):
    del request.session['name']
    del request.session['email']
    del request.session['mobile']
    del request.session['password1']
    del request.session['password2']
    del request.session['id']
    return redirect('userlogin')       

def register_user(request):
    return render(request,'user_register.html')

def user_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        data = Register(name=name,email=email,mobile=mobile,password1=password1,password2=password2)
        data.save()
    return redirect('userlogin')

def branches(request):
    obj = Branche.objects.all()
    return render(request,'branches.html',{'obj':obj})


 
def services(request,branchname):
    if (branchname == 'all'):
        data = Service.objects.all()
    else:
        data = Service.objects.filter(branch=branchname)
    return render(request,'services.html',{'data': data})        

 

def cart(request):
    u = request.session.get('id')
    data = Cart.objects.filter(userid=u,status=0)
    s = Cart.objects.filter(userid=u,status=0).aggregate(Sum('total'))
    print(s)
    return render(request,'cart.html',{'data':data,'s':s})

def cart_data(request,sid):
    if 'id' in request.session:
        userid = request.session.get('id')
        price_total = Service.objects.get(id=sid).price
        print(price_total)
        print(userid)
        data = Cart(serviceid=Service.objects.get(id=sid),userid=Register.objects.get(id=userid),status=0,total=price_total)
        data.save() 
        return redirect('cart')
    else:
        messages.error(request,"Please Login")
    return redirect('userlogin')



def cart_delete(request,cartid):
    Cart.objects.filter(id=cartid).delete()
    return redirect('cart')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        conatct = request.POST.get('conatct')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = Contact(name=name,email=email,conatct=conatct,subject=subject,message=message)
        data.save()
        messages.success(request, 'Successfully Sent The Message!')

    return render(request,'contact.html')


def checkout(request):
    u = request.session.get('id') 
    data = Cart.objects.filter(userid=u,status=0)
    s = Cart.objects.filter(userid=u,status=0).aggregate(Sum('total'))
    print(s)
    return render(request,'checkout.html',{'data':data,'s':s})


def checkout_data(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        date = request.POST.get('date')
        time = request.POST.get('time')
        u = request.session.get('id')
        order = Cart.objects.filter(userid=u,status=0)
        for i in order:
            data = Checkout(cartid=Cart.objects.get(id=i.id),fname=fname,lname=lname,email=email,mobile=mobile,date=date,time=time)
            data.save()
            Cart.objects.filter(id=i.id).update(status=1)
    return redirect('index')     
  
