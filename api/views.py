from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http.response import JsonResponse
from api.models import User, Manager, Mail, Draft
from api.serializers import UserSerializer, ManagerSerializer, MailSerializer, DraftSerializer

class MailView(APIView):
    def post(self, request):
        try:
            author = User.objects.get(name=request.data.get('author'))
            receiver = User.objects.get(name=request.data.get('receiver'))
        except:
            return JsonResponse({"bad response": "problem with users"}, safe=False)

        Mail.objects.create(
            title = request.data.get('title'),
            text = request.data.get('text'),
            receiver = receiver,
            author = author
        )
        return JsonResponse({"good response": "message is sent"}, safe=False)
    
    def get(self, request):
        try:
            mails = Mail.objects.all()
        except:
            return JsonResponse({"LMAOOO": "error occured"}, safe=False)
        
        return JsonResponse(MailSerializer(mails, many=True).data, safe=False)


