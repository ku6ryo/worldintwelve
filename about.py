#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2014 The World in Twelve.


import common
import jinja2
import os
import urllib
import webapp2


class Handler(webapp2.RequestHandler):
  def get(self, lang, topic):
    base_template = common.GetTemplate('base.html')
    frame_template = common.GetTemplate('about/frame.html')
    blog_template = common.GetTemplate('about/%s/%s.html' % (lang, topic))
    body = blog_template.render()
    frame = frame_template.render({'body': body, 'lang': lang})
    self.response.write(common.WrapWithBaseTemplate(
        frame, lang, ['about', topic]))


app = webapp2.WSGIApplication([
    webapp2.Route('/ja/about', webapp2.RedirectHandler, defaults={
      '_uri': '/ja/about/wxii', '_code': 301}),
    webapp2.Route('/en/about', webapp2.RedirectHandler, defaults={
      '_uri': '/en/about/wxii', '_code': 301}),
    webapp2.Route('/en/about/', webapp2.RedirectHandler, defaults={
      '_uri': '/en/about/wxii', '_code': 301}),
    webapp2.Route('/ja/about/', webapp2.RedirectHandler, defaults={
      '_uri': '/ja/about/wxii', '_code': 301}),
    (r'/(en|ja)/about/(cities|projects|wxii|faq|rules)', Handler),
], debug=True)
