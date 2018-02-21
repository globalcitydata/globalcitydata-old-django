from .models import Data, Scale, Parameter, Outcome
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


class DataFilter():
    def __init__(self, cd, type='all'):
        self.cd = cd
        self.type = type

    def search(self):
        query = self.cd['query']
        # Perform dataset field search
        data_search = set(Data.published.annotate(
            search=SearchVector('title', 'description', 'context', 'key_takeaways', 'sample_uses_and_visualization',
                                'technical_details', 'applicable_models', 'relevant_publications', 'contact_details',
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
        scales = self.filterScales(scales_q, self.type)
        params_q = Parameter.objects.all().filter(title__icontains=query)
        params = self.filterParams(params_q, self.type)
        outcomes_q = Outcome.objects.all().filter(title__icontains=query)
        outcomes = self.filterOutcomes(outcomes_q, self.type)
        # return union of all datasets and models
        return set.union(data_search, scales, params, outcomes)

    def getData(self):
        # Get scales
        scales_q = self.cd['scales']
        scales = self.filterScales(scales_q, self.type)
        # Get parameters
        params_q = self.cd['parameters']
        params = self.filterParams(params_q, self.type)
        # Get outcomes
        outcomes_q = self.cd['outcomes']
        outcomes = self.filterOutcomes(outcomes_q, self.type)

        # Intersect datasets
        data = set.union(scales, params, outcomes)
        if not data:
            data = Data.published.all()
        return data

    def getModels(self):
        # Get scales
        scales_q = self.cd['scales']
        scales = self.filterScales(scales_q, self.type)
        # Get parameters
        params_q = self.cd['parameters']
        params = self.filterParams(params_q, self.type)
        # Get outcomes
        outcomes_q = self.cd['outcomes']
        outcomes = self.filterOutcomes(outcomes_q, self.type)

        # Intersect datasets
        models = set.union(scales, params, outcomes)
        if not models:
            models = Data.datasetModels.all()
        return models

    def getDatasets(self):
        # Get scales
        scales_q = self.cd['scales']
        scales = self.filterScales(scales_q, self.type)
        # Get parameters
        params_q = self.cd['parameters']
        params = self.filterParams(params_q, self.type)
        # Get outcomes
        outcomes_q = self.cd['outcomes']
        outcomes = self.filterOutcomes(outcomes_q, self.type)

        # Intersect datasets
        datasets = set.union(scales, params, outcomes)
        if not datasets:
            datasets = set(Data.datasets.all())
        return datasets

    def filterScales(self, scales_q, type):
        scales = set()
        if scales_q:
            if type == 'model':
                scales = set(Data.datasetModels.filter(scales__in=scales_q))
            elif type == 'dataset':
                scales = set(Data.datasets.filter(scales__in=scales_q))
            else:
                scales = set(Data.published.filter(scales__in=scales_q))
        return scales

    def filterParams(self, params_q, type):
        params = set()
        if params_q:
            if type == 'model':
                params = set(Data.datasetModels.filter(parameters__in=params_q))
            elif type == 'dataset':
                params = set(Data.datasets.filter(parameters__in=params_q))
            else:
                params = set(Data.published.filter(parameters__in=params_q))
        return params

    def filterOutcomes(self, outcomes_q, type):
        outcomes = set()
        if outcomes_q:
            if type == 'model':
                outcomes = set(Data.datasetModels.filter(outcomes__in=outcomes_q))
            elif type == 'dataset':
                outcomes = set(Data.datasets.filter(outcomes__in=outcomes_q))
            else:
                outcomes = set(Data.published.filter(outcomes__in=outcomes_q))
        return outcomes
