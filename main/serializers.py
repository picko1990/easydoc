from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Patient, Appointment, Drug, Consultation, PrescriptionField


class UserSerializer(serializers.ModelSerializer):
    group = serializers.CharField()

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'group']
        read_only_fields = ('id',)


class LogInSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        user_data = UserSerializer(user).data
        for key, value in user_data.items():
            if key != 'id':
                token[key] = value
        return token


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = '__all__'


class PrescriptionFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionField
        fields = '__all__'


class NestedPrescriptionFieldSerializer(serializers.ModelSerializer):
    drug = DrugSerializer()

    class Meta:
        model = PrescriptionField
        fields = '__all__'


class ConsultationSerializer(serializers.ModelSerializer):
    prescription_fields = NestedPrescriptionFieldSerializer(many=True, read_only=True)

    class Meta:
        model = Consultation
        fields = '__all__'


class NestedPatientSerializer(serializers.ModelSerializer):
    consultations = ConsultationSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = '__all__'


class NestedConsultationSerializer(serializers.ModelSerializer):
    prescription_fields = PrescriptionFieldSerializer(many=True, read_only=True)
    patient = PatientSerializer()

    class Meta:
        model = Consultation
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

