from django.urls import path
from api import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('mail/', views.MailView.as_view()),
    path('user/', views.UserView.as_view()),

   
    
]