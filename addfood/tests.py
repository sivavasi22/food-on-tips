from django.test import TestCase

# Create your tests here.
class Demotest(TestCase):
	def mytest(self):
		self.assertEqual(1+2,3)
		self.assertEqual(2+3,5)

class Demotest2(TestCase):
	def mytest(self):
		self.assertEqual(1+2,3)
		self.assertEqual(2+3,5)