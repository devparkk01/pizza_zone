from django.shortcuts import render
from .forms import PizzaForm
from .models import Pizza, Size , Topping 


def home ( request) : 
    return render(request , 'pizza/home.html' ) 

def order(request) :
    if request.method == "POST" : 
        filledForm = PizzaForm(request.POST , request.FILES) 
        if( filledForm.is_valid()) :
            filledForm.save() 

            # pizzaObject = Pizza() 
            topping1 = filledForm.cleaned_data.get("topping1")
            topping2 = filledForm.cleaned_data.get("topping2")
            size = filledForm.cleaned_data.get("size")
            # image = filledForm.cleaned_data.get("image")

            # SizeObject = Size.objects.get(title = size)

            # pizzaObject.topping1 = topping1
            # pizzaObject.topping2 = topping2
            # pizzaObject.size = SizeObject
            # pizzaObject.image = image
            # pizzaObject.save() 

            note = f"Your Order placed for {size} {topping1} , {topping2} pizza "
            newForm = PizzaForm() 
            context = { "pizzaform" : newForm , "note" : note} 
            return render (request , 'pizza/order.html' ,context = context)


    else : 
        form = PizzaForm() 
        context = {"pizzaform" : form }
        return render(request , 'pizza/order.html', context = context ) 

    
