"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('core/', include('core.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import authentication, permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="API description",
        terms_of_service="https://mine/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(authentication.BasicAuthentication,),
)

# from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
# doc_urlpatterns = [
#     # YOUR PATTERNS
#     path('doc', SpectacularAPIView.as_view(), name='schema'),
#     # Optional UI:
#     path('doc/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
#     path('doc/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
# ]

doc_urlpatterns = [
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("apps.authentication.urls")),
    path("api/", include("apps.attendance.urls")),
    path("api/", include("apps.service.urls")),
] + doc_urlpatterns
