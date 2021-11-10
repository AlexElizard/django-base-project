from djangorestframework_camel_case.settings import api_settings
from djangorestframework_camel_case.util import underscoreize


class CamelCaseQueryParamsMiddleware:
    """Переводит GET-параметры из camelCase в snake_case"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.GET = underscoreize(request.GET, **api_settings.JSON_UNDERSCOREIZE)
        return self.get_response(request)
