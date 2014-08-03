from __future__ import absolute_import, unicode_literals

import re

from django.core.management import call_command
from django.template import Context, Template
from django.test import TestCase

import cms.api
from sekizai.context import SekizaiContext

from django_harness.fast_dispatch import FastDispatchMixin
from django_harness.html_parsing import HtmlParsingMixin

class SimpleTest(FastDispatchMixin, HtmlParsingMixin, TestCase):
    longMessage = True

    def setUp(self):
        self.home = cms.api.create_page(title="Home Page",
            template="custom/homepage.html", language="en", slug="home",
            reverse_id="home",
            published=True)
        title = self.home.title_set.all()[0]
        title.page_title = "Home Page (whee)"
        title.save()
        self.publish_page(self.home)
        self.fake_request = self.get_fake_request('/fake_request')

    def test_get_homepage(self):
        """
        Test that we can download and render the fixture home page correctly.
        This requires that django-cms isn't broken by installing this module.
        """

        response = self.client.get('/en/')
        self.assertContains(response, 'CMSBootstrap')

    def test_homepage_structure(self):
        response = self.client.get('/en/')
        body = self.query(response, 'body')
        self.assertEquals('slug_home lang_en template_homepage', body.get('class'),
            "Wrong CSS classes on body element")

        header = self.query(body, 'header')
        self.assertEqual('cmsbootstrap_header container-fluid', header.get('class'))
        # http://html5doctor.com/the-main-element/
        self.assertEqual('banner', header.get('role'))
        user_access = self.query(header, 'nav.user_access')
        header_nav = self.query(header, 'ul.header_nav')
        self.assertEquals('header_nav nav nav-pills', header_nav.get('class'))
        self.assertEquals('navigation', header_nav.get('role'))

        main = self.query(body, 'main')
        self.assertEquals('container-fluid', main.get('class'))
        self.assertEquals('main', main.get('role'))
        article = self.query(main, 'article')

        breadcrumb_wrap = self.query(main, '.breadcrumb_wrap')
        self.assertEquals('breadcrumb_wrap row', breadcrumb_wrap.get('class'))
        self.assertEquals('breadcrumb col-sm-12',
            self.query(breadcrumb_wrap, 'ul').get('class'))

        footer = self.query(body, 'footer')
        self.assertEquals('container-fluid', footer.get('class'))
        # http://html5doctor.com/the-main-element/
        self.assertEquals('contentinfo', footer.get('role'))
        footer_nav = self.query(footer, 'nav')
        self.assertEquals('navbar navbar-default', footer_nav.get('class'))
        self.assertEquals('navigation', footer_nav.get('role'))

    def assert_override_block(self, template_name, block_to_override,
            path_to_expect_content, attribute_if_not_text=None,
            element_not_to_find=None, override_block_with="Hello world!",
            context={}, skip=[]):

        if block_to_override in skip:
            return # without testing anything

        template = Template("""
            {%% extends "%(template_name)s" %%}
            {%% block %(block_to_override)s %%}{%% spaceless %%}
            %(override_block_with)s
            {%% endspaceless %%}{%% endblock %%}
            """ % dict(template_name=template_name,
                block_to_override=block_to_override,
                override_block_with=override_block_with))

        context.setdefault('request', self.fake_request)
        html = template.render(SekizaiContext(context))
        element = self.query(html, path_to_expect_content)

        if attribute_if_not_text is None:
            values = [element.text]
            values.extend([e.tail for e in element])
            value = ",".join([v for v in values if v is not None])
        else:
            value = element.get(attribute_if_not_text)
            if value is None: value = ''

        self.assertIn(override_block_with, value,
            "Did not find expected text in correct location (%s) when overriding "
            "block '%s' on template '%s'. The complete output was: %s" %
            (path_to_expect_content, block_to_override, template_name, html))

        if element_not_to_find is not None:
            unexpected_matches = self.query(html,
                "%s %s" % (path_to_expect_content, element_not_to_find),
                list=True, required=False)

            self.assertEquals([],
                [self.tostring(e) for e in unexpected_matches],
                "An element that should have been replaced was found in the "
                "rendered page: %s" % element_not_to_find)

        return html

    def test_page_title(self):
        response = self.client.get('/en/')

        title = self.query(response, 'html > head > title').text
        title = re.sub(r'\s+', ' ', title.strip())

        self.assertEqual('CMSBootstrap - Home Page (whee)', title)

    def assert_override_template_blocks(self, template, skip=[]):
        self.assert_override_block(template, 'title', 'html > head > title', skip=skip)

        """
        def extract_title(block_to_override):
            title = self.assert_override_block(template, block_to_override,
                'html > head > title', override_block_with='foobar')
            title = self.query(title, 'html > head > title').text
            title = re.sub(r'\s+', ' ', title.strip())
            return title
        self.assertEquals('foobar - Home Page (whee)', extract_title('site_name'))
        self.assertEquals('CMSBootstrap - foobar', extract_title('page_title'))
        """

        self.assert_override_block(template, 'viewport', 'html > head',
            element_not_to_find='> meta[name=viewport]', skip=skip)
        self.assert_override_block(template, 'media', 'html > head',
            element_not_to_find='> link[rel=stylesheet]', skip=skip)
        self.assert_override_block(template, 'standard_css', 'html > head',
            element_not_to_find='> link[rel=stylesheet]', skip=skip)

        self.assert_override_block(template, 'body_classes', 'html > body',
            attribute_if_not_text='class', skip=skip)
        self.assert_override_block(template, 'header', 'html > body',
            element_not_to_find='header', skip=skip)
        self.assert_override_block(template, 'logo', 'html > body > header', skip=skip)
        self.assert_override_block(template, 'user_access', 'html > body > header',
            element_not_to_find='nav.user_access', skip=skip)
        self.assert_override_block(template, 'user_login_links',
            'html > body > header > nav.user_access > div.user_login_links',
            element_not_to_find='div.user_login', skip=skip)
        self.assert_override_block(template, 'search_box',
            'html > body > header', skip=skip)
        self.assert_override_block(template, 'header_nav',
            'html > body > header', element_not_to_find='nav.cmsbootstrap_header',
            skip=skip)
        self.assert_override_block(template, 'header_nav_menu',
            'nav.cmsbootstrap_header .navbar-collapse > ul',
            element_not_to_find='li.language_menu', skip=skip)
        self.assert_override_block(template, 'language_menu',
            'nav.cmsbootstrap_header .navbar-collapse > ul',
            element_not_to_find='li.language_menu_item', skip=skip)

        self.assert_override_block(template, 'main', 'html > body',
            element_not_to_find='main', skip=skip)
        self.assert_override_block(template, 'main_classes', 'html > body > main',
            attribute_if_not_text='class', skip=skip)
        self.assert_override_block(template, 'breadcrumb_wrap',
            'html > body > main', element_not_to_find='div.breadcrumb_wrap', skip=skip)
        self.assert_override_block(template, 'breadcrumb_wrap_classes',
            'html > body > main > div',
            attribute_if_not_text='class', skip=skip)
        self.assert_override_block(template, 'breadcrumb_classes',
            'html > body > main > .breadcrumb_wrap > ul',
            attribute_if_not_text='class', skip=skip)
        self.assert_override_block(template, 'article',
            'html > body > main', element_not_to_find='article', skip=skip)
        self.assert_override_block(template, 'content',
            'html > body > main > article', skip=skip)

        self.assert_override_block(template, 'footer', 'html > body',
            element_not_to_find='footer', skip=skip)
        self.assert_override_block(template, 'footer_classes', 'html > body > footer',
            attribute_if_not_text='class', skip=skip)
        self.assert_override_block(template, 'footer_nav_classes',
            'html > body > footer nav', attribute_if_not_text='class', skip=skip)
        self.assert_override_block(template, 'credits',
            'html > body > footer nav > .footer_right',
            element_not_to_find='a', skip=skip)
        self.assert_override_block(template, 'js_footer',
            'html > body', element_not_to_find='script', skip=skip)

    def test_homepage_blocks(self):
        self.assert_override_template_blocks("custom/base.html")

    def assert_page_3col_structure(self, response, skip=[]):
        body = self.query(response, 'body')
        main = self.query(body, 'main')

        self.query(main, 'article')
        if 'sidebar_left' not in skip:
            self.query(main, 'nav.sidebar_left')
        if 'sidebar_right' not in skip:
            self.query(main, 'div.sidebar_right')

        self.assert_override_block(self.home.template, 'sidebar_left',
            'html > body > main > .article.row',
            element_not_to_find='nav.sidebar_left', skip=skip)

        self.assert_override_block(self.home.template, 'content_body',
            'html > body > main > .article.row',
            element_not_to_find='article', skip=skip)

        self.assert_override_block(self.home.template, 'messages',
            'html > body > main > .article.row > article',
            context={'messages': ["Whee!"]},
            element_not_to_find='div.alert', skip=skip)

        self.assert_override_block(self.home.template, 'main_section_title',
            'html > body > main > .article.row > article', skip=skip)

        self.assert_override_block(self.home.template, 'main_content',
            'html > body > main > .article.row > article', skip=skip)

        self.assert_override_block(self.home.template, 'sidebar_right',
            'html > body > main > .article.row',
            element_not_to_find='nav.sidebar_right', skip=skip)

        self.assert_override_block(self.home.template, 'sidebar_right_content',
            'html > body > main > .article.row > .sidebar_right > .sidebar_right_inner',
            skip=skip)

    def publish_page(self, page):
        try:
            page.publish() # cms2
        except TypeError:
            page.publish('en') # cms3

    def test_page_3col_notitle_structure(self):
        self.home.template = 'custom/page_3col_notitle.html'
        self.publish_page(self.home)

        response = self.client.get('/en/')
        self.assertEquals(self.home.template, response.templates[0].name)

        body = self.query(response, 'body')
        self.assertEquals('slug_home lang_en template_page_3_columns_notitle',
            body.get('class'), "Wrong CSS classes on body element")

        self.assert_page_3col_structure(response)

    def test_page_3col_structure(self):
        self.home.template = 'custom/page_3col.html'
        self.publish_page(self.home)

        response = self.client.get('/en/')
        self.assertEquals(self.home.template, response.templates[0].name)

        body = self.query(response, 'body')
        self.assertEquals('slug_home lang_en template_page_3_columns',
            body.get('class'), "Wrong CSS classes on body element")

        self.assert_page_3col_structure(response)
        self.assert_override_block(self.home.template, 'main_section_title',
            'html > body > main > .article.row > article', element_not_to_find='h1')

    def test_page_1col_structure(self):
        self.home.template = 'custom/page_1col.html'
        self.publish_page(self.home)

        response = self.client.get('/en/')
        self.assertEquals(self.home.template, response.templates[0].name)

        body = self.query(response, 'body')
        self.assertEquals('slug_home lang_en template_page_1_column',
            body.get('class'), "Wrong CSS classes on body element")

        self.assert_page_3col_structure(response,
            skip=['sidebar_left', 'sidebar_right', 'sidebar_right_content'])
        self.assert_override_block(self.home.template, 'main_section_title',
            'html > body > main > .article.row > article', element_not_to_find='h1')

        self.assertEquals([], [self.tostring(e)
            for e in self.query(body, 'main > nav.sidebar_left', list=True,
                required=False)], "Left sidebar should have been hidden but wasn't")
        self.assertEquals([], [self.tostring(e)
            for e in self.query(body, 'main > div.sidebar_right', list=True,
                required=False)], "Right sidebar should have been hidden but wasn't")

    def test_homepage_structure(self):
        self.home.template = 'custom/homepage.html'
        self.publish_page(self.home)

        response = self.client.get('/en/')
        self.assertEquals(self.home.template, response.templates[0].name)

        body = self.query(response, 'body')
        self.assertEquals('slug_home lang_en template_homepage',
            body.get('class'), "Wrong CSS classes on body element")

        self.query(body, 'main > div.content_body')
        self.query(body, 'main > div.content_body > div.row.intro')
        self.query(body, 'main > div.content_body > div.row.intro > section.page_intro')
        self.query(body, 'main > div.content_body > div.row.intro > section.page_features')
        self.query(body, 'main > div.content_body > div.row.latest')
        self.query(body, 'main > div.content_body > div.row.latest > section.latest_section_1')
        self.query(body, 'main > div.content_body > div.row.latest > section.latest_section_2')

    def test_can_build_assets(self):
        call_command('assets', 'build')
