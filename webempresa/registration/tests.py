from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

class ProfileTestCase(TestCase):
    def setUp(self):
        # Corregí la forma de crear un usuario y lo guardé en una variable de instancia
        self.usuario = User.objects.create_user('test', 'test@test.com', 'test1234')

    def test_profile_exists(self):
        # Corregí la forma de verificar si el perfil existe
        existe = Profile.objects.filter(user=self.usuario).exists()
        self.assertEqual(existe, True)

        
        