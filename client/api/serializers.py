from rest_framework import serializers
from client.models import Client

class ClientSerializers(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    modified_by = serializers.StringRelatedField()
        
    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'created_by', 'modified_at', 'modified_by']

    def validate_client_id(self, value):
        if not value.startswith('Cid-'):
            return f'Cid-{value}'
        return value

class ClientGetSerializers(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    modified_by = serializers.StringRelatedField()
    
    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'created_by', 'modified_at', 'modified_by'] 
