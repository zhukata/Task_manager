from django.test import TestCase
from django.urls import reverse

from task_manager.labels.models import Label

class LabelListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass # 5 лейблов в фикстуре

    def test_list_view(self):
        resp = self.client.get(reverse('labels'))
        self.assertEqual(resp.status_code, 200)

    def test_view_template(self):
        resp = self.client.get(reverse('labels'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'labels/labels.html')
        resp.context() # == 
    
    def test_delete(self):
        # создаем task 
        #  добавляем лейбл 
        # пробуем удалить
        pass
