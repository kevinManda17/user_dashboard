from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import Profile, Group
from .forms import RegisterForm, ProfileForm,  GroupForm


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_count'] = User.objects.count()
        context['recent_users'] = User.objects.order_by('-date_joined')[:5]
        return context

class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user, full_name=user.username)
        login(self.request, user)
        return redirect(self.success_url)

class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'accounts/profile_list.html'
    context_object_name = 'profiles'

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile_detail.html'

class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile_form.html'
    success_url = reverse_lazy('profile_list')

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile_form.html'
    success_url = reverse_lazy('profile_list')

class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'accounts/profile_confirm_delete.html'
    success_url = reverse_lazy('profile_list')


class GroupListView(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'accounts/group_list.html'
    context_object_name = 'groups'

class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'accounts/group_form.html'
    success_url = reverse_lazy('group_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class GroupDetailView(LoginRequiredMixin, DetailView):
    model = Group
    template_name = 'accounts/group_detail.html'
    context_object_name = 'group'
