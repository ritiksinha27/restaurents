from django import forms

class MyCustomer(forms.Form):
    name=forms.CharField(max_length=20)
    phone = forms.IntegerField(required=True)
    Service_id=forms.CharField(max_length=10)
    