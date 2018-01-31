from .models import DataSet, Scale, Parameter, Outcome
from django.contrib.postgres.search import SearchVector


class DataSetFilter():
    def __init__(self, cd):
        self.cd = cd

    def search(self):
        datasets = set()
        query = self.cd['query']
        print(query)

        datasets = DataSet.objects.all()
        return datasets

    def getDatasets(self):
        # Get scales
        scales_q = self.cd['scales']
        scales = self.filterScales(scales_q)
        # Get parameters
        params_q = self.cd['parameters']
        params = self.filterParams(params_q)
        # Get outcomes
        outcomes_q = self.cd['outcomes']
        outcomes = self.filterOutcomes(outcomes_q)

        # Intersect datasets
        datasets = set.union(scales, params, outcomes)
        if not datasets:
            datasets = DataSet.objects.all()
        return datasets

    def filterScales(self, scales_q):
        scales = set()
        if scales_q:
            scales = set(DataSet.objects.all().filter(scales__in=scales_q))
        return scales

    def filterParams(self, params_q):
        params = set()
        if params_q:
            params = set(DataSet.objects.all().filter(parameters__in=params_q))
        return params

    def filterOutcomes(self, outcomes_q):
        outcomes = set()
        if outcomes_q:
            outcomes = set(DataSet.objects.all().filter(outcomes__in=outcomes_q))
        return outcomes
