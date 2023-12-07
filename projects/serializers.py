from rest_framework import serializers
from .models import Profile, Project, CertifyingInstitution, Certificate


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'github', 'linkedin', 'bio']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'description',
            'github_url',
            'keyword',
            'key_skill',
            'profile'
        ]


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertifyingInstitution
        fields = ['id', 'name', 'url']


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = [
            'id',
            'name',
            'certifying_institution',
            'timestamp',
            'profiles'
        ]
