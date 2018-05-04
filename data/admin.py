from django.contrib import admin
from django.db import models
from .models import DataSet, Type, Scale, Parameter, Outcome, Time, WorldRegions
from django.forms import CheckboxSelectMultiple


class DataSetAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}  # built in feature
    list_display = ('title', 'slug', 'status', 'type', 'get_parameters', 'get_outcomes', 'get_scales', 'get_time',
                    'get_world_regions')  # built in feature
    list_filter = ('type', 'status', 'parameters', 'outcomes', 'spatial_scales', 'temporal_scales', 'world_regions')  # built in feature
    search_fields = ('title', 'slug', 'spatial_scales__title', 'parameters__title', 'outcomes__title', 'type', 'temporal_scales__title',
                     'world_regions__title')  # built in feature
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
admin.site.register(DataSet, DataSetAdmin)


class TimeAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_data')
admin.site.register(Time, TimeAdmin)


class WorldRegionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_data')
admin.site.register(WorldRegions, WorldRegionsAdmin)


class ScaleAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_data')
admin.site.register(Scale, ScaleAdmin)


class ParameterAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_data')
admin.site.register(Parameter, ParameterAdmin)


class OutcomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_data')
admin.site.register(Outcome, OutcomeAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_models', 'get_datasets')
admin.site.register(Type, TypeAdmin)
