#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2014 The World in Twelve.

import common
import datetime
import jinja2
import os
import urllib
import webapp2


class TopHandler(webapp2.RequestHandler):
  def get(self, lang):
    now = datetime.datetime.now()
    date20150101 = datetime.datetime.fromtimestamp(1420090000)
    diff = (now.year * 12 + now.month) - (date20150101.year * 12 + date20150101.month)
    print now, date20150101
    if diff > 11:
      diff = 11

    if lang == 'en':
      label_key = 'label'
    else:
      label_key = 'label_ja'

    current_city_name = common.CITY_METAS[common.CITIES[diff]][label_key]

    top_template = common.GetTemplate('top.html')
    cities = ['tokyo']
    cities.extend(common.CITIES)
    body = top_template.render({
      'cities': [common.CITY_METAS[c] for c in cities],
      'lang': lang,
      'current_city_name': current_city_name
    })
    self.response.write(common.WrapWithBaseTemplate(body, lang, []))


class PeopleHandler(webapp2.RequestHandler):
  def get(self, lang):
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


class TestPageHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write(common.GetTemplate('test/ad.html').render())


app = webapp2.WSGIApplication([
    # English is the default.
    webapp2.Route('/', webapp2.RedirectHandler, defaults={
      '_uri': '/en/', '_code': 301}),
    ('/(en|ja)/', TopHandler),
    ('/(en|ja)/people', PeopleHandler),
    ('/(en|ja)/sponsors', SponsorsHandler),
    ('/(en|ja)/test_city_tokyo', TestCityHandler),
    ('/tac', TacHandler),
    ('/(en|ja)/coming_soon', ComingSoonHandler),
    ('/ad', TestPageHandler),
], debug=True)
