from django.shortcuts import redirect


class AdminLoginControl:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_anonymous and request.path == '/main_panel_admin/':
            return redirect('accounts:login')

        if request.user.is_authenticated and request.path == '/accounts/login/':
            return redirect('accounts:dashboard')

        response = self.get_response(request)

        if request.path == '/main_panel_admin/' and request.user.is_authenticated and not request.user.is_superuser:
            return redirect('accounts:dashboard')

        return response
