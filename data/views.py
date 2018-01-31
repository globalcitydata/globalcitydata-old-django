from django.shortcuts import render, get_object_or_404
from .models import DataSet
from .forms import DataSetForm
from .filters import DataSetFilter

def dataset_detail(request, slug):
    dataset = get_object_or_404(DataSet, slug=slug)
    return render(request=request, template_name='data/dataset/detail.html', context={'dataset': dataset})

def dataset_list(request):
    datasets = DataSet.objects.all()
    if request.method == 'POST':
        # Form was submitted
        form = DataSetForm(request.POST)
        if form.is_valid():
            dataset_filter = DataSetFilter(cd = form.cleaned_data)
            datasets = dataset_filter.getDatasets()
    else:
        form = DataSetForm()
    return render(request=request, template_name='data/dataset/list.html', context={'datasets': datasets,
                                                                                    'form': form})
