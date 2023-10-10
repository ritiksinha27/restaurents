from django.db import models
from menu.models import *
# Create your models here.

class POS(models.Model):
    order_inf=models.ForeignKey(Order,on_delete=models.CASCADE)
    Amount=models.FloatField()
    def order_in(self):
        return self.order_inf.order_no
class POS_view(models.Model):
    orders=models.ForeignKey(OrderItems,on_delete=models.CASCADE)
    def __str__(self):
        return self.orders.order.order_no
    def ordno(self):
        return self.orders.order.order_no
class Invenory_Cat(models.Model):
    category=models.CharField(max_length=25,unique=True)
    def __str__(self):
        return self.category
class Inventory_Item(models.Model):
    categ=models.ForeignKey(Invenory_Cat,on_delete=models.CASCADE)
    item_name=models.CharField(max_length=30,unique=True)
    def __str__(self):
        return self.item_name
    def catego(self):
        return self.categ.category
class Inventory(models.Model):
    item_inv=models.ForeignKey(Inventory_Item,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    def item(self):
        return self.item_inv.item_name
class Staff_types(models.Model):
    staff_type=models.CharField(max_length=25,unique=True)

class Staff(models.Model):
    position=models.ForeignKey(Staff_types,on_delete=models.CASCADE)
    name=models.CharField(max_length=25)
    phone=models.PositiveBigIntegerField(unique=True)
    staffid=models.IntegerField()
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
    staffid=models.ForeignKey(Staff,on_delete=models.CASCADE)
    Wrkhours=models.TimeField
    def __str__(self):
        return f"{self.staffid.name}--{self.staffid.staffid}"
    def staff_id(self):
        return self.staffid.staffid
    
