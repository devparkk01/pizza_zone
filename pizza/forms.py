from django import forms 
from .models import Pizza 

#  This is a form made from forms.Form

class PizzaForm(forms.Form) :
    topping1= forms.CharField(label = "Topping 1 " , max_length= 100 )
    topping2= forms.CharField(label=  "Topping 2 " , max_length= 100) 
    size = forms.ChoiceField(label = "Size" , choices=[("Small","Small") , ("Medium" ,"Medium"),("Large", "Large")])
    image = forms.ImageField(label = "Upload Image") 


# This is a form made from forms.ModelForm 

# class PizzaForm(forms.ModelForm):
#     class Meta : 
#         model = Pizza
#         fields = ["topping1" , 'topping2' , 'size'] 
#         labels = {"topping1" : "Topping 1 " , "topping2" : "Topping 2 " , "size" : "Size "}