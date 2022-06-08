from rest_framework import serializers
from eyecolourwheel.quickstart.models import EyeColour

class EyeColourSerializer(serializers.ModelSerializer):
    class Meta:
        model = EyeColour
        fields = '__all__'
