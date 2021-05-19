from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView
from django.core.cache import cache
from rest_framework import generics

from urlshort_api.models import UrlShort
from urlshort_api.serializer import UrlShortCreateSerializer
from urlshort_api.serializer import UrlShortSerializer
from urlshort_api.pagination import UrlShortListPagination


class UrlDetail(generics.RetrieveAPIView):
    queryset = UrlShort.objects.all()
    serializer_class = UrlShortSerializer
    lookup_field = 'hash'


class UrlShortList(generics.ListAPIView):
    queryset = UrlShort.objects.all().order_by('-created_at')
    serializer_class = UrlShortSerializer
    pagination_class = UrlShortListPagination

    def get_queryset(self):
        queryset = self.queryset
        session_key = self.request.session.session_key or self.request.COOKIES.get('sessionid')
        return queryset.filter(user_session_key=session_key)


class UrlShortCreate(generics.CreateAPIView):
    serializer_class = UrlShortCreateSerializer

    def get_serializer_context(self):
        if not self.request.session.session_key:
            self.request.session.save()
        return {
            'session_key': self.request.session.session_key
        }


class UrlShortDelete(generics.DestroyAPIView):
    queryset = UrlShort.objects.all()
    serializer_class = UrlShortSerializer
    lookup_field = 'hash'

    def get_object(self):
        # Если сессия указанная в UrlShort принадлежит пользователю, то можно удалить
        session_key = self.request.session.session_key
        url_hash = self.kwargs['hash']
        return get_object_or_404(UrlShort, hash=url_hash, user_session_key=session_key)


class UrlShortRedirect(RedirectView):
    permanent = True

    def get_redirect_url(self, **kwargs):
        cached_url = cache.get(kwargs['hash'])
        if not cached_url:
            url_object = get_object_or_404(UrlShort, hash=kwargs['hash'])
            cache.set(url_object.hash, url_object.full_url, timeout=(60 * 60) * 24)
            return url_object.full_url
        else:
            return cached_url
