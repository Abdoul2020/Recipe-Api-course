from django.contrib.auth import get_user_model
from django.test import  TestCase


class TestsModel(TestCase):

    def test_create_user_with_email_success(self):
        """Test creating a new user when the amil is successfully"""
        email='abd@gmail.com'
        password="abd123"
        user = get_user_model().objects.create_user(email=email,
        
        password=password)

        self.assertEqual(email,email)
        self.assertTrue(user.check_password(password))

    
    def test_new_user_normalize(self):
        """Test the email for a new user is normalize"""
        email="ABDN@gmail.COM"
        user=get_user_model().objects.create_user(email,'123t')
        self.assertEqual(email,email.lower())

    def test_new_user_invalid(self):
        """test if there is no email and raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,"test123")

    def test_new_superuser(self):
        """test creating a new superuser"""
        user=get_user_model().objects.create_superuser("test@gmail.com","test123")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
    
    

