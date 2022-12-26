from django.test import SimpleTestCase
from django.urls import reverse, resolve
from task1.views import home


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):    # Write this URL for each and every URL
        url = reverse('home')

        # url = reverse('home', args=[list_of_arg])    # Use this URL if url is taking argument
        # print(resolve(url))
        self.assertEquals(resolve(url).func, home)   # It means function belonging to URL should match to home view function
        # self.assertEquals(resolve(url).func.view_class, ClassbasedView)    # use func.view_class if it is class based view
