from django.shortcuts import render
from .forms import PizzaForm


def home ( request) : 
    return render(request , 'pizza/home.html' ) 

def order(request) :
    if request.method == "POST" : 
        filledForm = PizzaForm(request.POST , request.FILES) 
        if( filledForm.is_valid()) :
            topping1 = filledForm.cleaned_data.get("topping1")
            topping2 = filledForm.cleaned_data.get("topping2")
            size = filledForm.cleaned_data.get("size")
            note = f"Your Order placed for {size} {topping1} , {topping2} pizza "
            newForm = PizzaForm() 
            context = { "pizzaform" : newForm , "note" : note} 
            return render (request , 'pizza/order.html' ,context = context)


    else : 
        form = PizzaForm() 
        context = {"pizzaform" : form }
        return render(request , 'pizza/order.html', context = context ) 

    
