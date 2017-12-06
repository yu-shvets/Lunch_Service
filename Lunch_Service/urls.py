"""Lunch_Service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib.auth.views import login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import RedirectView, TemplateView
from django.contrib.auth import views as auth_views
from lunch_app.regbackend import MyRegistrationView
from lunch_app.views import OrderListView, OrderUpdateView

urlpatterns = [

    # User Related urls
    url(r'^users/login/$', login, {'authentication_form': AuthenticationForm}, name='login'),
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'home'},
        name='auth_logout'),
    url(r'^users/profile/$', TemplateView.as_view(
        template_name='registration/profile.html'), name='profile'),
    url(r'^users/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='home'),
        name='registration_complete'),
    url(r'^users/', include('registration.backends.simple.urls',
        namespace='users')),

    url(r'^$', OrderListView.as_view(), name='home'),
    url(r'^update/(?P<pk>\d+)/$', OrderUpdateView.as_view(), name='update'),

    url(r'^admin/', admin.site.urls),
]
