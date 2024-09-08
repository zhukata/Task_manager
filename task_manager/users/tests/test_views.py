from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class UserTestView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model()
        test_user1 = cls.user.objects.create_user(username='testuser1', password='12345')
        test_user1.save()

    def test_list_users(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/users.html')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/users/login/?next=/tasks/')
    
    def test_logged(self):
        self.client.login(username='testuser1', password='12345')
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 200)

    def test_user_delete(self):
        user = self.user.objects.create_user(username='testuser2', password='12345')
        response = self.client.get(reverse('user_delete', kwargs={'pk': user.pk,}), ) # pk??
        self.assertEqual(response.status_code, 302)



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

        # form = self.form({k
        #     'username': 'login',
        #     'password' : '123456'
        # })