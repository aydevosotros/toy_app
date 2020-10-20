from rest_framework import serializers

from welcome.models import Visit


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'
