from django.urls import path, include

from . import views

urlpatterns = [
    path('api/user/', views.UserView.as_view()),
    path('api/order/', views.OrderView.as_view()),
    path('api/registrationUser/', views.RegistrationUserView.as_view(), include('rest_framework.urls')),
    path('api/registrationContractor/', views.RegistrationContractorView.as_view(), include('rest_framework.urls'))
]
