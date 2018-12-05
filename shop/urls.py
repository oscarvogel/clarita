"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from shop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^cart/', include(('apps.cart.urls', 'cart'), namespace='cart'), name='cart'),
    url(r'^cuenta/', include(('apps.account.urls', 'cuenta')), name='cuenta'),
    url(r'^accounts/', include('django.contrib.auth.urls'), name='accounts'),
    path('orders/', include('apps.orders.urls', namespace='orders')),
    url(r'^', include(('apps.ecommerce.urls','shop'), namespace='shop'), name='shop'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
