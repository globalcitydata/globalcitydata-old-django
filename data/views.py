from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, FormView
from .models import DataSet
from .forms import DataSetForm, SearchForm
from .filters import DataSetFilter

def dataset_detail(request, slug):
    dataset = get_object_or_404(DataSet, slug=slug)
    return render(request=request, template_name='data/dataset/detail.html', context={'dataset': dataset})

def dataset_list(request):
    datasets = DataSet.objects.all()
    if request.method == 'POST':
        # Form was submitted
        form = DataSetForm(request.POST)
        search = SearchForm(request.POST)
        if form.is_valid():
            dataset_filter = DataSetFilter(cd = form.cleaned_data)
            datasets = dataset_filter.getDatasets()
        elif search.is_valid():
            dataset_filter = DataSetFilter(cd=form.cleaned_data)
            datasets = dataset_filter.search()
    else:
        form = DataSetForm()
        search = SearchForm()
    return render(request=request, template_name='data/dataset/list.html', context={'datasets': datasets,
                                                                                    'form': form,
                                                                                    'search': search})

class MainListView(TemplateView):
    template_name = 'data/dataset/list.html'

    def get(self, request, *args, **kwargs):
        form = DataSetForm()
        search = SearchForm()
        datasets = DataSet.objects.all()
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['search'] = search
        context['datasets'] = datasets
        return self.render_to_response(context)


class DataSetFormView(FormView):
    form_class = DataSetForm
    template_name = 'data/dataset/list.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        datasetForm = self.form_class(request.POST)
        searchForm = SearchForm()
        if datasetForm.is_valid():
            datasetFilter = DataSetFilter(cd=datasetForm.cleaned_data)
            return self.render_to_response(
                self.get_context_data(
                    datasets = datasetFilter.getDatasets(),
                    form = datasetForm,
                    search = searchForm
                )
            )
        else:
            return self.render_to_response(
                self.get_context_data(
                    datasets=DataSet.objects.all(),
                    form=datasetForm,
                    search=searchForm
                )
            )

class SearchFormView(FormView):
    form_class = SearchForm
    template_name = 'data/dataset/list.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        datasetForm = DataSetForm()
        searchForm = self.form_class(request.POST)
        if searchForm.is_valid():
            datasetFilter = DataSetFilter(cd=searchForm.cleaned_data)
            return self.render_to_response(
                self.get_context_data(
                    datasets = datasetFilter.getDatasets(),
                    form = datasetForm,
                    search = searchForm
                )
            )
        else:
            return self.render_to_response(
                self.get_context_data(
                    datasets=DataSet.objects.all(),
                    form=datasetForm,
                    search=searchForm
                )
            )