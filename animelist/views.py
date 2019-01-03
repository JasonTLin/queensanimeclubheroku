from django.shortcuts import render
from .animelistretrieval import retrieve
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.


def animelist(request):
    kitsuanime = retrieve()
    page = request.GET.get('page', 1)
    paginator = Paginator(kitsuanime, 5)
    try:
        kitsuanime = paginator.page(page)
    except PageNotAnInteger:
        kitsuanime = paginator.page(1)
    except EmptyPage:
        kitsuanime = paginator.page(paginator.num_pages)
    context = {"kitsuanimelist": kitsuanime}
    return render(request, 'animelist/animelist.html', context)


def search(request):
    query = str(request.GET.get('q')).lower()
    kitsuanime = retrieve()
    results = list()
    for i in kitsuanime:
        if query in i['anime'].lower():
            results.append(i)
    context = {
        'results': results
    }
    return render(request, 'animelist/results.html', context)
