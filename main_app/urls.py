from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('patient_ui/', views.patient_ui, name='patient_ui'),
    path('doctor_ui/', views.doctor_ui, name='doctor_ui'),
    path('admin_ui/', views.admin_ui, name='admin_ui'),
    path('disease_predict/', views.disease_predict, name='disease_predict'),
    path('consultation_history/', views.consultation_history, name='consultation_history'),
    path('pconsultation_history/', views.pconsultation_history, name='pconsultation_history'),
    path('dconsultation_history/', views.dconsultation_history, name='dconsultation_history'),
    path('rate_doctor/<int:doctor_id>/', views.rate_doctor, name='rate_doctor'),
]
