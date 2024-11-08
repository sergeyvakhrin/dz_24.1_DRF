from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from materials.models import Course, Lesson
from users.models import User


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
            'course': self.course,
            'owner': self.user
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
