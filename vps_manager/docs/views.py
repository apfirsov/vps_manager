"""
Provides API dynamic documentation, Swagger and Redoc."
"""
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


project_info = {
    'title': "VPS manager",
    'default_version': 'v1',
    'description': "Документация для приложения",
    'contact': openapi.Contact(url="https://github.com/apfirsov"),
    'license': openapi.License(name="MIT License"),
}

schema_view = get_schema_view(
   openapi.Info(**project_info),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
