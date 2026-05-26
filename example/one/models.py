from django.db import models

class Hospital(models.Model):
    name=models.CharField(max_length=30)
    city=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name=models.CharField(max_length=30)
    hospital=models.ForeignKey(Hospital,on_delete=models.CASCADE,related_name="hsptl")
    bill_amount=models.IntegerField()

    def __str__(self):
        return self.name











































# class Hospital(models.Model):
#     name = models.CharField(max_length=150)
#     city = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


# class Patient(models.Model):
#     hospital = models.ForeignKey(
#         Hospital,
#         on_delete=models.CASCADE,
#         related_name='patients'
#     )
#     name = models.CharField(max_length=100)
#     bill_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     is_admitted = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name

# 1)Admitted patients with hospital name.
# 2)Patients with bill between 5,000 and 20,000
# 3)Total bill amount per hospital
# 4)Patients from hospital city "Kochi"
# 5)Display patient name and hospital name
# 6)Admitted patients from hospital city "Calicut"