"""
URL configuration for CRUD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from events.views import welcome,addEvent,getEvents,getEventByID,updateEvent,deleteEvent,getEventByPaginate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', welcome, name="welcome"),
    path('api/event/add', addEvent, name="addEvent"),
    path('api/events/', getEvents, name="getEvent"),
    path('api/event/<int:id>/', getEventByID, name="getEventByID"),
    path('api/edit/<int:id>/', updateEvent, name="updateEvent"),
    path('api/delete/<int:id>/', deleteEvent, name="deleteEvent"),
    path('api/events/paginate', getEventByPaginate, name="getEventByPaginate")
]
