from users.models import Subscription


def get_subs_changes(course):
    """ Получаем подписки в которых изменилось содержание курса """
    subscription = Subscription.objects.filter(course=course)
    email_list = []
    for subs in subscription:
        email_list.append(subs.user.email)
    return email_list
