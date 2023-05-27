from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Contact
from .forms import ContactForm, CustomUserCreationForm
# Create your views here.


class Contact(LoginRequiredMixin, CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'auth/contact.html'
    success_url = reverse_lazy("/")

    def post(self, request):
        form = ContactForm(request.POST)

        if form.is_valid():
            f = form.save(commit=False)
            f.name = request.user
            f.save()
            print('ok')
            return redirect('/')
        return render(request, 'auth/contact.html', {'form': form})


def my_register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            u.save()
            return redirect("/")
    else:
        form = CustomUserCreationForm()
        context = {
            'form': form
        }
    return render(request, 'auth/register.html', context)
