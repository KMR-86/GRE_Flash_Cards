from django.test import TestCase

from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from words.views import word_list
from rest_framework import status


# Create your tests here.
class word_list_test(APITestCase):

    def test_see_all_words(self):
        response = self.client.get('/get_all_words/')
        self.assertEqual(200, response.status_code)


class word_search(APITestCase):

    def test_see_all_words(self):
        response = self.client.get('/search/a/')
        print(response)
        self.assertEqual(200, response.status_code)


class word_post(APITestCase):

    def test_word_post(self):
        url = "/get_all_words/"
        data = {
            "word": "portand",
            "meaning": "be a sign of warning of something",
            "sentence1": "sdfdsf",
            "sentence2": "sdfdsf",
            "etymology": "sdfdsf",
            "mnemonic": "sdfdsf",
            "hardness_level": 5
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
