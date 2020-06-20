'''Views for the `loc` app'''

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Q
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import Link
from .forms import LinkForm

from lf_project import versioninfo

from web_meta import find_website_meta

def index(request):
    return render(request, 'lf_app/index.html')


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


class TaggedLinksView(ListView):
    context_object_name = 'links'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['tag'] = self.kwargs['tag']

        return context

    def get_queryset(self):
        qs = Link.objects.filter(tags__name__in=[self.kwargs['tag']]).order_by('-created_on')

        return qs


class LinkDetailView(DetailView):
    '''Show details of a link.'''

    model = Link
    context_object_name = 'link'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        related_links = self.object.tags.similar_objects()

        context['related'] = related_links

        return context


class LinkCreateView(CreateView):
    '''View to create a new link.'''

    model = Link
    form_class = LinkForm

    def get_initial(self):
        '''Set initial data if we get it through the get request.'''

        initial = super().get_initial()

        initial['url'] = self.request.GET.get('url', '')
        initial['title'] = self.request.GET.get('title', '')

        return initial


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()

        # for saving the tags
        form.save_m2m()

        return redirect(self.get_success_url())



class LinkUpdateView(UpdateView):
    '''View to edit a link.'''

    model = Link
    form_class = LinkForm


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        # for saving the tags
        form.save_m2m()

        return redirect(self.get_success_url())


class LinkDeleteView(DeleteView):
    '''Delete a link.'''
    model = Link
    success_url = reverse_lazy('lf:index')


def link_search(request):
    term_str = request.GET.get('term', '')

    terms = term_str.split(' ')

    tags = [term[4:] for term in terms if term.startswith('tag:')]
    words = [term for term in terms if not term.startswith('tag:')]

    qs = Link.objects

    for word in words:
        qs = qs.filter(Q(title__icontains=word) | Q(notes__icontains=word)) \

    for tag in tags:
        qs = qs.filter(tags__name__in=[tag])

    qs.distinct()

    links = qs.order_by('-created_on')

    context = {
        'links': links,
    }

    return render(request, 'lf_app/link_list.html', context)


def tags_list(request):
    tags = Link.tags.order_by('name').all()

    context = {
        'tags': tags,
    }

    return render(request, 'lf_app/tags_list.html', context)


def find_metadata(request):
    url = request.GET.get('url', '')

    if not 'url':
        raise Http404()

    metadata = find_website_meta(url)

    return JsonResponse(metadata)
