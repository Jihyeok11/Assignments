from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = [
            "id",
            "gender_concept_id",
            "race_concept_id", # 인종
            "ethnicity_concept_id", # 민족
        ]