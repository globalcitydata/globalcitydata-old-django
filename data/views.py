from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, FormView
from django.http import HttpResponse
from .models import DataSet, DataSetModel
from .forms import QueryForm, SearchForm
from .filters import DataFilter


def detailView(request, slug):
    dataset = get_object_or_404(DataSet, slug=slug)
    return render(request=request, template_name='data/dataset/detail.html', context={'dataset': dataset})


def homeView(request):
    if request.method == 'POST':
        # Form was submitted
        if 'search' in request.POST:
            queryForm = QueryForm()
            searchForm = SearchForm(request.POST)
            if searchForm.is_valid():
                data_filter = DataFilter(cd=searchForm.cleaned_data, type='all')
                response_data = data_filter.search()
        elif 'query' in request.POST:
            queryForm = QueryForm(request.POST)
            searchForm = SearchForm()
            if queryForm.is_valid():
                dataset_filter = DataFilter(cd=queryForm.cleaned_data, type='all')
                response_data = dataset_filter.getDatasets()
    else:
        queryForm = QueryForm()
        searchForm = SearchForm()
        datasets = set(DataSet.published.all())
        models = set(DataSetModel.published.all())
        response_data = set.union(datasets, models)
    return render(request=request, template_name='data/dataset/home.html', context={'response_data': response_data,
                                                                                    'queryForm': queryForm,
                                                                                    'searchForm': searchForm})
