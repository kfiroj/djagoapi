from rest_framework import serializers
from .models import User, ActivityPeriod


class UserActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('uid', 'name', 'tz')