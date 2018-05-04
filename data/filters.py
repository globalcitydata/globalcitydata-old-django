from .models import DataSet, Scale, Parameter, Outcome, Time, FuturesModeling
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


class DataFilter():
    def __init__(self, cd):
        self.cd = cd

    def search(self):
        self.type = None
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
        scales = self.filter('scales', scales_q)
        params_q = Parameter.objects.all().filter(title__icontains=query)
        params = self.filter('params', params_q)
        outcomes_q = Outcome.objects.all().filter(title__icontains=query)
        outcomes = self.filter('outcomes', outcomes_q)
        time_q = Time.objects.all().filter(title__icontains=query)
        time = self.filter('time', time_q)
        futures_modeling_q = FuturesModeling.objects.all().filter(title__icontains=query)
        futures_modeling = self.filter('futures', futures_modeling_q)

        # return union of all datasets and models
        return set.union(data_search, scales, params, outcomes, time, futures_modeling)

    def getData(self):
        # Get scales
        self.type = self.cd['type']
        scales_q = self.cd['spatial_scales']
        scales = self.filter('scales', scales_q)
        # Get parameters
        params_q = self.cd['parameters']
        params = self.filter('params', params_q)
        # Get outcomes
        outcomes_q = self.cd['outcomes']
        outcomes = self.filter('outcomes', outcomes_q)
        # Get time
        time_q = self.cd['temporal_scales']
        time = self.filter('time', time_q)
        # Get futures modeling
        futures_modeling_q = self.cd['futures_modeling']
        futures_modeling = self.filter('futures', futures_modeling_q)
        # Intersect datasets
        data = set.union(scales, params, outcomes, time, futures_modeling)
        if not data:
            if self.type:
                data = DataSet.published.filter(type__title=self.type)
            else:
                data = DataSet.published.all()
        return data

    def filter(self, type, type_q):
        data = set()
        if type_q:
            if type == 'scales':
                if self.type:
                    data = set(DataSet.published.filter(type__title=self.type).filter(scales__in=type_q))
                else:
                    data = set(DataSet.published.filter(scales__in=type_q))
            elif type == 'params':
                if self.type:
                    data = set(DataSet.published.filter(type__title=self.type).filter(parameters__in=type_q))
                else:
                    data = set(DataSet.published.filter(parameters__in=type_q))
            elif type == 'outcomes':
                if self.type:
                    data = set(DataSet.published.filter(type__title=self.type).filter(outcomes__in=type_q))
                else:
                    data = set(DataSet.published.filter(outcomes__in=type_q))
            elif type == 'time':
                if self.type:
                    data = set(DataSet.published.filter(type__title=self.type).filter(time__in=type_q))
                else:
                    data = set(DataSet.published.filter(time__in=type_q))
            elif type == 'futures':
                if self.type:
                    data = set(DataSet.published.filter(type__title=self.type).filter(futures_modeling__in=type_q))
                else:
                    data = set(DataSet.published.filter(futures_modeling__in=type_q))
        return data
