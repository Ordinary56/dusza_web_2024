from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.
#TODO: add test

'''
Test adding new user 
'''
def testNewUser() -> None:
    new_user = User.objects.create_user()
    pass

'''
    Test user authentication
'''
def testLogin() -> None:
    
    pass