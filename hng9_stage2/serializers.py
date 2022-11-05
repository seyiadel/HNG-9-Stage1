from rest_framework import serializers
from rest_enumfield import EnumField
from enum import Enum
class Operations(Enum):
    SUBTRACTION=0
    ADDITION=1
    MULTIPLICATION=2

class CalculationSerializer(serializers.Serializer):
    operation_type=serializers.CharField(max_length=76)
    x=serializers.IntegerField()
    y=serializers.IntegerField()