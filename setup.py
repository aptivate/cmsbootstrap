import os

os.environ['DJANGO_SETTINGS_MODULE'] = \
    'test_project.settings'

from setuptools import setup

setup(
    name='cmsbootstrap',
    version='0.140721',
    author='http://www.aptivate.org/',
    author_email='support+cmsbootstrap@aptivate.org',
    packages=['cmsbootstrap'],
    include_package_data=True,
    url='https://github.com/aptivate/cmsbootstrap',
    license='LICENSE',
    description='Django-CMS basic theme with Bootstrap to get you started quickly',
    #long_description=open('README.md').read(),
    setup_requires = [ "setuptools_git >= 0.3", ],
    install_requires=[
        "Django", # 1.5 or 1.6
        "django-cms", # 2.4 or 3.0
        "django-assets >= 0.10",
        "south >= 0.8.4",
        "pyScss >= 1.2.0.post3",
        "cssmin >= 0.2.0",
        "jsmin >= 2.0.9",
    ],
    dependency_links=[
        "git+https://github.com/miracle2k/django-assets.git@8b0a63fab4221cebd927b4022f4daae1a1f46b70#egg=django-assets",
    ],
    tests_require=[
    ],
    test_suite = "cmsbootstrap.tests",
)
