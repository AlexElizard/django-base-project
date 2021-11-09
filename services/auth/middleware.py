class RemoteAddressMiddleware:
    """Добавляет ip-пользователя в REMOTE_ADDR"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if "HTTP_X_REAL_IP" in request.META:
            request.META["REMOTE_ADDR"] = request.META["HTTP_X_REAL_IP"]
        elif "HTTP_X_FORWARDED_FOR" in request.META:
            request.META["REMOTE_ADDR"] = request.META["HTTP_X_FORWARDED_FOR"].split(',')[0]
        return self.get_response(request)
