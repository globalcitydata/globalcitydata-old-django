from django.contrib import admin
from django.db import models
from .models import DataSet, DataSetModel, Scale, Parameter, Outcome
from django.forms import CheckboxSelectMultiple


class DataSetAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}  # built in feature
    list_display = ('title', 'slug', 'get_scales', 'get_parameters', 'get_outcomes', 'publish')  # built in feature
    list_filter = ('scales', 'parameters', 'outcomes', 'publish')  # built in feature
    search_fields = ('title', 'slug', 'scales__title', 'parameters__title', 'outcomes__title')  # built in feature
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
admin.site.register(DataSet, DataSetAdmin)


class DataSetModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}  # built in feature
    list_display = ('title', 'slug', 'get_scales', 'get_parameters', 'get_outcomes', 'publish')  # built in feature
    list_filter = ('scales', 'parameters', 'outcomes', 'publish')  # built in feature
    search_fields = ('title', 'slug', 'scales__title', 'parameters__title', 'outcomes__title')  # built in feature
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
admin.site.register(DataSetModel, DataSetModelAdmin)

# Only Need Following To Change DataSet Tags
# class ScaleAdmin(admin.ModelAdmin):
#     list_display = ('title', 'get_datasets')
# admin.site.register(Scale, ScaleAdmin)
#
#
# class ParameterAdmin(admin.ModelAdmin):
#     list_display = ('title', 'get_datasets')
# admin.site.register(Parameter, ParameterAdmin)
#
#
# class OutcomeAdmin(admin.ModelAdmin):
#     list_display = ('title', 'get_datasets')
# admin.site.register(Outcome, OutcomeAdmin)
