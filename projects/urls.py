from rest_framework import routers
from django.urls import path, include
from .views import (
    ProfileViewSet,
    ProjectViewSet,
    CertifyingInstitutionViewSet,
    CertificateViewSet
)

router = routers.DefaultRouter()
router.register('profiles', ProfileViewSet)
router.register('projects', ProjectViewSet)
router.register('certifying-institutions', CertifyingInstitutionViewSet)
router.register('certificates', CertificateViewSet)

urlpatterns = [
    path('', include(router.urls))
]
