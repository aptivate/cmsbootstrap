import collections

# Custom BreadCrumb "class" for use with context['custom_breadcrumb']
# to override the Django-CMS breadcrumbs if necessary for your app.

BreadCrumb = collections.namedtuple("BreadCrumb", ["title", "url"])
