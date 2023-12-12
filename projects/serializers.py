from rest_framework import serializers
from .models import Profile, Project, CertifyingInstitution, Certificate


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


class NestedCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'name', 'profiles']


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = NestedCertificateSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        fields = ['certificates', 'id', 'name', 'url']

    def create(self, validated_data):
        certificate_data = validated_data.pop('certificates')
        certifying_institution = CertifyingInstitution.objects.create(
            **validated_data)
        for certificate in certificate_data:
            CertificateSerializer().create({
                'certifying_institution': certifying_institution,
                **certificate
            })
        return certifying_institution
