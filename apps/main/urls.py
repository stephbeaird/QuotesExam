from django.conf.urls import url, include # Notice we added include
from .import views

urlpatterns = [
      url(r'^$', views.index),
      url(r'register$', views.register),
      url(r'quotes$', views.quotes),
      url(r'main$', views.main),
      url(r'users$', views.users),
      url(r'logout$', views.logout),
      url(r'login$', views.login),
      url(r'dashboard$', views.dashboard),
      url(r'contribute$', views.contribute),
]