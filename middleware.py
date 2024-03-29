from django.http import QueryDict


class HttpXMethodOverride:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'HTTP_X_METHOD_OVERRIDE' in request.META.keys():
            http_method = request.META['HTTP_X_METHOD_OVERRIDE']
            if http_method.lower() == 'put':
                request.method = 'PUT'
                request.META['REQUEST_METHOD'] = 'PUT'
                request.PUT = QueryDict(request.body)
            if http_method.lower() == 'patch':
                request.method = 'PATCH'
                request.META['REQUEST_METHOD'] = 'PATCH'
                request.PATCH = QueryDict(request.body)
            if http_method.lower() == 'delete':
                request.method = 'DELETE'
                request.META['REQUEST_METHOD'] = 'DELETE'
                request.DELETE = QueryDict(request.body)
        response = self.get_response(request)
        return response
