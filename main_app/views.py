from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import patient, doctor, diseaseinfo, consultation, rating_review
import pickle
import numpy as np
from datetime import date


# Disease prediction functionality
def load_model():
    """Load the trained machine learning model"""
    try:
        with open('trained_model', 'rb') as f:
            model = pickle.load(f)
        return model
    except FileNotFoundError:
        return None


def predict_disease(symptoms):
    """Predict disease based on symptoms"""
    model = load_model()
    if model is None:
        return None, 0.0
    
    # This would need to be implemented based on your specific model
    # For now, returning placeholder values
    return "Common Cold", 0.85


def index(request):
    """Homepage view"""
    return render(request, 'homepage/index.html')


def about(request):
    """About page view"""
    return render(request, 'homepage/about.html')


@login_required
def patient_ui(request):
    """Patient dashboard view"""
    try:
        patient_obj = patient.objects.get(user=request.user)
        context = {
            'patient': patient_obj,
            'diseases': diseaseinfo.objects.filter(patient=patient_obj),
            'consultations': consultation.objects.filter(patient=patient_obj)
        }
        return render(request, 'patient/patient_ui.html', context)
    except patient.DoesNotExist:
        messages.error(request, 'Patient profile not found.')
        return redirect('index')


@login_required
def doctor_ui(request):
    """Doctor dashboard view"""
    try:
        doctor_obj = doctor.objects.get(user=request.user)
        context = {
            'doctor': doctor_obj,
            'consultations': consultation.objects.filter(doctor=doctor_obj),
            'patients': patient.objects.all()
        }
        return render(request, 'doctor/doctor_ui.html', context)
    except doctor.DoesNotExist:
        messages.error(request, 'Doctor profile not found.')
        return redirect('index')


@login_required
def admin_ui(request):
    """Admin dashboard view"""
    if not request.user.is_superuser:
        messages.error(request, 'Access denied.')
        return redirect('index')
    
    context = {
        'total_patients': patient.objects.count(),
        'total_doctors': doctor.objects.count(),
        'total_consultations': consultation.objects.count(),
        'recent_consultations': consultation.objects.order_by('-consultation_date')[:10]
    }
    return render(request, 'admin/admin_ui.html', context)


@login_required
def disease_predict(request):
    """Disease prediction view"""
    if request.method == 'POST':
        symptoms = request.POST.getlist('symptoms')
        
        if not symptoms:
            messages.error(request, 'Please select at least one symptom.')
            return render(request, 'patient/disease_predict.html')
        
        # Predict disease
        disease_name, confidence = predict_disease(symptoms)
        
        if disease_name:
            # Save disease info
            try:
                patient_obj = patient.objects.get(user=request.user)
                disease_info = diseaseinfo.objects.create(
                    diseasename=disease_name,
                    no_of_symp=len(symptoms),
                    symptomsname=symptoms,
                    confidence=confidence,
                    patient=patient_obj
                )
                
                context = {
                    'disease': disease_info,
                    'recommended_doctors': doctor.objects.filter(
                        specialization__icontains=disease_name
                    )[:5]
                }
                return render(request, 'patient/prediction_result.html', context)
            except patient.DoesNotExist:
                messages.error(request, 'Patient profile not found.')
                return redirect('patient_ui')
        else:
            messages.error(request, 'Unable to predict disease. Please try again.')
    
    return render(request, 'patient/disease_predict.html')


@login_required
def consultation_history(request):
    """View consultation history"""
    try:
        if hasattr(request.user, 'patient'):
            consultations = consultation.objects.filter(patient=request.user.patient)
        elif hasattr(request.user, 'doctor'):
            consultations = consultation.objects.filter(doctor=request.user.doctor)
        else:
            consultations = consultation.objects.all()
        
        context = {'consultations': consultations}
        return render(request, 'consultation_history.html', context)
    except Exception as e:
        messages.error(request, 'Error loading consultation history.')
        return redirect('index')


@login_required
def pconsultation_history(request):
    """Patient consultation history"""
    try:
        patient_obj = patient.objects.get(user=request.user)
        consultations = consultation.objects.filter(patient=patient_obj)
        context = {'consultations': consultations}
        return render(request, 'patient/consultation_history.html', context)
    except patient.DoesNotExist:
        messages.error(request, 'Patient profile not found.')
        return redirect('index')


@login_required
def dconsultation_history(request):
    """Doctor consultation history"""
    try:
        doctor_obj = doctor.objects.get(user=request.user)
        consultations = consultation.objects.filter(doctor=doctor_obj)
        context = {'consultations': consultations}
        return render(request, 'doctor/consultation_history.html', context)
    except doctor.DoesNotExist:
        messages.error(request, 'Doctor profile not found.')
        return redirect('index')


@login_required
def rate_doctor(request, doctor_id):
    """Rate a doctor"""
    if request.method == 'POST':
        try:
            doctor_obj = doctor.objects.get(id=doctor_id)
            patient_obj = patient.objects.get(user=request.user)
            
            rating_value = int(request.POST.get('rating', 0))
            review_text = request.POST.get('review', '')
            
            if 1 <= rating_value <= 5:
                rating_review.objects.create(
                    rating=rating_value,
                    review=review_text,
                    doctor=doctor_obj,
                    patient=patient_obj
                )
                
                # Update doctor's average rating
                reviews = rating_review.objects.filter(doctor=doctor_obj)
                avg_rating = sum(r.rating for r in reviews) / len(reviews)
                doctor_obj.rating = avg_rating
                doctor_obj.save()
                
                messages.success(request, 'Thank you for your rating!')
            else:
                messages.error(request, 'Please provide a valid rating (1-5).')
                
        except (doctor.DoesNotExist, patient.DoesNotExist, ValueError):
            messages.error(request, 'Error submitting rating.')
    
    return redirect('pconsultation_history')
