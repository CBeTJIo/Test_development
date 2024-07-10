import pytest
import requests


class TestCreateFolderYandex:
    def setup_method(self):
        self.headers = {
            'Authorization': 'OAuth ТОКЕН' # вставить токен яндекса вместо ТОКЕН
        }

    def test_create_folder(self):
        params = {
            'path': 'Photo'
        }
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params=params,
                                headers=self.headers)

        assert response.status_code == 201

    def test_delete_folder(self):
        params = {
            'path': 'Image'
        }
        response = requests.delete('https://cloud-api.yandex.net/v1/disk/resources',
                                params=params,
                                headers=self.headers)

        assert response.status_code == 204

    def test_create_two_folder(self):
        params = {
            'path': 'Image'
        }
        requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params=params,
                                headers=self.headers)
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params=params,
                                headers=self.headers)

        assert response.status_code == 409