from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    @property
    def group(self):
        groups = self.groups.all()
        return groups[0].name if groups else None


class Patient(models.Model):
    name = models.CharField(max_length=200)
    birthdate = models.DateField()
    wilaya = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos', null=True, blank=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient_name = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()


class Drug(models.Model):
    commercial_name = models.CharField(max_length=200)
    scientific_name = models.CharField(max_length=200)


class Consultation(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=200)
    description = models.TextField()
    outcome = models.TextField()
    patient = models.ForeignKey(Patient, related_name='consultations', on_delete=models.CASCADE)


class PrescriptionField(models.Model):
    consultation = models.ForeignKey(Consultation, related_name='prescription_fields', on_delete=models.CASCADE)
    drug = models.ForeignKey(Drug, related_name='prescription_fields', on_delete=models.CASCADE)
    quantity = models.CharField(max_length=200)
    times_per_day = models.IntegerField()
