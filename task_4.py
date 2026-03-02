hourly_payment = 400

class EmployeeSalary:
    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
    
    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours is None:
            hours = (7 - rest_days) * 8
            return cls(name, hours, rest_days, email)
        else:
            return cls(name, hours, rest_days, email)
    
    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
            email = f"{name}@email.com"
            return cls(name, hours, rest_days, email)
        else:
            return cls(name, hours, rest_days, email)
    
    @classmethod
    def det_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment

    @staticmethod
    def salary(hours, hourly_payment):
        return hours * hourly_payment