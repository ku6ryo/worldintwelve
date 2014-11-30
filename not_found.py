#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2014 The World in Twelve.

import common
import jinja2
import webapp2


class Handler(webapp2.RequestHandler):
  def get(self, lang='en'):
    language = lang if lang in ('en', 'ja') else 'en'
    base_template = common.GetTemplate('base.html')
    template = common.GetTemplate('not_found.html')
    body = template.render()
    self.response.write(common.WrapWithBaseTemplate(body, language, ['not_found']))


app = webapp2.WSGIApplication([
    webapp2.Route(r'/<lang:>/<:.*>', handler=Handler),
    webapp2.Route(r'/<lang:>', handler=Handler),
], debug=True)
