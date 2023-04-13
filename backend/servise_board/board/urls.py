from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('api/user/', views.UserView.as_view()),
    path('api/order/', views.OrderView.as_view()),
    path('api/registrationUser/', views.RegistrationUserView.as_view()),
    path('api/registrationContractor/', views.RegistrationContractorView.as_view()),
    path('token/', obtain_auth_token),
    path('rgstr_user/', views.login_user_view),
    path('rgstr_contractor', views.login_contractor_view),
    path('api/categories/', views.CategoryList.as_view())
]