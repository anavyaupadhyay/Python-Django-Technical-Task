from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

def validating_mobno(num):

    if num.isnumeric:
        if len(num)!=10:
            raise ValidationError("Mobile number should contain exactly 10 digits.")
        else:
            return num
    
    else:
        raise ValidationError("Please enter digits only.") 


class user_model(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    mob_no = models.CharField(
        max_length=10,
        unique=True,
        validators=[validating_mobno],
        null=True, blank=True,
        help_text="Enter 10 digit mobile number"
    )

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

class customer_model(models.Model):
    profile_no = models.OneToOneField(user_model, null=True, on_delete=models.CASCADE)

