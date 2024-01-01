from django.test import TestCase
# from django.urls import resolve
# from lists.views import home_page
class HomePageTest(TestCase):
    
    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/') # substitui o teste acima
        # html = response.content.decode('utf8')
        # self.assertTrue(html.startswith('<html>'))
        # self.assertIn('<title>To-do lists</title>', html)
        self.assertTemplateUsed(response, 'home.html') # substitui os testes acima evitando hardcode