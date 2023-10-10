from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

class POS_Adm(admin.ModelAdmin):
    list_display=['order_in','Amount' ]

admin.site.register(POS,POS_Adm)
class POS_view_Adm(admin.ModelAdmin):
    list_display=[ 'ordno']
      
admin.site.register(POS_view,POS_view_Adm)  
class Invenory_Cat_Adm(admin.ModelAdmin):
    list_display=['category' ]
admin.site.register(Invenory_Cat,Invenory_Cat_Adm)       
class Inventory_Item_Adm(admin.ModelAdmin):
    list_display=['item_name', 'catego' ]
admin.site.register(Inventory_Item,Inventory_Item_Adm)       
class Inventory_Adm(admin.ModelAdmin):
    list_display=[ 'quantity' ,'item']
admin.site.register(Inventory,Inventory_Adm)       
class Staff_types_Adm(admin.ModelAdmin):
    list_display=[ 'staff_type']
admin.site.register(Staff_types,Staff_types_Adm)     
class Staff_Adm(admin.ModelAdmin):
    list_display=[ 'name','phone','staffid' ,'post']
admin.site.register(Staff,Staff_Adm)     
class Login_Adm(admin.ModelAdmin):
    list_display=[ 'st_name' ,'st_id' ,'login', 'logout', 'date']
admin.site.register(Login,Login_Adm)
class Staff_info_Adm(admin.ModelAdmin):
    list_display=['staff_id' ,'Wrkhours' ]
admin.site.register(Staff_info,Staff_info_Adm)     