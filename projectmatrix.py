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
    logging.info('/(en|ja)/project_results/(%s)_x_(%s)' % ('|'.join(common.CITIES), '|'.join(common.PROJECTS)))

    cities = common.CITIES;
    projects = common.PROJECTS;

    p_city_id = cities[cities.index(city) - 1] if cities.index(city) > 0 else '';
    c_city_id = city
    n_city_id = cities[cities.index(city) + 1] if cities.index(city) < len(cities) - 1 else '';

    p_project_id = projects[projects.index(project) - 1] if projects.index(project) > 0 else '';
    c_project_id = project
    n_project_id = projects[projects.index(project) + 1] if projects.index(project) < len(projects) - 1 else '';

    p_city_meta = common.CITY_METAS[p_city_id] if p_city_id else {};
    c_city_meta = common.CITY_METAS[c_city_id] if c_city_id else {};
    n_city_meta = common.CITY_METAS[n_city_id] if n_city_id else {};

    p_project_meta = common.PROJECT_METAS_EN[p_project_id] if p_project_id else {};
    c_project_meta = common.PROJECT_METAS_EN[c_project_id] if c_project_id else {};
    n_project_meta = common.PROJECT_METAS_EN[n_project_id] if n_project_id else {};

    base_template = common.GetTemplate('base.html')
    frame_template = common.GetTemplate('project_matrix/frame.html')
    content_template = common.GetTemplate('project_matrix/frame.html')
    body = ''#content_template.render()
    frame = frame_template.render({
      'body': body,
      'lang': lang,
      'p_city_meta': p_city_meta,
      'c_city_meta': c_city_meta,
      'n_city_meta': n_city_meta,
      'p_project_meta': p_project_meta,
      'c_project_meta': c_project_meta,
      'n_project_meta': n_project_meta
    })
    self.response.write(common.WrapWithBaseTemplate(
        frame, lang, ['project_matrix']))


app = webapp2.WSGIApplication([
    webapp2.Route(r'/<lang:>/project_matrix/<city:>_x_<project:>', handler=Handler),
    webapp2.Route(r'/<lang:>/project_matrix/.*', handler=not_found.Handler),
], debug=True)
