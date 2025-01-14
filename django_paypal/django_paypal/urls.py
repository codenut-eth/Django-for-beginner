"""
URL configuration for django_paypal project.

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
from payment import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.courses_list, name='courses_list'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('courses/<int:course_id>/create-order/', views.create_order, name='create_order'),
    path('courses/<int:course_id>/payment-success/', views.payment_success, name='payment_success'),
    path('courses/<int:course_id>/payment-cancel/', views.payment_cancel, name='payment_cancel'),
]
