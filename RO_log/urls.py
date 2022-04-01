from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .models import RO
from . import api_views


app_name = 'RO_log'

urlpatterns= [
    path('',views.ROTodayArchiveView.as_view(),name='archive_day'),
    path('login/',views.CustomLoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('report/',views.ROList.as_view(),name='report'),
    path('create/',views.ROCreate.as_view(),name='create'),
    path('update/<int:pk>/', views.ROUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.RODelete.as_view(), name='delete'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('payperiod/',views.PayPeriodList.as_view(),name='payperiod-list'),
    path('payperiod/create',views.PayPeriodCreate.as_view(),name='payperiod-create'),
    path('payperiod/update/<int:pk>/',views.PayPeriodUpdate.as_view(),name='payperiod-update'),
    path('payperiod/delete/<int:pk>/',views.PayPeriodDelete.as_view(),name='payperiod-delete'),
    path('dashboard/',views.DashboardView.as_view() ,name='dashboard'),
    path('api/payperiod/',api_views.PayPeriodList.as_view()),
    path('api/ro/',api_views.ROList.as_view()),

]
