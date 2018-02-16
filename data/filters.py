from .models import DataSet, Scale, Parameter, Outcome
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


class DataSetFilter():
    def __init__(self, cd):
        self.cd = cd

    def search(self):
        query = self.cd['query']
        # Perform dataset field search
        dataset_search = set(DataSet.published.annotate(
            search=SearchVector('title', 'description', 'context', 'key_takeaways', 'sample_uses_and_visualization',
                                'technical_details', 'applicable_models', 'relevant_publications', 'contact_details',
                                'owner'
                                )).filter(search=query))
        # Search dataset tags
        scales_q = Scale.objects.all().filter(title__icontains=query)
        scales = self.filterScales(scales_q)
        params_q = Parameter.objects.all().filter(title__icontains=query)
        params = self.filterParams(params_q)
        outcomes_q = Outcome.objects.all().filter(title__icontains=query)
        outcomes = self.filterOutcomes(outcomes_q)
        # Set union of all datasets
        datasets = set.union(dataset_search, scales, params, outcomes)

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
            datasets = DataSet.published.all()
        return datasets

    def filterScales(self, scales_q):
        scales = set()
        if scales_q:
            scales = set(DataSet.published.all().filter(scales__in=scales_q))
        return scales

    def filterParams(self, params_q):
        params = set()
        if params_q:
            params = set(DataSet.published.all().filter(parameters__in=params_q))
        return params

    def filterOutcomes(self, outcomes_q):
        outcomes = set()
        if outcomes_q:
            outcomes = set(DataSet.published.all().filter(outcomes__in=outcomes_q))
        return outcomes
