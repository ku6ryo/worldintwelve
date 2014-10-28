#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2014 The World in Twelve.


import common
import jinja2
import os
import urllib
import webapp2


class Handler(webapp2.RequestHandler):
  def get(self, lang, typ, item):
    is_top = item != None
    if typ == 'cities':
      metas = common.CITY_METAS
      items = common.CITIES
    else:
      if lang == 'ja':
        metas = common.PROJECT_METAS_JA
      else:
        metas = common.PROJECT_METAS_EN
      items = common.PROJECTS

    if is_top:
      frame_template = common.GetTemplate('%s/frame.html' % typ)
      type_template = common.GetTemplate('%s/%s/%s.html' % (typ, lang, item))
      info_template = common.GetTemplate('%s/info_frame.html' % typ)
      info_body = info_template.render({
        'description': type_template.render(),
        'meta': metas[item],
        'item_id': item
       })
      body = frame_template.render({
          'info': info_body,
          'item_id': item,
          'items': [metas[i] for i in items],
          'lang': lang,
      })
      dir_list = [typ, item]
    else:
      frame_template = common.GetTemplate('%s/frame.html' % typ)
      body = frame_template.render({
        'info': '',
        'item_id': '',
        'items': [metas[i] for i in items],
        'lang': lang,
        'is_top': True,
      })
      dir_list = [typ]
    self.response.write(common.WrapWithBaseTemplate(body, lang, dir_list))


app = webapp2.WSGIApplication([
    (r'/(en|ja)/(cities)/*(%s)?' % '|'.join(common.CITIES), Handler),
    (r'/(en|ja)/(projects)/*(%s)?' % '|'.join(common.PROJECTS), Handler),
], debug=True)
