from django.db import models

# Create your models here.
class jobfair(models.Model):
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
    eventname=models.CharField(max_length=100)
    eventdate=models.CharField(max_length=100)
    seminarperson=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    technology=models.CharField(max_length=100)
    deptment=models.CharField(max_length=7, choices=DEPARTMENT_CHOICES, default='MCA')
    companyname=models.CharField(max_length=100)
    eligibility=models.CharField(max_length=100)
    cgb=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    place=models.CharField(max_length=100)

    def __str__(self):
        return self.deptment