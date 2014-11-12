#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2014 The World in Twelve.

import common
import jinja2
import os
import urllib
import webapp2


class TopHandler(webapp2.RequestHandler):
  def get(self, lang):
    top_template = common.GetTemplate('/top.html')
    cities = ['tokyo']
    cities.extend(common.CITIES)
    body = top_template.render({
      'cities': [common.CITY_METAS[c] for c in cities],
      'lang': lang
    })
    self.response.write(common.WrapWithBaseTemplate(body, lang, []))


class PeopleHandler(webapp2.RequestHandler):
  def get(self, lang):
    base_template = common.GetTemplate('base.html')
    people_template = common.GetTemplate('people_%s.html' % lang)
    people_body = people_template.render()
    self.response.write(common.WrapWithBaseTemplate(people_body, lang, ['people']))


class SponsorsHandler(webapp2.RequestHandler):
  def get(self, lang):
    base_template = common.GetTemplate('base.html')
    sponsors_template = common.GetTemplate('sponsors_%s.html' % lang)
    sponsors_body = sponsors_template.render()
    self.response.write(common.WrapWithBaseTemplate(sponsors_body, lang, ['sponsors']))


class TestCityHandler(webapp2.RequestHandler):
  def get(self, lang):
    base_template = common.GetTemplate('base.html')
    test_city_template = common.GetTemplate(
        '/cities/%s/test_city_tokyo.html' % lang)
    info_template = common.GetTemplate('cities/info_frame.html')
    tokyo_template = common.GetTemplate('cities/%s/tokyo.html' % lang)
    info = info_template.render({
      'description': tokyo_template.render(),
      'meta': common.CITY_METAS['tokyo'],
      'item_id': 'tokyo',
    })
    body = test_city_template.render({
      'info': info,
      'lang': lang
    })
    self.response.write(
        common.WrapWithBaseTemplate(body, lang, ['test_city_tokyo']))


class NotFoundHandler(webapp2.RequestHandler):
  def get(self, lang):
    base_template = common.GetTemplate('base.html')
    template = common.GetTemplate('not_found.html')
    body = template.render()
    self.response.write(common.WrapWithBaseTemplate(body, lang, ['not_found']))


class ComingSoonHandler(webapp2.RequestHandler):
  def get(self, lang):
    base_template = common.GetTemplate('base.html')
    template = common.GetTemplate('coming_soon.html')
    body = template.render()
    self.response.write(common.WrapWithBaseTemplate(body, lang, ['coming_soon']))


class TacHandler(webapp2.RequestHandler):
  def get(self):
    base_template = common.GetTemplate('base.html')
    sponsors_template = common.GetTemplate('tac.html')
    sponsors_body = sponsors_template.render()
    self.response.write(common.WrapWithBaseTemplate(sponsors_body, 'en', ['tac']))


app = webapp2.WSGIApplication([
    # English is the default.
    webapp2.Route('/', webapp2.RedirectHandler, defaults={
      '_uri': '/en/', '_code': 301}),
    ('/(en|ja)/', TopHandler),
    ('/(en|ja)/people', PeopleHandler),
    ('/(en|ja)/sponsors', SponsorsHandler),
    ('/(en|ja)/test_city_tokyo', TestCityHandler),
    ('/tac', TacHandler),
    ('/(en|ja)/not_found', NotFoundHandler),
    ('/(en|ja)/coming_soon', ComingSoonHandler),
], debug=True)
