from django.contrib.sitemaps import Sitemap
from .models import DataSet


class DatasetSitemap(Sitemap):
    changefreq = 'weekly'  # Change of frequency of post filter
    priority = 0.5  # Relevance of blog posts in website

    def items(self):  # Queryset objects to include in sitemap
        return DataSet.published.all()

    def lastmod(self, obj):  # Receives each object returned by items and returns last time object is modified
        return obj.updated

        # If want to specify URL for each object, add location method to class
        # def location(self, obj):
        #     return None

