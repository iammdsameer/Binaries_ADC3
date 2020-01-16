from django.db import models


class Customers(models.Model):
    f_name = models.CharField(max_length=200)
    m_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200)
    dob = models.DateField()
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    gender = models.CharField(max_length=20)



