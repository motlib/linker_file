'''Views for the `loc` app'''

from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.http import Http404
from django.contrib.auth.decorators import login_required


from lf_project import versioninfo


def index(request):
    return render(request, 'lf/index.html')


def search(request):
    '''View for search results.'''

    raise Http404()


def info(request):
    '''View to show application info.'''

    context = {
        'info': versioninfo,
    }

    return render(request, 'lf/info.html', context)
