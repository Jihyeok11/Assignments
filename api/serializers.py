from .models import Person,VisitOccurence
from rest_framework import serializers

class PersonSerializer(serializers.Serializer):
    class Meta:
        model = Person
        fields = [
            "person_id",
            "gender_concept_id",
            "race_concept_id",
            "ethnicity_concept_id",

        ]