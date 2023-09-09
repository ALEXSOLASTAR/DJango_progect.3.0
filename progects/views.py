from django.shortcuts import render

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from progects.forms import ProgectForm
from progects.models import Progect

__all__ = (
    'home', 'ProgectListView',
    'ProgectDetailVaiew', 'ProgectCreateView', 'ProgectUpdateView', 'ProgectDeleteView',

)


def home(request, pk=None):
    qt = Progect.objects.all()
    lst = Paginator(qt, 2)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {"page_obj": page_obj,}
    return render(request, 'progects/home.html', context)


class ProgectListView(ListView):
    paginate_by = 2
    model = Progect
    template_name = 'progects/home.html'

class ProgectDetailVaiew(DetailView):
    queryset = Progect.objects.all()
    template_name = 'progects/detail.html'


class ProgectCreateView(SuccessMessageMixin, CreateView):
    model = Progect
    form_class = ProgectForm
    template_name = 'progects/create.html'
    success_url = reverse_lazy('progects:home')
    success_message = "Мову успішно додано"


class ProgectUpdateView(SuccessMessageMixin, UpdateView):
    model = Progect
    form_class = ProgectForm
    template_name = 'progects/update.html'
    success_url = reverse_lazy('progects:home')
    success_message = "Мову успішно виправлено"


class ProgectDeleteView(SuccessMessageMixin, DeleteView):
    model = Progect
    template_name = 'progects/delete.html'
    success_url = reverse_lazy('progects:home')

    def get(self, request, *args, **kwargs):
        messages.success(request, "Мову успішно ВИДАЛЕНО")
        return self.post(request, *args, **kwargs)




