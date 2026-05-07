from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from employees import views as emp_views

urlpatterns = [
    path('', lambda request: redirect('/login/'), name='home'),
    path('admin/', admin.site.urls),
    path('login/', emp_views.login_view, name='login'),
    path('logout/', emp_views.logout_view, name='logout'),
    path('employees/', include('employees.urls')),
]