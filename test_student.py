import unittest
from student import Student


class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')
    
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Smith')

    def test_full_name(self):
        print('test full name')
        self.assertEqual(self.student.full_name, 'John Smith')

    def tearDown(self):
        print('tearDown')
        
    def test_alert_santa(self):
        print('test alert santa')
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        print('test email')
        self.assertTrue(self.student.email, 'john.smith@email.com')

if __name__ == '__main__':
    unittest.main()