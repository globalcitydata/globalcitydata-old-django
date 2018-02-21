from .models import DataSet, Type, Scale, Parameter, Outcome
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


class DataFilter():
    def __init__(self, cd):
        self.cd = cd
        self.type = None

    def search(self):
        query = self.cd['query']
        # Perform dataset field search
        data_search = set(DataSet.published.annotate(
            search=SearchVector('title', 'description', 'context', 'key_takeaways', 'sample_uses_and_visualization',
                                'technical_details', 'applicable_models_or_datasets', 'relevant_publications', 'contact_details',
                                'owner'
                                )).filter(search=query))
        # # Perform dataset model field search
        # model_search = set(DataSetModel.published.annotate(
        #     search=SearchVector('title', 'description', 'context', 'key_takeaways', 'sample_uses_and_visualization',
        #                         'technical_details', 'applicable_models', 'relevant_publications', 'contact_details',
        #                         'owner', 'type'
        #                         )).filter(search=query))
        # Search dataset tags
        scales_q = Scale.objects.all().filter(title__icontains=query)
        scales = self.filterScales(scales_q)
        params_q = Parameter.objects.all().filter(title__icontains=query)
        params = self.filterParams(params_q)
        outcomes_q = Outcome.objects.all().filter(title__icontains=query)
        outcomes = self.filterOutcomes(outcomes_q)
        # return union of all datasets and models
        return set.union(data_search, scales, params, outcomes)

    def getData(self):
        # Get scales
        self.type = self.cd['type']
        scales_q = self.cd['scales']
        scales = self.filterScales(scales_q)
        # Get parameters
        params_q = self.cd['parameters']
        params = self.filterParams(params_q)
        # Get outcomes
        outcomes_q = self.cd['outcomes']
        outcomes = self.filterOutcomes(outcomes_q)
        # Intersect datasets
        data = set.union(scales, params, outcomes)
        if not data and self.type is None:
            data = DataSet.published.all()
        return data

    def filterScales(self, scales_q):
        scales = set()
        if scales_q:
            if self.type:
                scales = set(DataSet.published.filter(type__title=self.type).filter(scales__in=scales_q))
            else:
                scales = set(DataSet.published.filter(scales__in=scales_q))
        return scales

    def filterParams(self, params_q):
        params = set()
        if params_q:
            if self.type:
                params = set(DataSet.published.filter(type__title=self.type).filter(parameters__in=params_q))
            else:
                params = set(DataSet.published.filter(parameters__in=params_q))
        return params

    def filterOutcomes(self, outcomes_q):
        outcomes = set()
        if outcomes_q:
            if self.type:
                outcomes = set(DataSet.published.filter(type__title=self.type).filter(outcomes__in=outcomes_q))
            else:
                outcomes = set(DataSet.published.filter(outcomes__in=outcomes_q))
        return outcomes

    # def getModels(self):
    #     # Get scales
    #     scales_q = self.cd['scales']
    #     scales = self.filterScales(scales_q)
    #     # Get parameters
    #     params_q = self.cd['parameters']
    #     params = self.filterParams(params_q)
    #     # Get outcomes
    #     outcomes_q = self.cd['outcomes']
    #     outcomes = self.filterOutcomes(outcomes_q)
    #
    #     # Intersect datasets
    #     models = set.union(scales, params, outcomes)
    #     if not models:
    #         models = DataSet.datasetModels.all()
    #     return models
    #
    # def getDatasets(self):
    #     # Get scales
    #     scales_q = self.cd['scales']
    #     scales = self.filterScales(scales_q)
    #     # Get parameters
    #     params_q = self.cd['parameters']
    #     params = self.filterParams(params_q)
    #     # Get outcomes
    #     outcomes_q = self.cd['outcomes']
    #     outcomes = self.filterOutcomes(outcomes_q)
    #
    #     # Intersect datasets
    #     datasets = set.union(scales, params, outcomes)
    #     if not datasets:
    #         datasets = set(DataSet.datasets.all())
    #     return datasets