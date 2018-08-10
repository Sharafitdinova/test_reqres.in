from .get import SingleGet, ListGet


class TestSingleResource(SingleGet):
    """
    Тесты
        Single resource
    """
    url = 'resource/'


class TestListResource(ListGet):
    """
    Тесты
        List resource
    """
    url = 'resource'
