from django.db import models

# Create your models here.

class Size(models.Model) :
    title = models.CharField(max_length = 100) 

    def __str__ (self) :
        return self.title 

class Topping (models.Model ) : 
    title = models.CharField(max_length = 100 )
    def __str__ (self) : 
        return self.title 


class Pizza (models.Model) : 
    topping1 = models.ForeignKey(to = Topping , on_delete= models.CASCADE ) 
    topping2 = models.CharField(max_length = 100) 
    size = models.ForeignKey(to = Size , on_delete= models.CASCADE) 
    image = models.ImageField(upload_to = 'images/' ,default= 'images/earth.jpg' )
    
