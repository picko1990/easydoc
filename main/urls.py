from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root),
    path('api/log_in/', views.LogInView.as_view(), name='log_in'),
    path('ping', views.ping, name='ping'),
    path('patients/', views.PatientList.as_view(), name='patients-list'),
    path('patients/<int:pk>/', views.PatientDetail.as_view()),
    path('appointments/', views.AppointmentList.as_view(), name='appointments-list'),
    path('appointments/<int:pk>/', views.AppointmentDetail.as_view()),
    path('drugs/', views.DrugList.as_view(), name='drugs-list'),
    path('drugs/<int:pk>/', views.DrugDetail.as_view()),
    path('consultations/', views.ConsultationList.as_view(), name='consultations-list'),
    path('consultations/<int:pk>/', views.ConsultationDetail.as_view()),
    path('prescription_fields/', views.PrescriptionFieldList.as_view(), name='prescription_fields-list'),
    path('prescription_fields/<int:pk>/', views.PrescriptionFieldDetail.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
