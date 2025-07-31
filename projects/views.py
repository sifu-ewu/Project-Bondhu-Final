from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.http import Http404
from .models import Post, Comment, Contact, Appointment, Prescription
from .forms import PostForm, CommentForm


class HomeView(ListView):
    model = Post
    template_name = 'innerPro/home.html'
    ordering = ['-post_date']
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        return context


class articleview(DetailView):
    model = Post
    template_name = 'innerPro/article_details.html'


class AddPostview(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'innerPro/add_postpage.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AddCommentview(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'innerPro/add_comments.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.kwargs['pk']})


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'innerPro/updatePost.html'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise Http404("You are not allowed to edit this post")
        return super(UpdatePostView, self).dispatch(request, *args, **kwargs)


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'innerPro/delete_post.html'
    success_url = reverse_lazy('homeview')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise Http404("You are not allowed to delete this post")
        return super(DeletePostView, self).dispatch(request, *args, **kwargs)


class AddCategoryview(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'innerPro/add_CategoryPage.html'
    fields = ['category']


class AddContactview(CreateView):
    model = Contact
    template_name = 'innerPro/contact.html'
    fields = '__all__'

    def form_valid(self, form):
        messages.success(self.request, 'Your message has been sent successfully!')
        return super().form_valid(form)


class AddAppointmentview(LoginRequiredMixin, CreateView):
    model = Appointment
    template_name = 'innerPro/appointment.html'
    fields = ['name', 'email', 'phonenumber', 'doc_name']

    def form_valid(self, form):
        messages.success(self.request, 'Your appointment has been booked successfully!')
        return super().form_valid(form)


class AddPrescriptionview(LoginRequiredMixin, CreateView):
    model = Prescription
    template_name = 'innerPro/prescription.html'
    fields = ['Patient_name', 'patient_age', 'medicine', 'doc_name', 'patient_disease', 'advice']

    def form_valid(self, form):
        messages.success(self.request, 'Prescription has been created successfully!')
        return super().form_valid(form)


def all_appointment(request):
    """View to display all appointments"""
    appointments = Appointment.objects.all().order_by('-date_added')
    context = {
        'appointment_list': appointments
    }
    return render(request, 'innerPro/printappointment.html', context)


def payment_appointment(request):
    """Payment page for appointments"""
    return render(request, 'innerPro/paymentDemo.html')


def PrescriptionShow(request):
    """View to display prescriptions"""
    prescriptions = Prescription.objects.all().order_by('-date_added')
    context = {
        'showprescription_list': prescriptions
    }
    return render(request, 'innerPro/showPrescription.html', context)


def CategoryView(request, cats):
    """View posts by category"""
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    context = {
        'cats': cats.title().replace('-', ' '),
        'category_posts': category_posts
    }
    return render(request, 'innerPro/categories.html', context)
