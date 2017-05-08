from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from somfy_controller.forms import LoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('somfy_controller.urls')),
    url(r'^login/$', auth_views.login,
        {'template_name': 'login.html',
         'authentication_form': LoginForm}),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login/'}),
]
