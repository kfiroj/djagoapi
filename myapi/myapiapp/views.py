from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserActivitySerializer
from .models import User, ActivityPeriod


# Create your views here.
class UserActivityViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('name')
    serializer_class = UserActivitySerializer
