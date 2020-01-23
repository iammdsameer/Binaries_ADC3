from django.db import models


class Customers(models.Model):
    f_name = models.CharField(max_length=200,null=True)
    m_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200)
    dob = models.DateField()
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    gender = models.CharField(max_length=20)
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.f_name  

    def double_check_values(self):
        return True
