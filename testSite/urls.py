"""
URL configuration for testSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from coffe.views import CoffeAPIView
from coffe.views import CatAPIView
from coffe.views import TasteAPIView
from coffe.views import FavAPIView
from coffe.views import AllergensAPIView
from coffe.views import StoresAPIView
from coffe.views import OrdersHistoryAPIView
from coffe.views import RewardsHistoryAPIView
from coffe.views import SpecialsAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/coffes', CoffeAPIView.as_view()),
    path('api/v1/categories', CatAPIView.as_view()),
    path('api/v1/tastes', TasteAPIView.as_view()),
    path('api/v1/favourites', FavAPIView.as_view()),
    path('api/v1/allergens', AllergensAPIView.as_view()),
    path('api/v1/stores', StoresAPIView.as_view()),
    path('api/v1/ordershistory', OrdersHistoryAPIView.as_view()),
    path('api/v1/rewardshistory', RewardsHistoryAPIView.as_view()),
    path('api/v1/specials', SpecialsAPIView.as_view()),
]
