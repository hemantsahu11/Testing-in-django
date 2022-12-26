from django.test import TestCase, Client
from django.urls import reverse
from task1.models import Post
import json


class TestView(TestCase):

    def setUp(self):    # this method will be executed before all the test cases and initialize the required variables
        self.client = Client()    # reusability
        self.home_url = reverse('home')

    def test_project_home_get(self):
        client = Client()
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)   # matching status code of the response
        # self.assertTemplateUsed(response, 'task1/htmlfile')

    # def test_project_home_post(self):   # test case of post method
    #     Post.objects.create(
    #         title='mypost',
    #         content='post by hemant'
    #     )
    #
    #     response = self.client.post(self.post_url, {    # for post request
    #         'title': 'mypost',
    #         'content': 'Post by hemant'
    #     })
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEquals()   # you can compare more things
