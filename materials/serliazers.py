from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import validate_allowed_words
from users.models import Subscription
from users.serliazers import SubscriptionSerializer


class LessonSerializer(serializers.ModelSerializer):
    video = serializers.CharField(validators=[validate_allowed_words]) # Валидация на сторонние ресурсы

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseRetrieveSerializer(serializers.ModelSerializer):
    lessons_list = LessonSerializer(source='lesson_set', many=True, read_only=True)
    # lessons_list = serializers.SerializerMethodField()
    lessons_count = serializers.SerializerMethodField()
    subscription = serializers.SerializerMethodField()

    # subscription_list = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_subscription(self, instance):
        user = self.context['request'].user
        return Subscription.objects.filter(user=user).filter(course=instance).exists()

    def get_lessons_count(self, instance):
        """ Подсчет кол-ва уроков в курсе """
        return instance.lesson_set.count()

    # def get_subscription_list(self, instance):
    #     """ Вывод подписок в дополнительное поле """
    #     subscription_list = instance.subscourse.all()  # subscourse вместо course_set так как прописано related_name
    #     if subscription_list:
    #         return SubscriptionSerializer(subscription_list, many=True).data
    #     return 0

    # def get_lessons_list(self, instance):
    #     """ Метод получения списка названия уроков курса """
    #     lessons_list = instance.lesson_set.all()
    #     if lessons_list:
    #         return [a.lesson_name for a in lessons_list]
    #     return 0

    # def get_lessons_list(self, instance):
    #     """ Метод получения списка уроков курса """
    #     lessons_list = instance.lesson_set.all()
    #     if lessons_list:
    #         return LessonSerializer(lessons_list, many=True).data
    #     return 0
