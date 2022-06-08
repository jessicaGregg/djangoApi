from django.shortcuts import render
from eyecolourwheel.quickstart.serializers import EyeColourSerializer
from eyecolourwheel.quickstart.models import EyeColour
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from django.http.response import JsonResponse
# Create your views here.
# Get all eye colours


class EyeColourList(ModelViewSet):
    queryset = EyeColour.objects.all()
    serializer_class = EyeColourSerializer

    def get_serializer_context(self):
        return {'request': self.request}

    def create(self, request, *args, **kwargs):
        print(request.POST['eyeColour'])
        if request.POST['eyeColour'] == 'HZ':
            colourMatch = "Brown"
        elif request.POST['eyeColour'] == 'BLU':
            colourMatch = "Orange"
        elif request.POST['eyeColour'] == 'BRW':
            colourMatch = "Pink"
        elif request.POST['eyeColour'] == 'GR':
            colourMatch = "Blue"
        super().create(request, *args, **kwargs)
        return JsonResponse({'matches': colourMatch})
