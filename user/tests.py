from django.test import TestCase
from .models import Customers
# Create your tests here.


class CustomersTestCase(TestCase):
    def setUp(self):
        Customers.objects.create(f_name='Sunil', l_name="Rawal", email="sunil@gmail.com")
                            
    def test_costumers_gets_adopted(self):
        test1 = Customers.objects.get(f_name="Sunil")
        self.assertEqual(test1.email(), "sunil@gmail.com")
