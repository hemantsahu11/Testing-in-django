from django.test import SimpleTestCase
from task1.forms import PostForm


class TestForm(SimpleTestCase):

    def test_post_form_validate_data(self):
        form = PostForm(data={
            'title': 'mypost1',
            'content': 'this is post by hemant'
        })

        self.assertTrue(form.is_valid())

    def test_post_form_no_data(self):
        form = PostForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)