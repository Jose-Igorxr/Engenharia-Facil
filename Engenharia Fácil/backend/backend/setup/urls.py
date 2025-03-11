from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from coreapp import views
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('coreapp.api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', views.login_view, name='login_view'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout_view'),
    re_path(r'^.*$', lambda request: redirect('/login', permanent=False)),
]