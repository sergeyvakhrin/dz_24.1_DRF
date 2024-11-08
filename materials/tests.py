from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import User, Subscription


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='admin@sky.com')
        self.course = Course.objects.create(course_name='Курс Тест', owner=self.user)
        self.lesson = Lesson.objects.create(lesson_name='Урок Тест', course=self.course, owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('materials:lesson-get', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('lesson_name'), self.lesson.lesson_name)

    def test_lesson_create(self):
        url = reverse('materials:lesson-create')
        data = {
            'lesson_name': 'Тест',
            'video': 'youtube.com'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_lesson_update(self):
        url = reverse('materials:lesson-update', args=(self.lesson.pk,))
        data = {
            'lesson_name': 'Тест 3',
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get('lesson_name'), 'Тест 3')

    def test_lesson_delete(self):
        url = reverse('materials:lesson-delete', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.all().count(), 0)

    def test_lesson_list(self):
        url = reverse('materials:lesson-list')
        response = self.client.get(url)
        data = response.json()
        result = {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {'id': self.lesson.pk,
                 'video': self.lesson.video,
                 'lesson_name': self.lesson.lesson_name,
                 'description': self.lesson.description,
                 'preview': self.lesson.preview,
                 'course': self.course.pk,
                 'owner': self.lesson.owner.pk}]}
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='123@123.ru')
        self.course = Course.objects.create(course_name='test', owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        url = reverse('users:subscription-create')

        data = {
            'course': self.course.pk,
            'user': self.user.pk
        }
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data['message'], 'Подписка создана')
        self.assertEqual(Subscription.objects.all().count(), 1)

        data = {
            'course': self.course.pk,
            'user': self.user.pk
        }
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(data['message'], 'Подписка удалена')
        self.assertEqual(Subscription.objects.all().count(), 0)



