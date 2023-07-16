from rest_framework.response import Response
from .serializers import *
from rest_framework import viewsets, status
from drf_yasg.utils import swagger_auto_schema


class UserViewSet(viewsets.ModelViewSet):
    swagger_schema = None
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CoordsViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    filterset_fields = ('user__email',)

    def create(self, request, *args, **kwargs):
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': f'Запись №{instance.id} была создана',
                'id': instance.id,
            })
        if status.HTTP_400_BAD_REQUEST:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Параметры запроса некорректны',
                'id': None,
            })
        if status.HTTP_500_INTERNAL_SERVER_ERROR:
            return Response({
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': 'Ошибка подключения к базе данных',
                'id': None,
            })

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        pereval = self.get_object()
        if pereval.status == 'new':
            serializer = PerevalSerializer(pereval, data=request.data, partial=partial)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'state': '1',
                    'message': f'Данные записи успешно изменены {"PATCH" if partial else "PUT"}-запросом'
                })
            else:
                return Response({
                    'state': '0',
                    'message': serializer.errors
                })
        else:
            return Response({
                'state': '0',
                'message': f"Отклонено! Причина: {pereval.get_status_display()}"
            })

    def destroy(self, request, *args, **kwargs):
        pereval = self.get_object()
        if pereval.status == 'new':
            self.perform_destroy(pereval)
            return Response({
                'state': '1',
                'message': f'Запись успешно удалена'
            })
        else:
            return Response({
                'state': '0',
                'message': f"Отклонено! Причина: {pereval.get_status_display()}"
            })
