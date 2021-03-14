from django.test import TestCase

# Create your tests here.

class DummyTestCase(TestCase):
    
    def test_dummy_test_case(self):
        self.assertEqual(1, 1)