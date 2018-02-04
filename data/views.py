from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, FormView
from django.http import HttpResponse
from .models import DataSet
from .forms import QueryForm, SearchForm
from .filters import DataSetFilter


def dataset_detail(request, slug):
    dataset = get_object_or_404(DataSet, slug=slug)
    return render(request=request, template_name='data/dataset/detail.html', context={'dataset': dataset})


def dataset_list(request):
    datasets = DataSet.objects.all()
    if request.method == 'POST':
        # Form was submitted
        if 'search' in request.POST:
            queryForm = QueryForm()
            searchForm = SearchForm(request.POST)
            if searchForm.is_valid():
                dataset_filter = DataSetFilter(cd=searchForm.cleaned_data)
                datasets = dataset_filter.search()
        elif 'query' in request.POST:
            queryForm = QueryForm(request.POST)
            searchForm = SearchForm()
            if queryForm.is_valid():
                dataset_filter = DataSetFilter(cd=queryForm.cleaned_data)
                datasets = dataset_filter.getDatasets()
    else:
        queryForm = QueryForm()
        searchForm = SearchForm()
    return render(request=request, template_name='data/dataset/list.html', context={'datasets': datasets,
                                                                                    'queryForm': queryForm,
                                                                                    'searchForm': searchForm})
