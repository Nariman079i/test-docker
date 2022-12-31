

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from project import settings

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Naric API Documentation",
        default_version='v1',
        description="Naric API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="offer.start@mail.ru"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

doc_urls = [
    path('playground/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('users.urls'))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += doc_urls
