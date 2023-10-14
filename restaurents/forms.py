from django import forms
from pos.models import *
from menu.models import *
class MyCustomer(forms.Form):
    name=forms.CharField(max_length=20)
    phone = forms.IntegerField(required=True)
    Service_id=forms.CharField(max_length=10)
    
class Staff_form(forms.Form):
    name=forms.CharField(max_length=20,required=True)
    phone = forms.IntegerField(required=True)

class position_form(forms.Form):
    position=forms.ModelChoiceField(
        queryset=Staff_types.objects.all(),
        empty_label="Select Position"
    )
class MyMenu(forms.Form):
    item_name=forms.CharField(max_length=25,required=True)
    item_price=forms.FloatField(required=True)

class category_new(forms.Form):
    category_new=forms.CharField(max_length=25,required=True)
    
class category_select(forms.Form):
    category=forms.ModelChoiceField(queryset=Category.objects.all(),empty_label="select category")
    
class MyInv(forms.Form):
    item_name=forms.CharField(max_length=25,required=True)
    unit=forms.CharField(max_length=10)

class Invcategory_select(forms.Form):
    category=forms.ModelChoiceField(queryset=Invenory_Cat.objects.all(),empty_label="select category")
    
class Invitem_select(forms.Form):
    item=forms.ModelChoiceField(queryset=Inventory_Item.objects.all(),empty_label="select category")
    quantity=forms.IntegerField()
    
