from car_app.models import Cars
from django import forms
class UPCars(forms.ModelForm):
    class Meta:
        model=Cars
        fields=['name','price','image','desc','category']