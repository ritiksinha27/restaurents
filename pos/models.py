from django.db import models
from menu.models import *
from datetime import timedelta,time,datetime
# Create your models here.

class POS(models.Model):
    order_inf=models.OneToOneField(Order,on_delete=models.CASCADE,)
    def order_in(self):
        return self.order_inf.order_no
    def Amount(self):
        L=[]
        for ord in self.order_inf.orderitems_set.all():
            L.append(ord.quantity*ord.item.price)
        return sum(L)
    def Items(self):
        
        d={}
        for i in self.order_inf.orderitems_set.all():
            
            d[i.item.item]=i.quantity
            
        state=' , '.join([f"{key}:-{value}" for key, value in d.items()])
        return(state)
            
class POS_view(models.Model):
    orders=models.ForeignKey(OrderItems,on_delete=models.CASCADE)
    def __str__(self):
        return self.orders.order.order_no
    L=[]
    def ordno(self):
        
        return self.orders.order.service_id
class Invenory_Cat(models.Model):
    category=models.CharField(max_length=25,unique=True)
    def __str__(self):
        return self.category
class Inventory_Item(models.Model):
    categ=models.ForeignKey(Invenory_Cat,on_delete=models.CASCADE)
    item_name=models.CharField(max_length=30,unique=True)
    unit=models.CharField(max_length=12,default='KG')
    def __str__(self):
        return self.item_name
    def catego(self):
        return self.categ.category
class Inventory(models.Model):
    item_inv=models.ForeignKey(Inventory_Item,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    def unit(self):
        return self.item_inv.unit
    def item(self):
        return self.item_inv.item_name
class Staff_types(models.Model):
    staff_type=models.CharField(max_length=25,unique=True)
    def __str__(self):
        return self.staff_type

class Staff(models.Model):
    position=models.ForeignKey(Staff_types,on_delete=models.CASCADE)
    name=models.CharField(max_length=25)
    phone=models.PositiveBigIntegerField(unique=True)
    staffid=models.IntegerField(unique=True)
    def __str__(self):
        return self.name
    def post(self):
        return self.position.staff_type
class Login(models.Model):
    staff_id=models.ForeignKey(Staff,on_delete=models.CASCADE)
    login=models.TimeField()
    logout=models.TimeField()
    date=models.DateField()
    def __str__(self):
        return self.staff_id.name
    def st_id(self):
        return self.staff_id.staffid
    def st_name(self):
        return self.staff_id.name

class Staff_info(models.Model):
    log=models.ForeignKey(Login,on_delete=models.CASCADE)
    work=models.DurationField(default=timedelta(hours=0, minutes=0, seconds=0))
    def staff_no(self):
        return self.log.staff_id
    def wrk(self):
        now = datetime.now()
        datetime1 = datetime.combine(now.date(), self.log.login)
        datetime2 = datetime.combine(now.date(), self.log.logout)
        d= datetime2-datetime1
        self.work=d
        super(Staff_info, self).save()
        # return d
