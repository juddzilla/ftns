from rest_framework import serializers
from .models import Exercise

class CommaSeparatedArrayField(serializers.ListField):
    def to_representation(self, obj):
        if isinstance(obj, list):
            return ','.join(obj)
        stripped = obj.strip('{}')
        cleaned = stripped.replace('"', '')
        return cleaned.split(',')

    def to_internal_value(self, data):        
        return data.split(',')

class ExerciseSerializer(serializers.ModelSerializer):
    primary_muscles = CommaSeparatedArrayField(child=serializers.CharField())
    secondary_muscles = CommaSeparatedArrayField(child=serializers.CharField())
    
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'aliases', 'primary_muscles', 'secondary_muscles', 'force', 'level', 'mechanic', 'equipment', 'category', 'instructions', 'description', 'tips', 'date_created', 'date_updated']