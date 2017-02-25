from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^login$',views.login),
    url(r'^register$',views.register),
    url(r'^about$',views.about),
    url(r'^username$',views.username),
    url(r'^dologin$',views.dologin),
    url(r'^logout$',views.logout),
    url(r'^test$',views.test)
]