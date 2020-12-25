"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view, openapi

from first import settings

from rest_framework import permissions

schema_view = get_schema_view(

    #     .Info(
    #     title="Snippets API",
    #     default_version='v1',
    #     description="Test description",
    #     terms_of_service="https://www.google.com/policies/terms/",
    #     contact=openapi.Contact(email="contact@snippets.local"),
    #     license=openapi.License(name="BSD License"),
    # ),
    title="تشریح API",
    description='برای ارائه می باشد',
    public=True,
    permission_classes=(permissions.AllowAny,),
    version='1.0.0',
    url='',
    urlconf='api.urls',
)


urlpatterns = [
    path('', include('api.urls'), name='apies'),
    path('admin/', admin.site.urls),
    path('apenapi/', schema_view, name='api_schema'),
    path('docs/', TemplateView.as_view(template_name='documentation.html',
                                       extra_context={'schema_url': 'api_schema'}), name='swagger-ui')
]
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
