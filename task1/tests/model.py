from django.test import TestCase
from task1.models import Post
from django.contrib.auth.models import User


class TestAppModel(TestCase):
    # def setUp(self):   # here also we can write a function that will be execute
    #     self.post = Post.objects.create()

    def test_model_str(self):
        title = Post.objects.create(title='Django testing')
        content = Post.objects.create(content='This is some content of testing')
        self.assertEqual(str(title), 'Django testing')

    def test_post_like_users(self):
        testuser1 = User.objects.create_user(username='testuser1', password='1234')
        testuser2 = User.objects.create_user(username='testuser2', password='1234')
        title = Post.objects.create(title='django', content='New content')
        title.likes.set([testuser1.pk, testuser2.pk])
        self.assertEqual(title.likes.count(), 2)
