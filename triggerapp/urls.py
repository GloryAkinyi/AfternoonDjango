from django.contrib import admin
from django.urls import path
from triggerapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('contact/',views.contact),
    path('payment/',views.payment),
    path('info/',views.information),
]
