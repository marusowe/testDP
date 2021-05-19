from django.urls import path

from urlshort_api.views import UrlDetail
from urlshort_api.views import UrlShortList
from urlshort_api.views import UrlShortDelete
from urlshort_api.views import UrlShortCreate
from urlshort_api.views import UrlShortRedirect

urlpatterns = [
    path('urls/all/', UrlShortList.as_view(), name='list_urls'),
    path('urls/<str:hash>/delete/', UrlShortDelete.as_view(), name='delete_url'),
    path('urls/create/', UrlShortCreate.as_view(), name='create_url'),
    path('urls/<str:hash>/', UrlDetail.as_view(), name='detail_url'),
    path('<str:hash>/', UrlShortRedirect.as_view(), name='redirect'),
]