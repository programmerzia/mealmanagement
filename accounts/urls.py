from django.urls import path
from django.contrib.auth import views as auth_view
from . import views as user_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', user_view.home, name="home"),
	path('accounts/login/', auth_view.LoginView.as_view(template_name='accounts/login.html'), name="login"),
	path('accounts/profile/', user_view.profile, name="profile"),
	path('accounts/login/', auth_view.LogoutView.as_view(template_name='accounts/login.html'), name="logout"),
	path('accounts/register/', user_view.register, name="accounts/register.html"),
	path('accounts/password_change/', auth_view.PasswordChangeView.as_view(template_name='accounts/password_change.html'), name="password_change"),
	path('accounts/password_change/done/', auth_view.PasswordChangeView.as_view(template_name='accounts/password_change_done.html'), name="password_change_done"),
]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)