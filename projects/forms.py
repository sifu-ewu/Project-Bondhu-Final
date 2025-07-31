
from django import forms
from .models import Post, Comment, Contact, Appointment, Prescription


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('name', 'email', 'phonenumber', 'doc_name')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phonenumber': forms.NumberInput(attrs={'class': 'form-control'}),
            'doc_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ('Patient_name', 'patient_age', 'medicine', 'doc_name', 'patient_disease', 'advice')

        widgets = {
            'Patient_name': forms.TextInput(attrs={'class': 'form-control'}),
            'patient_age': forms.NumberInput(attrs={'class': 'form-control'}),
            'medicine': forms.TextInput(attrs={'class': 'form-control'}),
            'doc_name': forms.TextInput(attrs={'class': 'form-control'}),
            'patient_disease': forms.TextInput(attrs={'class': 'form-control'}),
            'advice': forms.Textarea(attrs={'class': 'form-control'}),
        }
