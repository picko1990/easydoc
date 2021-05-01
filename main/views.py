from django.http import JsonResponse
from .models import Patient, Appointment, Drug, Consultation, PrescriptionField
from .serializers import PatientSerializer, AppointmentSerializer, ConsultationSerializer,\
    DrugSerializer, PrescriptionFieldSerializer, NestedPatientSerializer, NestedConsultationSerializer, LogInSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework_simplejwt.views import TokenObtainPairView


class LogInView(TokenObtainPairView):
    serializer_class = LogInSerializer


@api_view(['GET'])
def api_root(request):
    return Response({
        'login': reverse('log_in', request=request),
        'patients': reverse('patients-list', request=request),
        'appointments': reverse('appointments-list', request=request),
        'drugs': reverse('drugs-list', request=request),
        'consultations': reverse('consultations-list', request=request),
        'prescription_fields    ': reverse('prescription_fields-list', request=request),
    })


def ping(request):
    ppp = {'ping': 'pong'}
    return JsonResponse(ppp)


class PatientList(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()


class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NestedPatientSerializer
    queryset = Patient.objects.all()


class AppointmentList(generics.ListCreateAPIView):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        queryset = Appointment.objects.all()
        date = self.request.query_params.get('date')
        print(date)
        if date is not None:
            queryset = queryset.filter(date=date)
        return queryset


class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()


class DrugList(generics.ListCreateAPIView):
    serializer_class = DrugSerializer
    queryset = Drug.objects.all()


class DrugDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DrugSerializer
    queryset = Drug.objects.all()


class ConsultationList(generics.ListCreateAPIView):
    serializer_class = ConsultationSerializer
    queryset = Consultation.objects.all()


class ConsultationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NestedConsultationSerializer
    queryset = Consultation.objects.all()


class PrescriptionFieldList(generics.ListCreateAPIView):
    serializer_class = PrescriptionFieldSerializer
    queryset = PrescriptionField.objects.all()


class PrescriptionFieldDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PrescriptionFieldSerializer
    queryset = PrescriptionField.objects.all()
