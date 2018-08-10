# test_reqres.in

https://reqres.in/
Для данного REST API необходимо:
 - написать минимально необходимое количество тест-кейсов
 - расставить для них приоритеты для автоматизации
 - разработать автотесты для наиболее приоритетных кейсов


Используемые технологии и фреймворки:
 - py.test (http://doc.pytest.org/en/latest/) - фреймворк для разработки и запуска автотестов
 - yandex.allure (https://github.com/allure-framework/allure-pytest) - для генерации наглядного HTML-отчета
 - тесты должны использовать fixture и параметризацию из py.test
 - по возможности вынести код в отдельные классы и модули
 - в сами тесты добавить возможность пробросить параметры командной строки (например, стенд, на котором запускать тесты: py.test -s -v test_file.py --testing-stand=DEV)
 - если выполняется запрос по http, то в отчете allure нужно прикрепить сам запрос и ответ от сервера (from requests_toolbelt.utils import dump)