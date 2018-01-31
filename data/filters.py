from .models import DataSet, Scale, Parameter, Outcome

class DataSetFilter():
    def __init__(self, cd):
        self.cd = cd

    def getDatasets(self):
        scales_q = self.cd['scales']
        print(scales_q)
        if not scales_q:
            scales_q = Scale.objects.all()
        scales = set(DataSet.objects.all().filter(scales__in=scales_q))
        print(scales)

        parameters_q = self.cd['parameters']
        if not parameters_q:
            parameters_q = Parameter.objects.all()
        parameters = set(DataSet.objects.all().filter(parameters__in=parameters_q))
        print(parameters)

        outcomes_q = self.cd['outcomes']
        if not outcomes_q:
            outcomes_q = Outcome.objects.all()
        outcomes = set(DataSet.objects.all().filter(outcomes__in=outcomes_q))
        print(outcomes)

        datasets = set.intersection(scales, parameters, outcomes)
        print(datasets)
        return datasets
