"""PoliticalPartyAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from partyapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('politicalparty/', views.PoliticalPartyView.as_view()),
    path('politicalparty_pk/<int:pk>/', views.PoliticalPartyView.as_view()),

    path('politicalleader/',views.PoliticalLeaderView.as_view()),
    path('politicalleader_pk/<int:pk>/', views.PoliticalLeaderView.as_view()),

    path('development/',views.DevelopmentView.as_view()),
    path('development_pk/<int:pk>/', views.DevelopmentView.as_view()),

    path('politicalleaderbyparty/',views.PoliticalLeaderByPartyView.as_view()),
    path('developmentbyleader/',views.DevelopmentByLeaderView.as_view()),

]
