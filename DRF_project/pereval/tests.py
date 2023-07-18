from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.utils import json

from pereval.models import Pereval, User, Coords, Level, Images
from pereval.serializers import PerevalSerializer
from .payloads import *


class BaseTestCase(APITestCase):
    def setUp(self):
        self.pereval1 = Pereval.objects.create(
            beauty_title='Название препятствия 1',
            title='Название вершины 1',
            other_titles='Другое название 1',
            connect='',
            user=User.objects.create(
                email='user1@mail.ru',
                fam='Фамилия 1',
                name='Имя 1',
                otc='Отчество 1',
                phone='+111111'
            ),
            coords=Coords.objects.create(
                latitude=11.1,
                longitude=22.22,
                height=333
            ),
            level=Level.objects.create(
                winter='A1',
                summer='1B',
                autumn='C1',
                spring='1D'
            )
        )

        Images.objects.bulk_create([
            Images(pereval=self.pereval1, title='Название 1', data='https://example.com/image1.jpg'),
            Images(pereval=self.pereval1, title='Название 2', data='https://example.com/image2.jpg'),
        ])

        self.pereval2 = Pereval.objects.create(
            beauty_title='Название препятствия 2',
            title='Название вершины 2',
            other_titles='Другое название 2',
            connect='',
            user=User.objects.create(
                email='user2@mail.ru',
                fam='Фамилия 2',
                name='Имя 2',
                otc='Отчество 2',
                phone='+2222222'
            ),
            coords=Coords.objects.create(
                latitude=44.44,
                longitude=55.5,
                height=666
            ),
            level=Level.objects.create(
                winter='',
                summer='2B',
                autumn='C2',
                spring=''
            )
        )

        Images.objects.bulk_create([
            Images(pereval=self.pereval2, title='Название 3', data='https://example.com/image3.jpg'),
            Images(pereval=self.pereval2, title='Название 4', data='https://example.com/image4.jpg'),
        ])

        self.pereval3 = Pereval.objects.create(
            status='pending',
            beauty_title='Название препятствия 3',
            title='Название вершины 3',
            other_titles='Другое название 3',
            connect='',
            user=User.objects.create(
                email='user3@mail.ru',
                fam='Фамилия 3',
                name='Имя 3',
                otc='Отчество 3',
                phone='+333333333'
            ),
            coords=Coords.objects.create(
                latitude=77.0,
                longitude=88.0,
                height=999
            ),
            level=Level.objects.create(
                winter='',
                summer='',
                autumn='',
                spring=''
            )
        )

        Images.objects.bulk_create([
            Images(pereval=self.pereval3, title='Название 5', data='https://example.com/image5.jpg'),
            Images(pereval=self.pereval3, title='Название 6', data='https://example.com/image6.jpg'),
        ])


