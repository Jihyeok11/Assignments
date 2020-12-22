from rest_framework import serializers
from .models import Person,Gender


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = [
            "id",
            "gender_concept_id",
            "race_concept_id", # 인종
            "ethnicity_concept_id", # 민족
        ]

class GenderSerializer(serializers.ModelSerializer):
    person = PersonSerializer(read_only=True, many=False)
    class Meta:
        model = Gender
        fields = [
            "person_id",
            "gender_concept_id"
        ]