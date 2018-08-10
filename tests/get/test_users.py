from .get import SingleGet, ListGet


class TestSingleUser(SingleGet):
    """
    Тесты
        Single user
    """
    url = 'users/'


class TestListUser(ListGet):
    """
    Тесты
        List user
    """
    url = 'users'
