from rest_framework.serializers import ValidationError

allowed_words = 'youtube.com'


def validate_allowed_words(value):
    """ Проверка на запрещенные слова. Если будет список слов, то нужно циклом проверять """
    if allowed_words not in value.lower():
        raise ValidationError("Нельзя использовать ссылки на сторонние ресурсы")
