from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.

#creating test cases
class CustomersTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="anilpdl", password="anil123")
        User.objects.create_user(username="sunil", password="123")
        User.objects.create_user(username="Md", password="12md")
        
#Test for user created to not and also test that we can create multiple users at a time 
    def testUser1(self):
        testUser1 = User.objects.get(username="anilpdl")
        self.assertEqual(testUser1.username, "anilpdl")


    def testUser2(self):
        testUser2 = User.objects.get(username="sunil")
        self.assertEqual(testUser2.username, "sunil")

    def testUser3(self):
        testUser3 = User.objects.get(username="Md")
        self.assertEqual(testUser3.username, "Md")
