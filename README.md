# cmsbootstrap

Django-CMS extensible basic theme with Bootstrap to get you started quickly.

![Build Status on Travis](https://travis-ci.org/aptivate/cmsbootstrap.svg?branch=master)

## Purpose

Django-CMS is very powerful, but comes with no themes by default.
[They say](https://groups.google.com/d/msg/django-cms/4oxF9goRk2g/WEPLSk7OzdYJ):

> Themes are outside the django CMS scope. If you wish to theme the admin,
> just override the template `admin/base_site.html` and include some custom css.

That's all very well, but everyone wanting to start a new project with
Django-CMS faces a lot of study, effort and difficult choices just to get
their first pages to display sensibly. This is where we can help.

## Philosophy

CMS Bootstrap aims to:

### Work with Django-CMS

Themes for non-CMS projects are out of scope.

### Work out of the box

Provide a reasonable basic theme for a Django-CMS site automatically,
out of the box, with no effort.

### Use Bootstrap

Use the Bootstrap project to provide a sensible default theme (toolkit)
that you can pull bits from when you need them, without getting in your way.

### Be reasonably extensible

Make the simple things simple, and the hard things possible. Changing
colours, fonts and sizes should be easy with SCSS.

To that end, we use the
[Sass/SCSS version of Bootstrap](http://getbootstrap.com/getting-started/#download-sass)
so that you can quickly enable and disable modules and change colours.

### Be lightweight

Low bandwidth accessibility is a big part of our philosophy, and this theme
needs to support that. Using Bootstrap/Sass allows us to enable and disable
Bootstrap modules quickly, so we can skip large chunks of CSS and keep the
overall page weight small, while still being flexible.

Our goal on our first project is to keep our pages below 100 kB compressed,
including images, CSS and javascript. This allows them to be loaded within
10 seconds on an 80 kbps connection. Standard Bootstrap CSS alone is 99 kB
(bootstrap-3.1.1-dist/css/bootstrap.min.css), which leaves no room for anything
else on the page within our budget!

### Be reusable

This is related to being extensible, but often in conflict. For example:

To be extensible, a theme needs a lot of hooks to override in subclasses:
Django template blocks, CSS classes applied to elements, etc. But all the
hooks that you're not using are noise that clutters and bloats your pages,
so a page full of hooks is a poor template to copy and modify in your own
code, at least not without ripping out a lot of code.

So our aim is to have *likely* extension points, but not *every possible*
one. Other reuse mechanisms such as:

* Importing existing files wholesale
* Extending (importing and then overriding) existing files
* Reusing a block's contents, but adding to it
* Replacing a file completely
* Disabling a file

should all be supported and used where possible in preference to cluttering
every template with every possible extension point.

### Be maintainable

For the same reason, our "API" to developers should be clear, simple, and
stable: unlikely to change, or need to be changed in future to support newer
versions of Django, Django-CMS, Bootstrap, etc.

This allows developers using CMSBootstrap in their projects to upgrade to the
latest version (for example, if there is a security vulnerability in the CSS,
or to support a newer version of Django) with minimal risk that it will break
their projects and require extensive repair.

### Be portable

As well as slow and unreliable connections, our philosophy is that websites
should be accessible:

* Using old browsers (e.g. Internet Explorer 8) for those without bandwidth,
  skills or permission to upgrade their browsers.
* Using mobile devices (smart phones, feature phones, low cost tablets) as well
  as desktop PCs. So our designs should be responsive, compatible with
  older and simpler browsers such as Opera Mini, and not require Javascript.
* Using free software (Linux, Firefox, Chromium etc.) as well as Windows,
  Internet Explorer and Flash, to access our websites.
* By people using assistive technology (screen readers etc.)
* Into the future, by using web standards properly. So we use HTML5 elements
  such as `header` and `nav` elements, and add backwards compatibility in
  IE8 using Javascript.

Where these standard conflict, we aim to support the largest possible number
of users in our target audience.

### Use Django-Assets

We use [django-assets](https://github.com/miracle2k/django-assets) to
automatically compile Sass/SCSS to standard, minified CSS. It will make your
life better, so we think you should use it too.

You can manually compile the Sass files to standard CSS if you really want to.

## Contents

The Github project contains the following files and directories:

* cmsbootstrap: the app which you can add to `INSTALLED_APPS` in Django.
  * models.py: an empty models file to keep Django happy.
  * static: static resources: Sass/SCSS, CSS and JavaScript.
    * bootstrap-sass-3.1.1.tar.gz: the complete sources for
      the supplied version of Bootstrap (in Sass/SCSS format).
    * css/cmsbootstrap/ie7.css: Internet Explorer 7
      compatibility CSS library (minimal, just for the included styles).
    * css/cmsbootstrap/ie8.css: Internet Explorer 8
      compatibility CSS library (minimal, just for the included styles).
    * js/bootstrap.js, js/bootstrap: the JavaScript libraries supplied with
      Bootstrap.
    * js/html5shiv.js, js/lte-ie7.js, js/respond.min.js: compatibility
      libraries for Internet Explorer 8 (responsive media queries and HTML5
      elements).
    * sass/bootstrap: Bootstrap Sass/SCSS source files.
    * sass/cmsbootstrap.scss: a few additional styles in Sass/SCSS format.
  * templates: the supplied templates.
    * base.html: the root base template, intended to
      be overridden by you.
    * cmsbootstrap: the example templates, not
      intended to be overridden but extended or ignored and replaced.
    * cmsbootstrap/menu/breadcrumb.html:
      render Django-CMS breadcrumbs using Bootstrap styles.
    * cmsbootstrap/menu/language_chooser.html:
      render Django-CMS language chooser using Bootstrap styles.
    * cmsbootstrap/menu/menu.html:
      render Django-CMS menus using Bootstrap styles.
    * cmsbootstrap/placeholders_extra.html:
      template with placeholders for extra bits of text that can be inserted
      into other pages.
  * tests: test cases for cmsbootstrap, may be affected by
    your own application choices (e.g. changing URLs, languages or pages.)
  * views.py: no views are currently provided.

## Usage

### With DYE

If you don't yet have a Django-CMS project, the easiest way to get started is:

* [use DYE and cookiecutter](https://github.com/aptivate/dye/blob/develop/readme-cookiecutter.rst)
  to create one,
* enter `cms` for the *Project type*.

Whether this is a new or an existing DYE project, add `cmsbootstrap` to it:

* add this line to `deploy/pip_packages.txt`:
    -e git+https://github.com/aptivate/cmsbootstrap.git
* run `deploy/bootstrap.py`,
* run `deploy/tasks.py deploy:dev`.

### Manual Installation

If you're not using DYE, then install `cmsbootstrap` in your global Python
environment or virtualenv:

    pip install cmsbootstrap

Or if it's not available on PyPI, or you need a newer version:

    pip install -e git+https://github.com/aptivate/cmsbootstrap.git

Of course you need [Django](https://www.djangoproject.com/)
(1.5 or higher) and
[Django-CMS](https://www.django-cms.org/en/) (2.4 or higher) in your
environment as well. They'll be installed automatically by Pip if you don't
have them already.

### Add to `INSTALLED_APPS`

Add `django_assets` and `cmsbootstrap` to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'django_assets',
        'cmsbootstrap',
    )

Add `django_assets.finders.AssetsFinder` to your `STATICFILES_FINDERS`:

    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'django_assets.finders.AssetsFinder',
    )

Ensure that you have the `LocaleMiddleware` enabled in your `MIDDLEWARE_CLASSES`:

    MIDDLEWARE_CLASSES = (
        # other middleware ...
        'django.middleware.locale.LocaleMiddleware',
    )

You'll need to add some templates too. You don't need all of these, but you
probably want at least one simple page design, a custom home page, and the
global placeholders.

    CMS_TEMPLATES = (
        ('cmsbootstrap/page_1col.html', 'CMS Simple Page (no sidebars)'),
        ('cmsbootstrap/page_3col.html', 'CMS Simple Page (both sidebars)'),
        ('cmsbootstrap/page_3col_notitle.html', 'CMS Simple Page (without title, for plugins)'),
        ('cmsbootstrap/homepage.html', 'CMS Home Page'),
        ('cmsbootstrap/placeholders_extra.html', 'CMS Global Placeholders'),
    )

This allows Django to find the templates and static files that we've provided.
It also allows `django-assets` to find the assets and compile them.

### Building the assets

You'll have to build the assets (CSS files) from the Sass sources at least
once:

    django/website/manage.py assets build

Or you can run the following command, in a spare terminal, to watch the sources
for changes and rebuild them automatically when necessary:

    django/website/manage.py assets watch

### Creating a superuser

If you don't have one already, you'll need a superuser to log into the
Django-CMS admin. You can create one like this:

    django/website/manage.py createsuperuser

And run the development server (in a spare terminal):

    django/website/manage.py runserver

You should be able to access http://localhost:8000/ and see the Django-CMS pony.

### Starting your site

If you haven't used Django-CMS before, we recommend that you start with the
[tutorial](http://docs.django-cms.org/en/2.4.3/getting_started/tutorial.html).

You need some Django-CMS pages to see the templates. If you don't have any,
then you'll just see the Django-CMS pony when you visit your site at
http://localhost:8000/.

Creating pages is not really in the scope of this documentation. You could 
follow the [Creating your first CMS Page](http://docs.django-cms.org/en/2.4.3/getting_started/tutorial.html#creating-your-first-cms-page)
part of the tutorial. Or, if you just want to get started quickly, you can
import the `homepage` fixture to get a simple home page into your CMS (you
can then customise or delete it as you wish):

    django/website/manage.py loaddata homepage

## Customisation

### Extending the provided templates

The default templates that we configured above live in the `cmsbootstrap`
application:

    CMS_TEMPLATES = (
        ('cmsbootstrap/page_3col.html', 'CMS Simple Page'),
        ('cmsbootstrap/homepage.html', 'CMS Home Page'),
        ('cmsbootstrap/placeholders_extra.html', 'CMS Global Placeholders'),
    )

You could override these by creating templates of the same name in an
application of your own. However you must ensure that your app loads after
`cmsbootstrap` in the list of `INSTALLED_APPS`, and you cannot inherit from
these templates if you override them using one of the same name. We recommend
that you override only `base.html` (not `cmsbootstrap/base.html`) as follows.

For example, you can create an app called `main`:

    django/website/manage.py startapp main

Add it to `INSTALLED_APPS` in `django/website/settings.py`:

    LOCAL_APPS = (
        'main',
    )

Create a directory inside the app to hold your templates:

    mkdir -p main/templates

Create your own replacement base template, `main/templates/base.html`, with
the following contents, overriding the one in
`cmsbootstrap/templates/base.html`:

    {% extends "cmsbootstrap/base.html" %}

    {% load cms_tags sekizai_tags i18n %}

    {% block html-title %}
    <title>My Project! - {% block title %}{% page_attribute "page_title" %}{% endblock %}</title>
    {% endblock html-title %}

Note: the `htmltitle` block was copied from the one in
`cmsbootstrap/templates/cmsbootstrap/base.html` and slightly modified. It
overrides the block of the same name in that file. The other `cmsbootstrap`
templates inherit from this one.

Original inheritance tree:

    CMS_TEMPLATES
    => cmsbootstrap/homepage.html
    -> base.html (in the cmsbootstrap app)
    -> cmsbootstrap/base.html (in the cmsbootstrap app)

New inheritance tree:

    CMS_TEMPLATES
    => cmsbootstrap/homepage.html
    -> base.html (in the main app)
    -> cmsbootstrap/base.html (in the cmsbootstrap app)

Note: the only difference is *in which app* the `base.html` template is found
by the Django template loader, which depends on the load order of applications
in `settings.py`.

### Defining new templates

We recommend that you create templates in your own apps, similar to (perhaps
based on) the sample templates in the `cmsbootstrap/templates/cmsbootstrap`
directory (`homepage.html` and `page_3col_notitle.html`). In particular, we
recommend that you start the templates with the following line:

    {% extends "base.html" %}

And override blocks defined in your base template (`main/templates/base.html`)
and/or the `cmsbootstrap` base template from which it inherits
(`cmsbootstrap/templates/cmsbootstrap/base.html`).

## Customisation examples

### Change the site credits

For some strange reason, you might want your pages to end with "Site by Cool
Dude" instead of "Site by Aptivate". You can do that by overriding the `credits`
block of the base template, placing the following code in your `base.html`:

	{% block credits %}
	{% trans "Site by" %} <a href="http://www.example.com">Cool Dude</a>
	{% endblock %}

### Change the top menu to a Bootstrap [Navbar](http://getbootstrap.com/components/#navbar).

You'll need to wrap the `top-navigation` block in some additional markup:

	{% load i18n %}

	{% block top-navigation %}
	<nav class="navbar navbar-default" role="navigation">
		<div class="container-fluid">
			<!-- Brand and toggle get grouped for better mobile display -->
			<div class="navbar-header">
				<button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
					<span class="sr-only">Toggle navigation</span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				</button>
				<a class="navbar-brand" href="#">Cool Dude</a>
			</div>

			<!-- Collect the nav links, forms, and other content for toggling -->
			<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
				{{ block.super }}
			</div>
		</div>
	</nav>
	{% endblock %}

And change the CSS classes of the `<ul class="top-navigation">` element as well:

	{% block top-navigation-classes%}
	top-navigation nav navbar-nav
	{% endblock %}

### Adding CSS styles

You can add a static CSS file to the base template easily:

	{% block css %}
		{{ block.super }}
		<link rel="stylesheet" href="{{ STATIC_URL }}css/additional-static.css" />
	{% endblock %}

### Adding SCSS styles

You can add new Sass/SCSS assets by following the
[django-assets documentation](http://elsdoerfer.name/docs/django-assets/),
creating an `assets.py` file. For example, you could create a `main/assets.py`
like this:

	from django_assets import Bundle, register

	main_css = Bundle(
	    'sass/main/main.scss',
	    filters='pyscss, cssmin',
	    output='css/main/main.css')

	register('main_css', main_css)

And create `main/static/sass/main/main.scss` with whatever additional
Sass/SCSS you'd like to include, for example:

	@import "bootstrap/bootstrap";

	.nav-text {
	    padding: $nav-link-padding;
	}

Because you've imported the `bootstrap.scss` from `cmsbootstrap`, which in turn
imports `variables.scss`, you have access to all the variables defined by it,
such as `$nav-link-padding` used above.

Then you need to include the generated CSS file in your `base.html`:

	{% block css %}
		{{ block.super }}
		<link rel="stylesheet" href="{{ STATIC_URL }}css/main/main.css" />
	{% endblock %}

### Changing Bootstrap variables and values

If you want to make changes to these variables, without copying all of the
`cmsbootstrap` Sass files into your own app, you can add the `cmsbootstrap`
project directory to `PYSCSS_LOAD_PATHS` in `settings.py`:
	
	PYSCSS_LOAD_PATHS = (
	    path.join(path.dirname(__file__), '.ve', 'src', 'cmsbootstrap',
		'cmsbootstrap', 'static', 'sass', 'bootstrap'),
	)

Then you can copy `bootstrap.scss` and `_variables.scss` into your own project,
for example `main/static/sass/bootstrap`:

	mkdir main/static/sass/bootstrap
	cp .ve/src/cmsbootstrap/cmsbootstrap/static/sass/bootstrap/bootstrap.scss main/static/sass/bootstrap
	cp .ve/src/cmsbootstrap/cmsbootstrap/static/sass/bootstrap/_variables.scss main/static/sass/bootstrap

In this case, all of the files imported by `bootstrap.scss` are found in the
`cmsbootstrap` project using the search path, except for the ones that you
copied into `main/static/sass/bootstrap` which are used in preference. So you
can modify the variable values defined in `variables.scss`, and enable or
disable modules in `bootstrap.scss` (most are commented out by default to
reduce bandwidth overhead).

In order to actually compile this, you must have created an `assets.py` in the
`main` app as described above. And you need to replace the `standard-css` block
inherited from `cmsbootstrap/base.html` with your own, including your file
instead of `bootstrap.scss`:

	{% block standard-css %}
		{# note that the inherited block.super is NOT included #}
		<link rel="stylesheet" href="{{ STATIC_URL }}css/cmsbootstrap.css" />
		<link rel="stylesheet" href="{{ STATIC_URL }}css/main/main.css" />
	{% endblock %}
