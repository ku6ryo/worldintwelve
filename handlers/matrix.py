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
  def get(self, lang, city, project):

    cities = ['tokyo']
    cities.extend(common.CITIES)
    projects = common.PROJECTS

    p_city_id = cities[cities.index(city) - 1] if cities.index(city) > 0 else ''
    c_city_id = city
    n_city_id = cities[cities.index(city) + 1] if cities.index(city) < len(cities) - 1 else ''

    p_project_id = projects[projects.index(project) - 1] if projects.index(project) > 0 else ''
    c_project_id = project
    n_project_id = projects[projects.index(project) + 1] if projects.index(project) < len(projects) - 1 else ''

    p_city_meta = common.CITY_METAS[p_city_id] if p_city_id else {}
    c_city_meta = common.CITY_METAS[c_city_id] if c_city_id else {}
    n_city_meta = common.CITY_METAS[n_city_id] if n_city_id else {}

    p_project_meta = common.PROJECT_METAS_EN[p_project_id] if p_project_id else {}
    c_project_meta = common.PROJECT_METAS_EN[c_project_id] if c_project_id else {}
    n_project_meta = common.PROJECT_METAS_EN[n_project_id] if n_project_id else {}

    is_multiple_pages = common.PROJECT_MATRIX_META[c_project_id][
        'is_multiple_pages']
    project_matrix_meta = common.PROJECT_MATRIX_META[c_project_id]

    pages_meta = []
    body = ''
    if is_multiple_pages and c_city_id in project_matrix_meta:
      pages_meta = project_matrix_meta[c_city_id]
      for page in pages_meta:
        content_template_path = 'matrix/%s/%s/%s_%s.html' % (
            lang, c_city_id, c_project_id, page['id'])
        if common.existTemplate(content_template_path):
          body += common.GetTemplate(content_template_path).render({
            'id': page['id']
          })
    else:
      content_template_path = 'matrix/%s/%s/%s.html' % (
          lang, c_city_id, c_project_id)
      if common.existTemplate(content_template_path):
        body += common.GetTemplate(content_template_path).render()

    # Creates grid data.
    _cities = [c for c in common.CITIES]
    _cities.append('tokyo')

    grid_data = {}
    for project in common.PROJECTS:
      project_data = {}
      for city in _cities:
        project_data[city] = False
      grid_data[project] = project_data

    for project in common.PROJECT_MATRIX_META:

      project_meta = common.PROJECT_MATRIX_META[project]
      for city in _cities:
        content_template_path = 'matrix/%s/%s/%s.html' % (lang, city, project)
        # Ignores other key like is_multiple_pages.
        if city in project_meta:
          grid_data[project][city] = True



    has_content = True
    if body is '':
      body = common.GetTemplate('coming_soon.html').render()
      has_content = False

    base_template = common.GetTemplate('base.html')
    frame_template = common.GetTemplate('matrix/frame.html')

    frame = frame_template.render({
      'body': body,
      'lang': lang,
      'p_city_meta': p_city_meta,
      'c_city_meta': c_city_meta,
      'n_city_meta': n_city_meta,
      'p_project_meta': p_project_meta,
      'c_project_meta': c_project_meta,
      'n_project_meta': n_project_meta,
      'is_multiple_pages': is_multiple_pages,
      'pages_meta': pages_meta,
      'has_content': has_content,
      'grid_data': grid_data,
      'cities': _cities,
      'projects': common.PROJECTS,
    })
    self.response.write(common.WrapWithBaseTemplate(
        frame, lang, ['project_matrix']))


app = webapp2.WSGIApplication([
  webapp2.Route(r'/<lang:>/matrix/<city:>_x_<project:>', handler=Handler),
  webapp2.Route(r'/<lang:>/matrix/.*', handler=not_found.Handler),
], debug=True)
