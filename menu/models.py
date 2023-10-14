

# Create your models here.
from django.db import models
from django.utils import timezone
# Create your models here.

#This model will store the data regading the type of service customer can opt for.
class Service(models.Model):
    service=models.CharField(max_length=20,primary_key=True)
    def __str__(self):
        return self.service
#This model will store the data of customer including the service type.
class Customer(models.Model):
    date=models.DateTimeField()
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    service_type=models.CharField(max_length=20)
    service_id=models.CharField(max_length=10)
    def __str__(self):
        return f" {self.name} - {self.phone}"
#This model will store the data of Table
class Table(models.Model):
    table=models.CharField(max_length=10,unique=True)
    def __str__(self):
        return self.table
    
#This model will store the data of Room
class Rooms(models.Model):
    room=models.CharField(max_length=10,unique=True)
    def __str__(self):
        return self.room    

#This model will store the data of Category of menu Items
class Category(models.Model):
    category=models.CharField(max_length=20,unique=True)
    def __str__(self):
        return self.category

#THis will store all the item details 
class Menu(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    item=models.CharField(unique=True,max_length=25)
    item_desc=models.CharField(max_length=120)
    price=models.FloatField()
    def __str__(self):
        return self.item
    def categ(self):
        return self.category.category

#This model will save all the Order details per customer.it will have order no.
class Order(models.Model):
    items=models.ManyToManyField(Menu,through='OrderItems')
    service_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_no=models.CharField(max_length=20,unique=True)
    def __str__(self):
        return f"Order {self.order_no} - Service {self.service_id.service_type} - ID {self.service_id.service_id}"
    def servicetype(self):
        return self.service_id.service_type
    def serviceid(self):
        return self.service_id.service_id
class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.order.order_no


    

    