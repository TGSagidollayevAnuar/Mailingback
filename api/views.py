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

class UserView(APIView):
    def get(self, request):
        try:
            users = User.objects.all()
        except:
            return JsonResponse({"LMAOOO": "error occured"}, safe=False)
        return JsonResponse(UserSerializer(users, many=True).data, safe=False)

    def post(self, request):
        User.objects.create(name=request.data.get('username'))
        return JsonResponse({"asd": "asd"}, safe=False)

@api_view(['PUT', 'DELETE'])
def user_actions(request, id):
    user = User.objects.get(id=id)
    
    if request.method == 'DELETE':
        user.delete()
        return JsonResponse({"deleted":""}, safe=False)

    elif request.method == 'PUT':
        user.name = request.data.get('username')
        user.save()

