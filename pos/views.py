from django.shortcuts import render,redirect
from .models import *
from menu.models import *
from restaurents.forms import *
# Create your views here.
def pos(request):
    data=POS.objects.all().order_by('-id')
    
    return render(request,'pos.html',{'data':data})

def staff_inform(request):
    staff=Staff.objects.all()
    form2=Staff_form(request.GET)
    form1=position_form(request.GET)
    if request.method=='GET':
        name=request.GET.get('name')
        phone=request.GET.get('phone')
        position=request.GET.get('position')
        
        last=Staff.objects.last()
        
        if name:
            p=Staff_types.objects.get(id=position)
            new_staff=Staff.objects.create(name=name,phone=phone,staffid=(last.staffid+1),position=p)
            new_staff.save()
            return redirect('staff')
    
    return render(request,'staff.html',{'data':staff,'form1':form1,'form2':form2})
def staff_det(request,pk):
    staff_in=Staff_info.objects.filter(log_id=pk)
    return render(request,'staff_info.html',{'data':staff_in})
def admin_home(request):
    return render(request,'admin_home.html')
def menu_manage(request):
    data=Menu.objects.all()
    my_menu=MyMenu(request.GET)
    new_cat=category_new(request.GET)
    select_cat=category_select(request.GET)
    if new_cat.is_valid():
        cat=request.GET.get('category_new')
        if cat:
            x=Category.objects.create(category=cat)
            x.save()
            return redirect('menu_manage')
    if my_menu.is_valid():
        name=request.GET.get('item_name')
        price=request.GET.get('item_price')
        category=request.GET.get('category')
        category_obj=Category.objects.get(id=category)
        if name:
            x=Menu.objects.create(item=name,price=price,category=category_obj)
            x.save()
            return redirect('menu_manage')
    return render(request,'menu_manage.html',{'data':data,'form1':select_cat,'form2':my_menu,'form3':new_cat})

def customer_details(request):
    x=Customer.objects.all()
    return render(request,'customer_det.html',{'data':x})

def inventory_manage(request):
    x=Inventory.objects.all()
    print(x)
    my_inv=MyInv(request.GET)
    new_cat=category_new(request.GET)
    select_cat=Invcategory_select(request.GET)
    select_item=Invitem_select(request.GET)
    if new_cat.is_valid():
        cat=request.GET.get('category_new')
        if cat:
            x=Invenory_Cat.objects.create(category=cat)
            x.save()
            return redirect('inventory')
    if my_inv.is_valid():
        name=request.GET.get('item_name')
        category=request.GET.get('category')
        unit=request.GET.get('unit')
        category_obj=Invenory_Cat.objects.get(id=category)
        if name:
            x=Inventory_Item.objects.create(item_name=name,categ=category_obj,unit=unit)
            x.save()
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
                    x.save()
                    return redirect('inventory_manage')
                else:
                    y=Inventory.objects.create(item_inv=item_obj2,quantity=qnty)
                    y.save()
                    return redirect('inventory_manage')
    return render(request,'inventory.html',{'data':x,'form1':new_cat,'form2':my_inv,'form3':select_cat,'form4':select_item})

    