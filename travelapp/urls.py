from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from .forms import UserLoginForm
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexView, name="home"),
    path('accounts/login/',LoginView.as_view(authentication_form=UserLoginForm),name="login_url"),
]

urlpatterns+= staticfiles_urlpatterns()
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)