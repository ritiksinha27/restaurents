from django.shortcuts import render,redirect
from restaurents.decorators import unathen_user,allowed_users
from .models import *
from menu.models import *
from restaurents.forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
def pos(request):
    data=POS.objects.all().order_by('-id')
    #To get all the order details from POS model
    return render(request,'pos.html',{'data':data})

def staff_inform(request):
    staff=Staff.objects.all()#To get all the available data in staff model
    form2=Staff_form(request.GET)
    form1=position_form(request.GET)
    if request.method=='GET':
        name=request.GET.get('name')
        phone=request.GET.get('phone')
        position=request.GET.get('position')
        last=Staff.objects.last()#To get last element added in staff model
        if name:
            p=Staff_types.objects.get(id=position)#fetch the position details With Respect tot position provided by user
            new_staff=Staff.objects.create(name=name,phone=phone,staffid=(last.staffid+1),position=p)
            new_staff.save()
            return redirect('staff')#redirect the page to staff
    return render(request,'staff.html',{'data':staff,'form1':form1,'form2':form2})
def staff_det(request,pk):
    staff_in=Staff_info.objects.filter(log_id=pk)
    return render(request,'staff_info.html',{'data':staff_in})
@login_required(login_url='login_a')#using auth we imported login_required function to make login necessary
def admin_home(request):
    #simple admin page for selection the domain to manage
    user=request.user# to show the user details
    name=user.username
    return render(request,'admin_home.html',{'name':name})
def menu_manage(request):
    #View to manage the Menu domain ,to add or modify the menu
    data=Menu.objects.all()
    my_menu=MyMenu(request.GET)
    new_cat=category_new(request.GET)
    select_cat=category_select(request.GET)
    if new_cat.is_valid():
        cat=request.GET.get('category_new')
        if cat:
            x=Category.objects.create(category=cat)
            x.save()#new category is added in menu
            return redirect('menu_manage')
    if my_menu.is_valid():
        name=request.GET.get('item_name')
        price=request.GET.get('item_price')
        category=request.GET.get('category')
        category_obj=Category.objects.get(id=category)
        if name:
            x=Menu.objects.create(item=name,price=price,category=category_obj)
            x.save()#new item is added in menu
            return redirect('menu_manage')
    return render(request,'menu_manage.html',{'data':data,'form1':select_cat,'form2':my_menu,'form3':new_cat})

def customer_details(request):
    #to get the customer details
    x=Customer.objects.all()
    return render(request,'customer_det.html',{'data':x})
@allowed_users(allowed_roles=['admin']) #allowed users is custom decorators we have made to allow selected users
def inventory_manage(request):
    x=Inventory.objects.all()
    my_inv=MyInv(request.GET)
    new_cat=category_new(request.GET)
    select_cat=Invcategory_select(request.GET)
    select_item=Invitem_select(request.GET)
    if new_cat.is_valid():
        cat=request.GET.get('category_new')
        if cat:
            x=Invenory_Cat.objects.create(category=cat)
            x.save()#new category is added in the inventory
            return redirect('inventory')
    if my_inv.is_valid():
        name=request.GET.get('item_name')
        category=request.GET.get('category')
        unit=request.GET.get('unit')
        category_obj=Invenory_Cat.objects.get(id=category)
        if name:
            x=Inventory_Item.objects.create(item_name=name,categ=category_obj,unit=unit)
            x.save()#New item is added in inventory
            return redirect('inventory_manage')
    if select_item.is_valid():
        item=request.GET.get('item')
        qnty=request.GET.get('quantity')
        if item:
            item_obj=Inventory_Item.objects.filter(id=item)
            if item_obj:
                item_obj2=Inventory_Item.objects.get(id=item)
                inv_avl=Inventory.objects.filter(item_inv=item_obj2)
                if inv_avl:
                    x=Inventory.objects.get(item_inv=item_obj2)
                    x.quantity+=int(qnty)
                    x.save()#add quantity to the items present in inventory
                    return redirect('inventory_manage')
                else:
                    y=Inventory.objects.create(item_inv=item_obj2,quantity=qnty)
                    y.save()#add new stock quantity in the inventory 
                    return redirect('inventory_manage')
    return render(request,'inventory.html',{'data':x,'form1':new_cat,'form2':my_inv,'form3':select_cat,'form4':select_item})

@unathen_user #This is custom decorator to check user is logged in or not
def register(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"account is created")
    return render (request,'register_a.html',{'form':form})
@unathen_user
def login_a(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            #this will login to admin control pannel
            return redirect('admin_home')
    return render(request,'login_a.html')
            
def logout_a(request):
    logout(request)
    #This will logout the user
    return redirect('login_a')