from django.contrib.auth.views import LoginView as AuthLoginView


class LoginView(AuthLoginView):
    template_name = 'accounts/login.html'


login = LoginView.as_view()
