from django.db import models
from django.urls import reverse
from django.utils import timezone


# Filters
class Scale(models.Model):
    SCALE_CHOICES = (
        ('Intra City Data', 'Intra City Data'),
        ('Whole City Data', 'Whole City Data'),
        ('All City Data', 'All City Data'),
    )
    title = models.CharField(max_length=20, choices=SCALE_CHOICES, blank=True, default='', unique=True)

    def __str__(self):
        return self.title

    def get_datasets(self):
        return ", ".join([dataset.title for dataset in self.dataset_set.all()])


class Parameter(models.Model):
    PARAMETER_CHOICES = (
        ('Social', 'Social'),
        ('Environment', 'Environment'),
        ('Infrastructure', 'Infrastructure'),
        ('Urban Design', 'Urban Design'),
    )
    title = models.CharField(max_length=20, choices=PARAMETER_CHOICES, blank=True, default='', unique=True)

    def __str__(self):
        return self.title

    def get_datasets(self):
        return ", ".join([dataset.title for dataset in self.dataset_set.all()])


class Outcome(models.Model):
    OUTCOME_CHOICES = (
        ('Well Being', 'Well Being'),
        ('Health', 'Health'),
        ('Environment', 'Environment'),
        ('Equity', 'Equity'),
        ('Livability', 'Livability'),
    )
    title = models.CharField(max_length=20, choices=OUTCOME_CHOICES, blank=True, default='', unique=True)

    def __str__(self):
        return self.title

    def get_datasets(self):
        return ", ".join([dataset.title for dataset in self.dataset_set.all()])


# DataSets
class DataSetManager(models.Manager):
    def get_queryset(self):
        return super(DataSetManager, self).get_queryset().all()


class DataSet(models.Model):
    # Info for Page Fields
    title = models.CharField(max_length=20, default='place title here', unique=True)
    slug = models.SlugField(max_length=50, default='', unique=True)
    description = models.CharField(max_length=250, default='None')
    context = models.CharField(max_length=100, default='None')
    key_takeaways = models.CharField(max_length=50, default='None')
    sample_uses_and_visualization = models.CharField(max_length=100, default='None')
    technical_details = models.CharField(max_length=100, default='None')
    applicable_models = models.CharField(max_length=100, default='None')
    relevant_publications = models.CharField(max_length=50, default='None')
    contact_details = models.CharField(max_length=50, default='None')
    owner = models.CharField(max_length=50, default='None')
    publish = models.DateTimeField(default=timezone.now)  # used when you want to specify specific date time in model

    # Filters
    scales = models.ManyToManyField(Scale)
    parameters = models.ManyToManyField(Parameter)
    outcomes = models.ManyToManyField(Outcome)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(viewname='data:dataset_detail', kwargs={'slug': self.slug})

    def get_scales(self):
        return ", ".join([scale.title for scale in self.scales.all()])

    def get_parameters(self):
        return ", ".join([param.title for param in self.parameters.all()])

    def get_outcomes(self):
        return ", ".join([outcome.title for outcome in self.outcomes.all()])
