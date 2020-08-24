from django.contrib.auth.models import User
from django.views.generic import ListView


class UserIndexView(ListView):
    template_name = 'index.html'
    model = User
    context_object_name = 'user_obj'


