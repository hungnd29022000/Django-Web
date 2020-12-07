"""django_ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from ecom import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contact/', views.contact, name= 'contact'),
    url(r'^laptop/', views.laptop, name= 'laptop'),
    url(r'^$', views.laptop, name='index'),
    url(r'^product/(?P<product_id>[0-9]+)/$', views.product, name='product'),
    url(r'^brand/(?P<brand_id>[0-9]+)/$', views.filter, name='brand'),
    url(r'^price/(?P<price_id_1>[0-9]+)/(?P<price_id_2>[0-9]+)$', views.filter, name='price'),
    url(r'^ram/(?P<ram_id>[0-9]+)/$', views.filter, name='ram'),
    url(r'^ssd/(?P<ssd_id>[0-9]+)/$', views.filter, name='ssd'),
    url(r'^cpu/(?P<cpu_id>[0-9]+)/$', views.filter, name='cpu'),
    url(r'^search/',views.search,name = 'search'),
    url(r'^filter/',views.filter,name = 'filter'),
    url(r'^cart/',views.cart,name = 'cart'),
    url(r'^update/(?P<cart_id_1>[0-9]+)/(?P<choose_id>[0-9]+)/$',views.update,name = 'update'),
    url(r'^add/(?P<add_id>[0-9]+)/$',views.add,name = 'add'),
    url(r'^voucher/',views.voucher,name = 'voucher'),
    url(r'^buy/',views.buy,name = 'buy'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
