from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator

# Create your models here.
class Dane(models.Model):
    teryt=models.CharField(validators=[MaxLengthValidator(11),MinLengthValidator(11)],\
        max_length = 11)
    okres=models.DateField()
    dana1=models.IntegerField(blank=True,null=True)
    dana2=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    dana3=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    dana4=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    dana5=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    dana6=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    dana7=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    dana8=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)
    dana9=models.DecimalField(max_digits=10,decimal_places=2,blank=True,null=True)


