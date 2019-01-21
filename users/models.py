from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # add additional fields in here
    DESTINATION_CHOICES = (
        ('STUDENT', 'Student'),
        ('HOD', 'HOD'),
    )
    DEPARTMENT_CHOICES = (
        ('MCA', 'MCA'),
        ('MSc', 'MSc'),
        ('BCA', 'BCA'),
        ('BSC(IT)', 'BSC(IT)'),
        ('BSC(CS)', 'BSC(CS)'),
        ('VISCOM', 'VISCOM'),
        ('BBA', 'BBA'),
        ('SSA', 'SSA'),
        ('BA', 'BA'),
        ('MA', 'MA'),
        ('Bcom(CA)','Bcom(CA)')
    )

    department=models.CharField(max_length=7, choices=DEPARTMENT_CHOICES, default='MCA')
    qualification=models.CharField(max_length=200)
    destination=models.CharField(max_length=7, choices=DESTINATION_CHOICES, default='STUDENT')
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=40)
    state=models.CharField(max_length=30)
    country=models.CharField(max_length=30)
    mobileno=models.CharField(max_length=12)
    alternativemobileno=models.CharField(max_length=12)


    def __str__(self):
        return self.email