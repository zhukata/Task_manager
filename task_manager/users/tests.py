from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from task_manager.users.forms import UserRegisterForm

class UserTest(TestCase):
    def setUp(self):
        user = get_user_model()
        self.form = UserRegisterForm
        test_user1 = user.objects.create_user(username='testuser1', password='12345')
        test_user1.save()
        test_user2 = user.objects.create_user(username='testuser2', password='12345')
        test_user2.save()

    def test_users(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/users.html')

    def test_register_get(self):
        response = self.client.get(reverse('user_create'))
        self.assertTemplateUsed(response, 'layouts/create.html')
        self.assertContains(response, '<form')
        self.assertTrue(issubclass(self.form, UserRegisterForm))
        self.assertTrue('username', self.form.Meta.fields)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/users/login/?next=/tasks/')
    
    def test_logged(self):
        login = self.client.login(username='testuser1', password='12345')
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 200)


    # def test_register_post(self):

    #     response = self.client.post('/users/create', {
    #         'username': 'user1',
    #         'password1': '123456',
    #         'password2': '123456',
    #     })
        # print(get_user_model())
        # self.assertTrue(get_user_model().objects.first().username, 'user1' )
        # self.assertRedirects(response, expected_url=reverse('user_login')) # why 301
        # self.assertEqual(get_user_model().objects.count(), 0)

        # form = self.form({
        #     'username': 'login',
        #     'password' : '123456'
        # })
