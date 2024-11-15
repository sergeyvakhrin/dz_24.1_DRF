from users.models import Subscription


def get_subs_changes(course):
    """ Получаем список подписчиков, в подписках которых изменилось содержание Курса """
    return get_set(course)


def get_lesson_changes(lesson):
    """ Получаем список подписчиков, в подписках которых изменилось содержание Урока """
    course = lesson.course
    return get_set(course)


def get_set(data):
    """ Получаем список адресов для рассылки """
    subscription = Subscription.objects.filter(course=data)
    email_list = []
    for subs in subscription:
        email_list.append(subs.user.email)
    return email_list



