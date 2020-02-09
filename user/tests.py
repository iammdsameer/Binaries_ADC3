from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.


class CustomersTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="anilpdl", password="anil123")

    def testUser(self):
        testUser = User.objects.get(username="anilpdl")
        self.assertEqual(testUser.username, "anilpdl")
