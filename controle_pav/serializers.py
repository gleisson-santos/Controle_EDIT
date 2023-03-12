from rest_framework import serializers
from controle_pav.models import Pavimento

class PavimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pavimento
        fields = '__all__'
