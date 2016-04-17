#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2014 The World in Twelve.


import common
import jinja2
import not_found
import os
import urllib
import webapp2
import logging



class Handler(webapp2.RequestHandler):
  def get(self, lang, project_id, city_id):

    metas = common.CITY_METAS
    items = common.CITIES

    cities = ['tokyo']
    cities.extend(common.CITIES)
    projects = common.PROJECTS

    is_multiple_pages = common.PROJECT_MATRIX_META[project_id]['is_multiple_pages']
    project_matrix_meta = common.PROJECT_MATRIX_META[project_id]

    pages_meta = []
    body = ''
    if is_multiple_pages and city_id in project_matrix_meta:
      pages_meta = project_matrix_meta[city_id]
      for page in pages_meta:
        content_template_path = 'matrix/%s/%s/%s_%s.html' % (
            lang, city_id, project_id, page['id'])
        if common.existTemplate(content_template_path):
          body += common.GetTemplate(content_template_path).render({
            'id': page['id']
          })
    else:
      content_template_path = 'matrix/%s/%s/%s.html' % (
          lang, city_id, project_id)
      if common.existTemplate(content_template_path):
        body += common.GetTemplate(content_template_path).render()

    has_content = True
    if body is '':
      body = common.GetTemplate('coming_soon.html').render()
      has_content = False

    frame_template = common.GetTemplate('matrix/single_project_frame.html')

    frame = frame_template.render({
      'body': body,
      'lang': lang,
      'item_id': city_id,
      'items': [metas[i] for i in items],
      'is_multiple_pages': is_multiple_pages,
      'pages_meta': pages_meta,
      'has_content': has_content,
      'city_id': city_id,
      'project_id': project_id,
    })
    self.response.write(common.WrapWithBaseTemplate(
        frame, lang, [project_id]))


app = webapp2.WSGIApplication([
  webapp2.Route(r'/<lang:>/<project_id:>/<city_id:>', handler=Handler),
], debug=True)
