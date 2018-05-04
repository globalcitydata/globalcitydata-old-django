from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.template.defaultfilters import slugify

STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)


# Filters
class Scale(models.Model):
    SCALE_CHOICES = (
        ('Intra Urban', 'Intra Urban'),
        ('Whole City', 'Whole City'),
        ('National Urban', 'National Urban'),
    )
    title = models.CharField(max_length=20, choices=SCALE_CHOICES, blank=True, default='', unique=True)

    def __str__(self):
        return self.title

    def get_data(self):
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

    def get_data(self):
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

    def get_data(self):
        return ", ".join([dataset.title for dataset in self.dataset_set.all()])


class Type(models.Model):
    DATA_TYPES = (
        ('Dataset', 'Dataset'),
        ('Model', 'Model'),
    )
    title = models.CharField(max_length=10, choices=DATA_TYPES, blank=True, default='', unique=True)

    def __str__(self):
        return self.title

    def get_models(self):
        return self.objects.all().filter(title='Model')

    def get_datasets(self):
        return self.objects.all().filter(title='Dataset')


class Time(models.Model):
    TIME_CHOICES = (
        ('One Time Assessment', 'One Time Assessment'),
        ('Time Series', 'Time Series')
    )
    title = models.CharField(max_length=20, choices=TIME_CHOICES, blank=True, default='', unique=True)

    def __str__(self):
        return self.title

    def get_data(self):
        return ", ".join([dataset.title for dataset in self.dataset_set.all()])


class FuturesModeling(models.Model):
    FUTURES_CHOICES = (
        ('Historical Data', 'Historical Data'),
        ('Base Year Data', 'Base Year Data'),
        ('Futures Modeling Data', 'Futures Modeling Data')
    )
    title = models.CharField(max_length=25, choices=FUTURES_CHOICES, blank=True, default='', unique=True)

    def __str__(self):
        return self.title

    def get_data(self):
        return ", ".join([dataset.title for dataset in self.dataset_set.all()])


# DataSets
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class DatasetManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type__title='Dataset')


class DatasetModelsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type__title='Model')


class DataSet(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    title = models.CharField(max_length=50, default='', unique=True)
    slug = models.SlugField(max_length=50, default='', unique=True)
    description = models.CharField(max_length=250, default='')
    context = models.CharField(max_length=100, default='')
    key_takeaways = models.CharField(max_length=50, default='')
    sample_uses_and_visualization = models.CharField(max_length=100, default='')
    technical_details = models.CharField(max_length=100, default='')
    applicable_models_or_datasets = models.CharField(max_length=100, default='')
    relevant_publications = models.CharField(max_length=50, default='')
    contact_details = models.EmailField(max_length=50, default='example@gmail.com')
    owner = models.CharField(max_length=50, default='')
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Retrieve published datasets
    datasets = DatasetManager()
    datasetModels = DatasetModelsManager()

    # Filters
    scales = models.ManyToManyField(Scale)
    parameters = models.ManyToManyField(Parameter)
    outcomes = models.ManyToManyField(Outcome)
    time = models.ManyToManyField(Time)
    futures_modeling = models.ManyToManyField(FuturesModeling)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(DataSet, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(viewname='data:detail', kwargs={'slug': self.slug})

    def get_scales(self):
        return ", ".join([scale.title for scale in self.scales.all()])

    def get_parameters(self):
        return ", ".join([param.title for param in self.parameters.all()])

    def get_outcomes(self):
        return ", ".join([outcome.title for outcome in self.outcomes.all()])

    def get_time(self):
        return ", ".join([time.title for time in self.time.all()])

    def get_futures_modeling(self):
        return ", ".join([future.title for future in self.futures_modeling.all()])

    class Meta:
        ordering = ('title',)
