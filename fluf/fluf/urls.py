from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("api/", include("core.urls")),
]

if settings.DEBUG:
    from drf_yasg import openapi
    from drf_yasg.views import get_schema_view as swagger_get_schema_view

    schema_view = swagger_get_schema_view(
        openapi.Info(
            title="Fluf API",
            default_version="1.0.0",
            description="Documetação da API do Fluf (^-^)",
        ),
        public=True,
    )

    debug_urls = [
        path("admin/", admin.site.urls),
        path(
            "swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "redoc/",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc",
        ),
    ]
    urlpatterns.extend(debug_urls)
