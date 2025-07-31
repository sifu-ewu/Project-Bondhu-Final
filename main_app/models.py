from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_patient = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    dob = models.DateField()
    img = models.ImageField(upload_to='pics', blank=True)
    address = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=True)
    name = models.CharField(max_length=50)
    dob = models.DateField()
    img = models.ImageField(upload_to='pics', blank=True)
    address = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    registration_no = models.CharField(max_length=20)
    year_of_registration = models.DateField()
    qualification = models.CharField(max_length=20)
    State_Medical_Council = models.CharField(max_length=30)
    specialization = models.CharField(max_length=30)
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class diseaseinfo(models.Model):
    diseasename = models.CharField(max_length=200)
    no_of_symp = models.IntegerField()
    symptomsname = ArrayField(models.CharField(max_length=200))
    confidence = models.DecimalField(max_digits=5, decimal_places=2)
    consultdoctor = models.CharField(max_length=200)
    patient = models.ForeignKey(patient, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.diseasename


class consultation(models.Model):
    consultation_date = models.DateField()
    messages = ArrayField(models.CharField(max_length=100), blank=True)
    status = models.CharField(max_length=20)
    diseaseinfo = models.OneToOneField(diseaseinfo, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(doctor, on_delete=models.SET_NULL, null=True)
    patient = models.ForeignKey(patient, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Consultation on {self.consultation_date}"


class rating_review(models.Model):
    rating = models.IntegerField()
    review = models.TextField()
    doctor = models.ForeignKey(doctor, on_delete=models.SET_NULL, null=True)
    patient = models.ForeignKey(patient, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Rating: {self.rating} for Dr. {self.doctor.name if self.doctor else 'Unknown'}"
