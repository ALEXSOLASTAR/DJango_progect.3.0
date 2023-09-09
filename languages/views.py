from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from languages.form import HtmlForm, LanguagesForm
from languages.models import program_language

__all__ = (
    'home', 'LanguagesDetailVaiew', 'LanguagesCreateView', 'LanguagesUpdateView', 'LanguagesDeleteView'
    , 'LanguagesListView',
)


def home(request, pk=None):
    if request.method == 'POST':
        form = LanguagesForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()

    form = LanguagesForm()
    qt = program_language.objects.all()
    lst = Paginator(qt, 2)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {"page_obj": page_obj, "form": form}
    return render(request, 'languages/home.html', context)


class LanguagesDetailVaiew(DetailView):
    queryset = program_language.objects.all()
    template_name = 'languages/detail.html'


class LanguagesCreateView(SuccessMessageMixin, CreateView):
    model = program_language
    form_class = LanguagesForm
    template_name = 'languages/create.html'
    success_url = reverse_lazy('languages:home')
    success_message = "Мову успішно додано"


class LanguagesUpdateView(SuccessMessageMixin, UpdateView):
    model = program_language
    form_class = LanguagesForm
    template_name = 'languages/update.html'
    success_url = reverse_lazy('languages:home')
    success_message = "Мову успішно виправлено"


class LanguagesDeleteView(SuccessMessageMixin, DeleteView):
    model = program_language
    #template_name = 'languages/delete.html'
    success_url = reverse_lazy('languages:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, "Мову успішно ВИДАЛЕНО")
        return self.post(request, *args, **kwargs)


class LanguagesListView(ListView):
    paginate_by = 2
    model = program_language
    template_name = 'languages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = LanguagesForm()
        context['form'] = form
        return context

