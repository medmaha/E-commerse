from django.test import TestCase

from store.models import Category, Product
from django.contrib.auth.models import User

class TestCategoryModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_categories_model_entry(self):
        '''
        Test Category model data insertion/type/field attribute
        '''
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_categories_model_entry(self):
        '''
        Test Category return name
        '''
        data = self.data1
        self.assertEqual(str(data), 'django')


class TestProductModel(TestCase):

    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(
            category_id=1,
            title='Django biginners',
            created_by_id=1,
            slug='django biginners',
            price=20.25,
            image='django',
        )

    def test_categories_model_entry(self):
        '''
        Test Category return name
        '''
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'Django biginners')
