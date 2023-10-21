from django.shortcuts import render,redirect
from .models import *
from restaurents.forms import *
from django.utils import timezone
from datetime import datetime
#This is view for homepage
def home(request):
    return render(request,'home.html')

#This is a view for customer who choose room service
def customer(request,pk):
    
    
    if request.method=='GET':
        form=MyCustomer(request.GET)
        date=datetime.today()
        service=pk
        name=request.GET.get('name')
        phone=request.GET.get('phone')
        serv_id=request.GET.get('service_id')
        if name:
            x=Customer.objects.create(date=date,name=name,phone=phone,service_type=service,service_id=serv_id)
            x.save()
            customer=Customer.objects.get(phone=phone)
            return redirect(f'/menu/?customer_id={customer.pk}')
    return render(request,'customer.html',{'form':form})

#this is for customer who choose Table Service
def customer2(request,tableno):
    
    tableno=tableno
    if request.method=='GET':
        form=MyCustomer(request.GET)
        date=datetime.today()
        name=request.GET.get('name')
        phone=request.GET.get('phone')
        if name:
            x=Customer.objects.create(date=date,name=name,phone=phone,service_type='Table',service_id=tableno)
            x.save()
            customer=Customer.objects.get(phone=phone)
            return redirect(f'/menu/?customer_id={customer.pk}')
    return render(request,'customer.html',{'table':tableno})

#This is a view where user will select his table
def table(request):
    data=Table.objects.all()
    my_object=None
    if request.method=='GET':
        table=request.GET.get('tableno')
        if table:
            my_object=Table.objects.get(table=table)
            return redirect('customer2',tableno=my_object.table)
                
    return render(request,'table.html',{'tables':data})
        
#This is the view for user to see menu and add items 
def menu(request):
    #To create new order with respect to new client
    customer_id = request.GET.get('customer_id', None)
    if customer_id:
        customer = Customer.objects.get(pk=customer_id)
        print(customer)
        exist=Order.objects.filter(service_id=customer)
        if exist:
            pass
        else:
            last_order=Order.objects.last()
            print(last_order)
            if last_order:
                order_crt=Order.objects.create(service_id=customer,order_no=int(last_order.order_no)+1)
                order_crt.save()#new  order number created
            else:
                order_crt=Order.objects.create(service_id=customer,order_no=1)
                order_crt.save()
        order_det=Order.objects.get(service_id=customer)#This will fetch order details for ongoing customer
        pos=POS.objects.create(order_inf=order_det)
        pos.save()#data has been saved to POS model also.
        menu_items=Menu.objects.all() #fetch all data from Menu Models.
        category=Category.objects.all()
        Total=OrderItems.objects.filter(order=order_det)
        prc=0
        for order in Total:
            
            prc+=int(order.item.price*order.quantity)
            #Total price of item with respect to its quantity
        print(prc)
            
        #a form to get the data to add item to order.
    if request.method=='GET':
            item=request.GET.get('item')
            order_id=request.GET.get('order_no')
            cust_id=request.GET.get('cust_id')
            if item:
                item_name=Menu.objects.get(item=item)
                order_no=Order.objects.get(order_no=order_id)
                check=OrderItems.objects.filter(order=order_no,item=item_name)
                order_no=Order.objects.get(order_no=order_id)
                if check:
                    x=OrderItems.objects.get(order=order_no,item=item_name)
                    x.quantity+=1
                    x.save()#This logic will increase the existing item quantity .
                    return redirect(f'/menu/?customer_id={cust_id}')
                else:
                    x=OrderItems.objects.create(order=order_no,item=item_name,quantity=1)
                    x.save()#this will add new item to the order.
                    return redirect(f'/menu/?customer_id={cust_id}')
        
    return render(request,'menu.html',{'data':menu_items,'category':category,'data_pass':customer,'order_id':order_det,'total':Total,'total_prc':prc})

def order(request,custid):
    cust_id=custid#Cust id is the primary key which is passed through url.
    customer = Customer.objects.get(pk=cust_id)
    ord_det=Order.objects.get(service_id=customer)
    bill=OrderItems.objects.filter(order=ord_det)
    x=[no.order.order_no for no in bill]#to get the order no of customer
    y=sum(nos.quantity*nos.item.price for nos in bill)#to get the total bill amount
    return render(request,'order.html',{'bill':bill,'order_no':x[0],'total':y})
def kitchen(request):
    orders=Order.objects.all()# to get the items and its quantity to get it prepared in kitchen.
    return render(request,'kitchen.html',{'orders':orders,})