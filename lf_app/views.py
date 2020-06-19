'''Views for the `loc` app'''

from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Link
from .forms import LinkForm

from lf_project import versioninfo


def index(request):
    return render(request, 'lf_app/index.html')


def search(request):
    '''View for search results.'''

    raise Http404()


def info(request):
    '''View to show application info.'''

    context = {
        'info': versioninfo,
    }

    return render(request, 'lf_app/info.html', context)


# run this view in a transaction to be sure to count followed links correctly
@transaction.atomic
def link_open(request, pk):
    link = get_object_or_404(Link, pk=pk)

    link.follow_count += 1
    link.save()

    return redirect(link.url)


class LinkIndexView(ListView):
    '''Index list of top-level plans'''

    # order links by create date
    queryset = Link.objects.order_by('-created_on')
    context_object_name = 'links'
    paginate_by = 10


class LinkDetailView(DetailView):
    model = Link
    context_object_name = 'link'


class LinkCreateView(CreateView):
    model = Link
    form_class = LinkForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()

        # for saving the tags
        form.save_m2m()

        return redirect(self.get_success_url())



class LinkUpdateView(UpdateView):
    model = Link
    form_class = LinkForm


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        # for saving the tags
        form.save_m2m()

        return redirect(self.get_success_url())


class LinkDeleteView(DeleteView):
    model = Link
    success_url = reverse_lazy('index')
