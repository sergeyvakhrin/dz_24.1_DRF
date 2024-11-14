from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from materials.models import Course, Lesson
from materials.paginations import CustomPagination
from materials.serliazers import CourseSerializer, LessonSerializer, CourseRetrieveSerializer
from materials.services import get_subs_changes
from users.permissions import IsModer, IsOwner

from materials.tasks import send_change_subs


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CustomPagination

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CourseRetrieveSerializer
        return CourseSerializer

    def perform_create(self, serializer):
        """ Присваиваем создателя owner """
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        """ Проверяем, есть ли права у пользователя на действия """
        if self.action == "create":
            self.permission_classes = (~IsModer, )
        elif self.action in ['update', 'retrieve']:
            self.permission_classes = (IsModer | IsOwner, )
        elif self.action == "destroy":
            self.permission_classes = (~IsModer | IsOwner, )
        return super().get_permissions()


class CourseUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = (AllowAny, )

    def get_queryset(self):
        """ Получаем список подписчиков курса """
        # Получаем курс в котором произошли изменения
        course_id = self.kwargs.get('pk')
        course = Course.objects.get(pk=course_id)
        # Получаем подписки в которых изменилось содержание курса
        email_list = get_subs_changes(course)
        # Отдаем в рассылку асинхронно через celery
        send_change_subs.delay(course.course_name, email_list)
        return super().get_queryset()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = (~IsModer, IsAuthenticated)

    def perform_create(self, serializer):
        """ Присваиваем создателя owner """
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = CustomPagination


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsModer | IsOwner, )


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsModer | IsOwner, )


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = (IsAuthenticated, IsOwner | ~IsModer)
