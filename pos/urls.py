from django.contrib import admin
from .views import *
from django.urls import path 
urlpatterns = [
    path('pos/',pos,name='pos'),
    path('ad',admin_home,name='admin_home'),
    path('staff/',staff_inform,name='staff'),
    path('staff_info/<int:pk>',staff_det,name='staff_det'),
    path('menu_mgmt',menu_manage,name='menu_manage'),
    path('inventory',inventory_manage,name='inventory_manage'),
    path('customer_det',customer_details,name='customer_details'),
]
