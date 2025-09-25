from rest_framework import serializers
from .models import KhorasanRate, SaraiRate, DaAfgRate

class KhorasanRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = KhorasanRate
        fields = '__all__'

class SaraiRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaraiRate
        fields = '__all__'

class DaAfgRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DaAfgRate
        fields = '__all__'