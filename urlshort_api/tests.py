from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from urlshort_api.models import UrlShort


class UrlShortApiTestCase(APITestCase):

    def setUp(self):
        self.test_data = {
            'full_url': 'https://yandex.ru/'
        }

    def test_create_url(self):
        url = reverse('create_url')
        response = self.client.post(url, format='json', data=self.test_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['full_url'], self.test_data['full_url'])
        if 'hash' not in response.data:
            raise Exception('Hash does not exists')
        try:
            check_db_record = UrlShort.objects.get(hash=response.data['hash'])
        except UrlShort.DoesNotExist:
            raise Exception('Record in db does not exists')
        if not check_db_record.user_session_key:
            raise Exception('User session key does not exists')

    def test_create_url_with_custom_hash(self):
        custom_hash = '123ttkk'
        url = reverse('create_url')
        self.test_data['custom_hash'] = custom_hash
        response = self.client.post(url, format='json', data=self.test_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['full_url'], self.test_data['full_url'])

    def test_create_duplicate_custom_hash(self):
        custom_hash = '123ttkk'
        url = reverse('create_url')
        self.test_data['custom_hash'] = custom_hash
        self.client.post(url, format='json', data=self.test_data)
        response = self.client.post(url, format='json', data=self.test_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_detail_user_urls(self):
        created_url_response = self.client.post(reverse('create_url'),
                                                format='json', data=self.test_data)
        url_detail = reverse('detail_url', kwargs=dict(hash=created_url_response.data['hash']))
        get_response = self.client.get(url_detail)
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_response.data['hash'], created_url_response.data['hash'])

    def test_get_user_urls(self):
        created_url_response = self.client.post(reverse('create_url'),
                                                format='json', data=self.test_data)
        get_response = self.client.get(reverse('list_urls'))
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_response.data[0]['hash'], created_url_response.data['hash'])

    def test_delete_user_urls(self):
        created_url_response = self.client.post(reverse('create_url'),
                                                format='json', data=self.test_data)
        delete_url = reverse('delete_url',
                             kwargs=dict(hash=created_url_response.data['hash']))
        delete_response = self.client.delete(delete_url)
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)

    def test_redirect(self):
        created_url_response = self.client.post(reverse('create_url'),
                                                format='json', data=self.test_data)
        redirect_url = reverse('redirect', kwargs=dict(hash=created_url_response.data['hash']))
        redirect_response = self.client.get(redirect_url)
        self.assertEqual(redirect_response.status_code, status.HTTP_301_MOVED_PERMANENTLY)
        self.assertEqual(redirect_response.url, self.test_data['full_url'])
