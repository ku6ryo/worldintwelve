#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2014 The World in Twelve.

import webapp2

class Handler(webapp2.RequestHandler):
  def get(self, lang):
    self.response.write('ggg')


app = webapp2.WSGIApplication([
    ('/(en|ja)/p', Handler),
], debug=True)
