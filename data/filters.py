from .models import DataSet, DataSetModel, Scale, Parameter, Outcome
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


class DataFilter():
    def __init__(self, cd, type='all'):
        self.cd = cd
        self.type = type

    def search(self):
        query = self.cd['query']
        # Perform dataset field search
        dataset_search = set(DataSet.published.annotate(
            search=SearchVector('title', 'description', 'context', 'key_takeaways', 'sample_uses_and_visualization',
                                'technical_details', 'applicable_models', 'relevant_publications', 'contact_details',
                                'owner'
                                )).filter(search=query))
        # Perform dataset model field search
        model_search = set(DataSetModel.published.annotate(
            search=SearchVector('title', 'description', 'context', 'key_takeaways', 'sample_uses_and_visualization',
                                'technical_details', 'applicable_models', 'relevant_publications', 'contact_details',
                                'owner'
                                )).filter(search=query))
        # Search dataset tags
        scales_q = Scale.objects.all().filter(title__icontains=query)
        scales = self.filterScales(scales_q, self.type)
        print(scales_q)
        print(scales)
        params_q = Parameter.objects.all().filter(title__icontains=query)
        params = self.filterParams(params_q, self.type)
        print(params_q)
        print(params)
        outcomes_q = Outcome.objects.all().filter(title__icontains=query)
        outcomes = self.filterOutcomes(outcomes_q, self.type)
        print(outcomes_q)
        print(outcomes)
        print(dataset_search)
        print(model_search)
        # Set union of all datasets
        datasets = set.union(dataset_search, model_search, scales, params, outcomes)
        print(datasets)

        return datasets

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
            datasets = DataSet.published.all()
        return datasets

    def getModels(self):
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

    def filterScales(self, scales_q, type):
        response = set()
        if scales_q:
            if type == 'model':
                response = set(DataSetModel.published.filter(scales__in=scales_q))
            elif type == 'dataset':
                response = set(DataSet.published.filter(scales__in=scales_q))
            else:
                scales = set(DataSet.published.filter(scales__in=scales_q))
                models = set(DataSetModel.published.filter(scales__in=scales_q))
                response = set.union(scales, models)
        return response

    def filterParams(self, params_q, type):
        response = set()
        if params_q:
            if type == 'model':
                response = set(DataSetModel.published.filter(parameters__in=params_q))
            elif type == 'dataset':
                response = set(DataSet.published.filter(parameters__in=params_q))
            else:
                params = set(DataSet.published.filter(parameters__in=params_q))
                models = set(DataSetModel.published.filter(parameters__in=params_q))
                response = set.union(params, models)
        return response

    def filterOutcomes(self, outcomes_q, type):
        response = set()
        if outcomes_q:
            if type == 'model':
                response = set(DataSetModel.published.filter(outcomes__in=outcomes_q))
            elif type == 'dataset':
                response = set(DataSet.published.filter(outcomes__in=outcomes_q))
            else:
                outcomes = set(DataSet.published.filter(outcomes__in=outcomes_q))
                models = set(DataSetModel.published.filter(outcomes__in=outcomes_q))
                response = set.union(outcomes, models)
        return response
