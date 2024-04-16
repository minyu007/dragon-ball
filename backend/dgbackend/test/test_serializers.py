from rest_framework import serializers
from base.models import TestDB

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestDB
        fields = '__all__'