class GetAllPeravalsTest(BaseTestCase):
    """ Проверка получения списка перевалов """
    def setUp(self):
        super().setUp()

    def test_get_all_perevals(self):
        response = self.client.get(reverse('pereval-list'))
        perevals = Pereval.objects.all()
        serializer = PerevalSerializer(perevals, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSinglePerevalTest(BaseTestCase):
    """ Проверка получения одного перевала """
    def setUp(self):
        super().setUp()

    def test_get_valid_single_pereval(self):
        response = self.client.get(reverse('pereval-detail', kwargs={'pk': self.pereval1.pk}))
        pereval = Pereval.objects.get(pk=self.pereval1.pk)
        serializer = PerevalSerializer(pereval)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_pereval(self):
        response = self.client.get(
            reverse('pereval-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewPerevalTest(APITestCase):
    """ Проверка создания нового перевала """
    def setUp(self):
        self.valid_payload = valid_pereval_test_data
        self.missing_user = missing_user_test_data
        self.missing_coords = missing_coords_test_data
        self.missing_level = missing_level_test_data
        self.missing_images = missing_images_test_data

    def test_create_valid_pereval(self):
        response = self.client.post(
            reverse('pereval-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_missing_user_pereval(self):
        response = self.client.post(
            reverse('pereval-list'),
            data=json.dumps(self.missing_user),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_missing_coords_pereval(self):
        response = self.client.post(
            reverse('pereval-list'),
            data=json.dumps(self.missing_coords),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_missing_level_pereval(self):
        response = self.client.post(
            reverse('pereval-list'),
            data=json.dumps(self.missing_level),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_missing_images_pereval(self):
        response = self.client.post(
            reverse('pereval-list'),
            data=json.dumps(self.missing_images),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class PatchSinglePerevalTest(BaseTestCase):
    """ Проверка PATCH-запроса для перевала """
    def setUp(self):
        super().setUp()

    def test_valid_patch_pereval(self):
        response = self.client.patch(path=reverse('pereval-detail', kwargs={'pk': self.pereval1.pk}),
                                     data=patch_valid_payload,
                                     format='json')
        self.assertEqual(response.data, {'state': 1, 'message': 'Данные записи успешно изменены PATCH-запросом'})

    def test_changed_user_patch_pereval(self):
        response = self.client.patch(path=reverse('pereval-detail', kwargs={'pk': self.pereval1.pk}),
                                     data=patch_changed_user_payload,
                                     format='json')
        pereval = Pereval.objects.get(pk=self.pereval1.pk)
        serializer = PerevalSerializer(instance=pereval,
                                       data=patch_changed_user_payload,
                                       partial=True)
        serializer.is_valid()
        self.assertEqual(response.data, {'state': 0, 'message': serializer.errors})

    def test_invalid_coords_pereval(self):
        response = self.client.patch(path=reverse('pereval-detail', kwargs={'pk': self.pereval1.pk}),
                                     data=patch_invalid_coords_payload,
                                     format='json')
        pereval = Pereval.objects.get(pk=self.pereval1.pk)
        serializer = PerevalSerializer(instance=pereval,
                                       data=patch_invalid_coords_payload,
                                       partial=True)
        serializer.is_valid()
        self.assertEqual(response.data, {'state': 0, 'message': serializer.errors})

    def test_not_new_status_pereval(self):
        response = self.client.patch(path=reverse('pereval-detail', kwargs={'pk': self.pereval3.pk}),
                                     data=patch_not_new_status_payload,
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class PutSinglePerevalTest(BaseTestCase):
    """ Проверка PUT-запроса для перевала """
    def setUp(self):
        super().setUp()

    def test_valid_put_pereval(self):
        response = self.client.put(path=reverse('pereval-detail', kwargs={'pk': self.pereval1.pk}),
                                   data=valid_pereval_test_data,
                                   format='json')
        self.assertEqual(response.data, {'state': 1, 'message': 'Данные записи успешно изменены PUT-запросом'})

    def test_changed_user_put_pereval(self):
        response = self.client.put(path=reverse('pereval-detail', kwargs={'pk': self.pereval1.pk}),
                                   data=put_changed_user_payload,
                                   format='json')
        pereval = Pereval.objects.get(pk=self.pereval1.pk)
        serializer = PerevalSerializer(instance=pereval,
                                       data=put_changed_user_payload,
                                       partial=False)
        serializer.is_valid()
        self.assertEqual(response.data, {'state': 0, 'message': serializer.errors})

    def test_not_new_status_pereval(self):
        response = self.client.put(path=reverse('pereval-detail', kwargs={'pk': self.pereval3.pk}),
                                   data=put_not_new_status_payload,
                                   format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GetPerevalsByEmailTest(BaseTestCase):
    """ Проверка получения списка перевалов при фильтрации по почте """
    def setUp(self):
        super().setUp()

    def test_get_data_by_email(self):
        response = self.client.get("/submitData/", {"user__email": "user2@mail.ru"})
        self.assertEqual(len(response.data), 1)


class DeletePeravalTest(BaseTestCase):
    """ Проверка удаления перевала """
    def setUp(self):
        super().setUp()

    def test_delete_pereval(self):
        response = self.client.delete(path=reverse('pereval-detail', kwargs={'pk': self.pereval2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_not_new_status_pereval(self):
        response = self.client.delete(path=reverse('pereval-detail', kwargs={'pk': self.pereval3.pk}))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
