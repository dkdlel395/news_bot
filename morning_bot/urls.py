from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('checks/', include('checks.urls')),
    path('rest-auth/', include('rest_auth.urls')), # 로그인, 로그아웃 토큰 생성 path 생성시 migrate 진행
    path('rest-auth/signup/', include('rest_auth.registration.urls')), # 회원가입
]