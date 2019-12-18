from django.conf.urls import url

from products.views import (
        ProductListView,  
        ProductDetailSlugView,
        ProductFeaturedListView,
        )

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^$', ProductFeaturedListView.as_view(), name='featured'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
]

