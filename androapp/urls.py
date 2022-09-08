
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.login,name="home"),
    path('logout/',views.logout,name="logout"),
    path('register/', views.register,name="home"),
    path('dashboard/', views.dashboard,name="dashboard"),
    path('viewapps/',views.viewApps,name="viewApps"),
    path('addapp/',views.addApp,name="addapp"),
    path('deleteapp/<int:appid>',views.deleteApp,name="deleteapp"),
    path('updateapp/<int:appid>',views.updateApp,name="updateapp"),
    path('adduser/',views.adduser,name="adduser"),
    path('viewusers/',views.viewusers,name="viewusers"),

    path('points/',views.userpoints,name="viewpoints"),
    path('tasks/',views.tasks,name="tasks"),

    path('regdata/', views.regdata,name="regdata"),
]