"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from project.views import home
from project import views as project_views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', project_views.loginPage, name='login'),
    path('logout/', project_views.logoutPage, name='logout'),
    path('signup/', project_views.signupPage, name='signup'),
    path('profile/', project_views.viewProfile, name='viewprofile'),
    path('profile/add/', project_views.addProfile, name='addprofile'),
    path('profile/edit/', project_views.editProfile, name='editprofile'),

    path('admin/', admin.site.urls),
    path('', project_views.home, name="home"),
    path('edit/<int:pk>', project_views.editTask, name="edit"),
    path('delete/<int:pk>', project_views.deleteTask, name="delete"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)