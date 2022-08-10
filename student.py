from datetime import date, timedelta

class Student:
    """
    A Student class as base for method testing
    """

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365) 
        # doesn't account for leap years
        self.naughty_list = False
    

    @property
    def full_name(self):
        return f'{self._first_name} {self._last_name}'
    
    def alert_santa(self):
        self.naughty_list = True
    
    @property
    def email(self):
        return f'{self._first_name.lower()}.{self._last_name.lower()}@email.com'
    
    def apply_extension(self, days):
        self.end_date += timedelta(days = days)
        return self.end_date