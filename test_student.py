import unittest
from datetime import date, timedelta
from student import Student
from unittest.mock import patch

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

    def test_apply_extension(self):
        print('test apply extension')
        self.assertTrue(self.student.apply_extension(30), self.student.end_date > self.student._start_date + timedelta(days=365))
    
    def test_course_schedule_success(self):
        with patch('student.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success!"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success!")
    
    def test_course_schedule_failure(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong")

if __name__ == '__main__':
    unittest.main()