from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):
    databases = '__all__'
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_contact_page_status_code(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
    
    def test_category_page_status_code(self):
        response = self.client.get('/category/')
        self.assertEqual(response.status_code, 200)
    
    def test_typpro_page_status_code(self):
        response = self.client.get('/category/typpro/')
        self.assertEqual(response.status_code, 200)
    
    def test_typbus_page_status_code(self):
        response = self.client.get('/category/typbus/')
        self.assertEqual(response.status_code, 200)
    
    def test_typgame_page_status_code(self):
        response = self.client.get('/category/typgame/')
        self.assertEqual(response.status_code, 200)

    def test_typgph_page_status_code(self):
        response = self.client.get('/category/typgph/')
        self.assertEqual(response.status_code, 200)

    def test_typstud_page_status_code(self):
        response = self.client.get('/category/typstud/')
        self.assertEqual(response.status_code, 200)
    
    