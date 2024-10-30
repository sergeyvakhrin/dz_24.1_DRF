from rest_framework import serializers

from materials.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_list = LessonSerializer(source='lesson_set', many=True)
    # lessons_list = serializers.SerializerMethodField()
    lessons_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    # def get_lessons_list(self, instance):
    #     """ Метод получания списка названия уроков курса """
    #     lessons_list = instance.lesson_set.all()
    #     if lessons_list:
    #         return [a.lesson_name for a in lessons_list]
    #     return 0

    # def get_lessons_list(self, instance):
    #     """ Метод получания списка уроков курса """
    #     lessons_list = instance.lesson_set.all()
    #     if lessons_list:
    #         return LessonSerializer(lessons_list, many=True).data
    #     return 0

    def get_lessons_count(self, instance):
        """ Подсчет кол-ва уроков в курсе """
        return instance.lesson_set.count()



