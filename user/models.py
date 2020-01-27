from django.db import models
from django.contrib.auth.models import User


class Customers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=200, null=True)
    m_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200)
    dob = models.DateField()
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField()
   
    gender = models.CharField(max_length=20)
    
    country = models.CharField(max_length=20, default="Nepal")
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.f_name

    def double_check_values(self):
        return True
