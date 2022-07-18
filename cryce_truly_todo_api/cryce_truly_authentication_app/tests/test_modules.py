from rest_framework.test import APITestCase
from cryce_truly_authentication_app.models import User

class TestModel(APITestCase):
    
    def test_creates_user(self): 
        user = User.objects.create_user('cryce', 'crycetryly@gmail.com', 'pass123')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'crycetryly@gmail.com')


