from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Customer


def dashboard(request):
    return render(request, 'repairs/dashboard.html')


class CustomEmploeeLogin(LoginView):
    template_name = 'repairs/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('dashboard')


class CustomerCreate(CreateView):
    model = Customer
    fields = "__all__"
    context_object_name = 'customer'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CustomerCreate, self).form_valid(form)
