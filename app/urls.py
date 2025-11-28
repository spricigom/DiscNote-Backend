from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from core.views import ComentarioViewSet, CurtidaViewSet, ResenhaViewSet, UserViewSet, GoogleLoginAPIView
from uploader.router import router as uploader_router

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = DefaultRouter()
# eita
router.register(r'curtidas', CurtidaViewSet, basename='curtidas')
router.register(r'comentarios', ComentarioViewSet, basename='comentarios')
router.register(r'usuarios', UserViewSet, basename='usuarios')
router.register(r'resenhas', ResenhaViewSet, basename='resenhas')

urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    path(
        "api/media/", include(uploader_router.urls)
        ),  # nova linha
    # API
    path('api/', include(router.urls)),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/auth/google/', GoogleLoginAPIView.as_view(), name='google-login'),
    path("api/auth/", include('social_django.urls', namespace="social")),
]

urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
