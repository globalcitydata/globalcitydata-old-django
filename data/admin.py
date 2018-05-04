from django.contrib import admin
from django.db import models
from .models import DataSet, Type, Scale, Parameter, Outcome, Time, FuturesModeling
from django.forms import CheckboxSelectMultiple


class DataSetAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}  # built in feature
    list_display = ('title', 'slug', 'get_scales', 'get_parameters', 'get_outcomes', 'status', 'type', 'get_time',
                    'get_futures_modeling')  # built in feature
    list_filter = ('spatial_scales', 'parameters', 'outcomes', 'status', 'type', 'temporal_scales', 'futures_modeling')  # built in feature
    search_fields = ('title', 'slug', 'spatial_scales__title', 'parameters__title', 'outcomes__title', 'type', 'temporal_scales__title',
                     'futures_modeling__title')  # built in feature
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
admin.site.register(DataSet, DataSetAdmin)


# class TimeAdmin(admin.ModelAdmin):
#     list_display = ('title', 'get_data')
# admin.site.register(Time, TimeAdmin)
#
#
# class FuturesModelingAdmin(admin.ModelAdmin):
#     list_display = ('title', 'get_data')
# admin.site.register(FuturesModeling, FuturesModelingAdmin)
#
#
# class ScaleAdmin(admin.ModelAdmin):
#     list_display = ('title', 'get_data')
# admin.site.register(Scale, ScaleAdmin)
#
#
# class ParameterAdmin(admin.ModelAdmin):
#     list_display = ('title', 'get_data')
# admin.site.register(Parameter, ParameterAdmin)
#
#
# class OutcomeAdmin(admin.ModelAdmin):
#     list_display = ('title', 'get_data')
# admin.site.register(Outcome, OutcomeAdmin)
#
#
# class TypeAdmin(admin.ModelAdmin):
#     list_display = ('title', 'get_models', 'get_datasets')
# admin.site.register(Type, TypeAdmin)
