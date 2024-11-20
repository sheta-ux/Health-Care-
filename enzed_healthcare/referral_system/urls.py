from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),

    path('people/', views.person_list, name='person_list'),
    path('people/add/', views.person_create, name='person_add'),
    path('people/<int:pk>/', views.person_detail, name='person_detail'),
    path('people/<int:pk>/edit/', views.person_update, name='person_edit'),
    path('people/<int:pk>/delete/', views.person_delete, name='person_delete'),

    path('referrals/', views.referral_list, name='referral_list'),
    path('referrals/add/', views.referral_create, name='referral_add'),
    path('referrals/<int:pk>/', views.referral_detail, name='referral_detail'),
    path('referrals/<int:pk>/edit/', views.referral_update, name='referral_edit'),
    path('referrals/<int:pk>/delete/', views.referral_delete, name='referral_delete'),

    path('login/', auth_views.LoginView.as_view(template_name='referral_system/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
