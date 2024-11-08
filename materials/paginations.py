from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    """ Класс для контроля вывода кол-ва результатов на страницу """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
