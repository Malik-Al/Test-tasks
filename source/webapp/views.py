from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView, UpdateView
from main.settings import HOST_NAME
from webapp.models import Profile, Token
from .forms import UserCreationForm, PasswordChangeForm


class UserIndexView(ListView):
    template_name = 'index.html'
    model = User
    context_object_name = 'user_obj'


class UserSuperView(ListView):
    template_name = 'superuser.html'
    context_object_name = 'user_obj'

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user_1 = User(
                email=form.cleaned_data['email'],
                is_active=False)
            user = form.save()
            token = Token.objects.create(user=user)
            user.save()
            Profile.objects.create(user=user)
            activation_url = HOST_NAME + reverse('user_activate') + '?token={}'.format(token)

            user_1.email_user('Регистрация на сайте localhost',
                              'Для активаций перейдите по ссылке:{}'.format(activation_url))
            login(request, user)
            user.save()
            Profile.objects.create(user=user)
            Profile.objects.all.create(user=user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', context={'form': form})





def user_activate(request):
    token_value = request.GET.get('token')
    try:
        token = Token.objects.get(token=token_value)
        user = token.user
        user.is_active = True
        user.save()
        token.delete()
        login(request, user)
        return redirect('index')
    except Token.DoesNotExist:
        return redirect('index')



class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'


class UserPasswordChangeView(UpdateView):
    model = User
    template_name = 'user_password_change.html'
    form_class = PasswordChangeForm
    context_object_name = 'user_obj'

    def get_success_url(self):
        return reverse('login')



