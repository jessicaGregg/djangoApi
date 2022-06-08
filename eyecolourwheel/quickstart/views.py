from django.shortcuts import render
from eyecolourwheel.quickstart.serializers import EyeColourSerializer
from eyecolourwheel.quickstart.models import EyeColour
from rest_framework.viewsets import ModelViewSet, GenericViewSet

# Create your views here.
# Get all eye colours


class EyeColourList(ModelViewSet):
    queryset = EyeColour.objects.all()
    serializer_class = EyeColourSerializer

    def get_serializer_context(self):
        return {'request': self.request}
