from rest_framework import serializers
from fish.models import Fish

class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fish
        fields = '__all__'
        # fields = ('fishId', 'fishDateTime', 'fishDateTime', 'fishType', 'fishTags', 'fishDetails')