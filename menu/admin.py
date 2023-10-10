# Register your models here.
from django.contrib import admin
from .models import *
from menu.models import *
# Register your models here.

class ServiceAdm(admin.ModelAdmin):
    list_display=['service']
    
admin.site.register(Service,ServiceAdm)

class CustomerAdm(admin.ModelAdmin):
    list_display=['date','name','phone','service_type','service_id']
    
admin.site.register(Customer,CustomerAdm)

class TableAdm(admin.ModelAdmin):
    list_display=['table']
    
admin.site.register(Table,TableAdm)

class RoomsAdm(admin.ModelAdmin):
    list_display=['room']
    
admin.site.register(Rooms,RoomsAdm)

class CategoryAdm(admin.ModelAdmin):
    list_display=['category']
    
admin.site.register(Category,CategoryAdm)

class MenuAdm(admin.ModelAdmin):
    list_display=['categ','item','item_desc','price']
    
admin.site.register(Menu,MenuAdm)

class OrderAdm(admin.ModelAdmin):
    list_display=['servicetype','serviceid','order_no']
    
admin.site.register(Order,OrderAdm)

class OrderItemAdm(admin.ModelAdmin):
    list_display=["order",'item','quantity']
    
admin.site.register(OrderItems,OrderItemAdm)
