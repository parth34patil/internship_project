from rest_framework import serializers
from .models import Item

# The ItemSerializer class converts a model instance to JSON format
# and handles data validation for incoming requests.
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        # Specifies the model to be serialized
        model = Item
        
        # 'fields = '__all__'' includes all fields from the Item model
        # in the serialized representation.
        fields = '__all__'