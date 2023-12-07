from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class SendMail(APIView):
    def post(self,request):
        email=request.data['to']
        emailw=EmailMessage(
            'Test email subject',
            'Test email body, this msg is from python',
            settings.EMAIL_HOST_USER,
            [email]
        )        
        emailw.send(fail_silently=False)
        return Response({'status':True,'message':'Email send successfully'})
 