from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RegisterSerialzer
# Create your views here.
from rest_framework.response import Response
from .models import *
from .utils import Util
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse


class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerialzer

    def post(self, request):
        user = request.data
        #Sending data to our serializer
        serializer = self.serializer_class(data = user)

        serializer.is_valid(raise_exception=True) # Validate method

        serializer.save()#Trigger create method

        user_data = serializer.data

        user = User.objects.get(email = user_data['email'])


        current_site = get_current_site(request).domain

        relativeLink = reverse('email-verify')

        absurl = 'http://' + current_site + relativeLink
        email_body = 'Hi ' + user.username + 'Use  link below to visit this issue \n' + absurl 
        data = {'domain': absurl, 'email_body':email_body, 'to_email':user.email, 'email_subject':'Verify  your email'}

        Util.send_email(data)


        return Response(user_data, status = status.HTTP_201_CREATED)


class VerifyEmail(generics.GenericAPIView):
    def get(self):
        pass