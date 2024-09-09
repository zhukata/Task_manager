from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class UserTestView(TestCase):
    fixtures = ["labels.json",
                'statuses.json',
                'tasks.json',
                'users.json',
                ]

    def test_list_users(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/users.html')
        self.assertEqual(len(response.context["users"]), 2)
        print([x.username for x in get_user_model().objects.all()])
        # self.assertEqual(response.context["title"], 'users')###

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/users/login/?next=/tasks/')
    
    def test_logged(self):
        self.client.login(username='test_user2', password='123456')
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        response = self.client.post(reverse('user_create'), {
            'username': 'test_user3',
            'first_name': 'test',
            'last_name': 'test',
            'password1': '123456test',
            'password2': '123456test',
        })
        self.assertTrue(get_user_model().objects.filter(username='test_user3').exists())
        self.assertRedirects(response, expected_url=reverse('user_login'))
    
    def test_update_user(self):
        self.client.login(username='test_user', password='123456')
        response = self.client.post(reverse('user_update', args=[1]), {
            'username': 'test_current',
            'first_name': 'test',
            'last_name': 'test',
            'password1': '123456test',
            'password2': '123456test',
        })
        self.assertTrue(get_user_model().objects.get(id=1) == 'test_current')

    # def test_user_delete(self):
    #     user = self.user.objects.create_user(username='testuser2', password='12345')
    #     response = self.client.get(reverse('user_delete', kwargs={'pk': user.pk,}), ) # pk??
    #     self.assertEqual(response.status_code, 302)


