from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from task_manager.statuses.forms import StatusCraeteForm
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task


class StatusTest(TestCase):

    def setUp(self):
        self.form = StatusCraeteForm
        self.model = Status
        self.test_user1 = get_user_model().objects.create_user(username='testuser1', password='123456')
        self.test_user1.save()
        self.client.login(username='testuser1', password='123456')
        test_status = self.model.objects.create(name='lol')
        test_status.save()

    def test_all_statuses_get(self):
        response = self.client.get(reverse('statuses'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'statuses/statuses.html')

    def test_create_status_get(self):
        response = self.client.get(reverse('status_create'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'layouts/create.html')
        # self.assertContains(response,'<form')
        # self.assertTrue('name', self.form.Meta.fields)


    def test_create_status_post(self):

        response = self.client.post(reverse('status_create'), {
            'name': 'lose'
        })

        self.assertRedirects(response, expected_url=reverse('statuses'))
        self.assertTrue(self.model.objects.filter(name='lose').exists())












    # def test_update_status_get(self):
    #     self.client.login(username='testuser1', password1='123456')

    #     self.model.objects.create(name='test_status')

    #     response = self.client.get(reverse('status_update', kwargs={'pk':1,}))

    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'statuses/update.html')
    #     self.assertContains(response,'<form')
    #     self.assertTrue('name', self.form.Meta.fields)

    # def test_update_status_post(self):
    #     self.client.login(username='testuser1', password1='123456')
    #     self.model.objects.create(name='test_status')

    #     response = self.client.post(reverse('status_update', kwargs={'pk':1,}), {
    #         'name': 'lose'
    #     })

    #     # self.assertRedirects(response, expected_url=reverse('statuses'))
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(self.model.objects.get(id=1).name, 'lose')

    # def test_delete_status_get(self):

    #     self.client.login(username='testuser1', password1='123456')
    #     self.model.objects.create(name='test_status')

    #     response = self.client.get(reverse('status_delete'), kwargs={'pk': 1, })

    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'statuses/delete.html')
    #     self.assertContains(response, '<form')
    #     self.assertTrue('name', self.form.Meta.fields)

    # def test_delete_status_post(self):
    #     self.client.login(username='testuser1', password1='123456')

    #     response = self.client.post(reverse('status_delete'), args=[1])
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(self.model.objects.count, 0)
