from django.test import TestCase

from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from words.views import word_list


# Create your tests here.
class word_list_test(APITestCase):

    def test_see_all_words(self):
        response = self.client.get('/get_all_words/')
        self.assertEqual(200, response.status_code)



