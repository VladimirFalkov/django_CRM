from django.db import models


class Record(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=55)
    state = models.CharField(max_length=55)
    zipcode = models.CharField(max_length=25)

    def __str__(self) -> str:
        return (f'{self.first_name} {self.last_name} {self.city}' )
    
