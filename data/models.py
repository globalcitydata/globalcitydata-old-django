from django.db import models
from django.urls import reverse
from django.utils import timezone

STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)

DATA_TYPES = (
    ('Dataset', 'Dataset'),
    ('Model', 'Model'),
)

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
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Base(models.Model):
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    title = models.CharField(max_length=50, default='', unique=True)
    slug = models.SlugField(max_length=50, default='', unique=True)
    description = models.CharField(max_length=250, default='')
    context = models.CharField(max_length=100, default='')
    key_takeaways = models.CharField(max_length=50, default='')
    sample_uses_and_visualization = models.CharField(max_length=100, default='')
    technical_details = models.CharField(max_length=100, default='')
    applicable_models = models.CharField(max_length=100, default='')
    relevant_publications = models.CharField(max_length=50, default='')
    contact_details = models.EmailField(max_length=50, default='example@gmail.com')
    owner = models.CharField(max_length=50, default='')
    updated = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=10, choices=DATA_TYPES, default='Dataset')

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Retrieve published datasets

    # Filters
    scales = models.ManyToManyField(Scale)
    parameters = models.ManyToManyField(Parameter)
    outcomes = models.ManyToManyField(Outcome)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(viewname='data:detail', kwargs={'slug': self.slug})

    def get_scales(self):
        return ", ".join([scale.title for scale in self.scales.all()])

    def get_parameters(self):
        return ", ".join([param.title for param in self.parameters.all()])

    def get_outcomes(self):
        return ", ".join([outcome.title for outcome in self.outcomes.all()])

    class Meta:
        abstract = True


class DataSet(Base):
    type = models.CharField(max_length=10, choices=DATA_TYPES, default='Dataset')


class DataSetModel(Base):
    type = models.CharField(max_length=10, choices=DATA_TYPES, default='Model')
