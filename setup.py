import os

os.environ['DJANGO_SETTINGS_MODULE'] = \
    'test_project.settings'

from setuptools import setup

setup(
    name='cmsbootstrap',
    version='0.140402',
    author='Tom Daley and Chris Wilson',
    author_email='support+cmsbootstrap@aptivate.org',
    packages=['cmsbootstrap'],
    url='https://github.com/aptivate/cmsbootstrap',
    license='LICENSE',
    description='Django-CMS basic theme with Bootstrap to get you started quickly',
    #long_description=open('README.md').read(),
    install_requires=[
        "Django >= 1.5, < 1.6",
        "django-cms >= 2.4.3, < 3.0c1",
        "django-assets >= 0.8",
        "south >= 0.8.4",
    ],
    tests_require=[
    ],
    test_suite = "cmsbootstrap.tests",
)
