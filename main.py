#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import urllib

import jinja2
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


CITIES = [
        {'id': 'sanfrancisco', 'label': 'San Francisco'},
        {'id': 'toronto', 'label': 'Toronto'},
        {'id': 'newyork', 'label': 'New York'},
        {'id': 'riodejaneiro', 'label': 'Rio de Janeiro'},
        {'id': 'london', 'label': 'London'},
        {'id': 'stockholm', 'label': 'Stockholm'},
        {'id': 'munich', 'label': 'Munich'},
        {'id': 'paris', 'label': 'Paris'},
        {'id': 'barcelona', 'label': 'Barcelona'},
        {'id': 'istanbul', 'label': 'Istanbul'},
        {'id': 'bangkok', 'label': 'Bangkok'},
        {'id': 'melbourne', 'label': 'Melbourne'},
]

CITY_METAS = {
  'tokyo': {
    'label': 'Tokyo',
    'population': '9,071,577',
    'area': '622.99',
    'urban_population': '37,239,000',
    'urban_area': '8,547',
    'num_districts': '23 Wards',
    'nicknames': '-',
    'month': '-'
  },
  'bangkok': {
    'label': 'Bandkok',
    'population': '8,280,925',
    'area': '1,568.737',
    'urban_population': '14,565,547',
    'urban_area': '7,761.6',
    'num_districts': '50 Districts, 12 Clusters',
    'nicknames': 'Big Mango, Venice of the East',
    'month': 'Oct, 2015'
  },
  'barcelona': {
    'label': 'Barcelona',
    'population': '1,620,943',
    'area': '101.9',
    'urban_population': '5,375,774',
    'urban_area': '803',
    'num_districts': '10 Districts',
    'nicknames': 'The City of Counts, The City of Gaudi',
    'month': 'Aug, 2015'
  },
  'istanbul': {
    'label': 'Istanbul',
    'population': '14,160,467',
    'area': '5,343',
    'urban_population': '14,160,467',
    'urban_area': '5,343',
    'num_districts': '39 Districts',
    'nicknames': 'The City on Seven Hills, Queen of Cities, City of World\'s Desires',
    'month': 'Sep, 2015'
  },
  'london': {
    'label': 'London',
    'population': '8,416,535',
    'area': '1,572.15',
    'urban_population': '9,576,000',
    'urban_area': '1,623',
    'num_districts': '33 Local Authorities',
    'nicknames': 'The Square Mile, The (Big) Smoke',
    'month': 'Apr, 2015'
  },
  'melbourne': {
    'label': 'Melbourne',
    'population': '116,431',
    'area': '33.7',
    'urban_population': '4,347,955',
    'urban_area': '9,990.5',
    'num_districts': '31 Municipalities',
    'nicknames': 'The Second City',
    'month': 'Nov, 2015'
  },
  'munich': {
    'label': 'Munich',
    'population': '1,388,308',
    'area': '310.43',
    'urban_population': '',
    'urban_area': '',
    'num_districts': '25 Boroughs',
    'nicknames': 'World City with Heart',
    'month': 'Jun, 2015'
  },
  'newyork': {
    'label': 'New York',
    'population': '8,405,837',
    'area': '783.84',
    'urban_population': '20,673,000',
    'urban_area': '11,642',
    'num_districts': '5 Boroughs',
    'nicknames': 'The Big Apple, Gotham',
    'month': 'Feb, 2015'
  },
  'paris': {
    'label': 'Paris',
    'population': '2,211,297',
    'area': '105',
    'urban_population': '12,292,895',
    'urban_area': '17,174.4',
    'num_districts': '20 arrondissements',
    'nicknames': 'la Ville Lumiere (City of Lights), City of Love',
    'month': 'Jul, 2015'
  },
  'riodejaneiro': {
    'label': 'Rio de Janeiro',
    'population': '6,429,923',
    'area': '1,200.27',
    'urban_population': '11,616,000',
    'urban_area': '2,020',
    'num_districts': '5 Districts',
    'nicknames': 'Cidade Maravilhosa (Marvelous City)',
    'month': 'Mar, 2015'
  },
  'sanfrancisco': {
    'label': 'San Francisco',
    'population': '837,442',
    'area': '600.6',
    'urban_population': '4,516,276',
    'urban_area': '9,128',
    'num_districts': '10 Neighborhoods (Unofficial)',
    'nicknames': 'San Fran, Frisco',
    'month': 'Dec, 2014'
  },
  'stockholm': {
    'label': 'Stockholm',
    'population': '905,184',
    'area': '188',
    'urban_population': '2,171,459',
    'urban_area': '6,519',
    'num_districts': '14 Districts (3 Divisions)',
    'nicknames': 'Eken (The Oak)',
    'month': 'May, 2015'
  },
  'toronto': {
    'label': 'Toronto',
    'population': '2,615,060',
    'area': '630',
    'urban_population': '5,583,064',
    'urban_area': '7,125',
    'num_districts': '140 Neighborhodds, 6 Districts',
    'nicknames': '-',
    'month': 'Jan, 2015'
  }
}


PROJECTS = [
  {'id': 'musicians', 'label': 'Musicians'},
  {'id': 'soundscape', 'label': 'Soundscape'},
  {'id': 'treasure_box', 'label': 'Treasure Box'},
  {'id': 'live', 'label': 'Live'},
  {'id': 'dates1', 'label': 'Dates Part 1'},
  {'id': 'dates2', 'label': 'Dates Part 2'},
  {'id': 'grandma_cooking', 'label': 'Grandma\'s Cooking'},
  {'id': 'micro_guide', 'label': 'Micro Guide'},
  {'id': 'misc', 'label': 'Misc'},
  {'id': 'twelve_questions', 'label': '12 Questions'},
  {'id': 'bck', 'label': 'BCK'},
  {'id': 'marketplace', 'label': 'Market Place'}
]

PROJECT_METAS = {
  'musicians': {
      'label': u'アーティスト・ミュージシャン',
      'metas': [u'基本フォーマット：音楽', u'曲数：12曲', u'尺：−−', u'参加人数：12組（バンド・アーティスト）']
  },
  'bck': {
      'label': 'Blind Cheap Kudos',
      'metas': [u'基本フォーマット：音楽', u'概要フォーマット：映像', u'尺：−−',
          u'曲数：1', u'参加人数：--']
  },
  'dates1': {
      'label': u'デート パート １',
      'metas': [u'基本フォーマット：映像', u'エピソード数：12本', u'尺：５分', u'参加人数：各都市４人']
  },
  'dates2': {
      'label': u'デート パート 2',
      'metas': [u'基本フォーマット：映像', u'エピソード数：12本',
          u'尺：2分24秒', u'参加人数：カップル12組（計24人）']
  },
  'grandma_cooking': {
      'label': u'おばあちゃんの手料理',
      'metas': [u'基本フォーマット：映像', u'概要フォーマット：写真・文章',
      u'エピソード数：1', u'参加人数：--']
  },
  'micro_guide': {
      'label': u'細かすぎて伝わらないトリセツ',
      'metas': [u'基本フォーマット：イラスト・文章', u'概要フォーマット：映像',
          u'参加人数：−−']
  },
  'soundscape': {
      'label': u'サウンドスケープ',
      'metas': [u'基本フォーマット：音楽・音像', u'曲数：12曲', u'尺：−−',
      u'参加人数：−−']
  },
  'misc': {
      'label': u'ザ・その時決める',
      'metas': [u'基本フォーマット：写真・文章', u'概要フォーマット：映像',
          u'エピソード数：1', u'参加人数：--']
  },
  'treasure_box': {
      'label': u'宝箱バトル',
      'metas': [u'基本フォーマット：写真・文章', u'サブフォーマット：映像',
      u'エピソード数：１回', u'参加人数：自分＋2~3人']
  },
  'twelve_questions': {
      'label': u'１２の質問',
      'metas': [u'基本フォーマット：写真・文章', u'概要フォーマット：映像',
      u'エピソード数：12回', u'参加人数：12人']
  },
  'marketplace': {
      'label': u'マーケット',
      'metas': [u'基本フォーマット：写真・ウェブ', u'尺：−−',
          u'参加人数：最低12組']
  },
  'live': {
      'label': u'ライブ！',
      'metas': []
  }
}


class TopHandler(webapp2.RequestHandler):
    def get(self):
        base_template = JINJA_ENVIRONMENT.get_template('templates/base.html')
        top_template = JINJA_ENVIRONMENT.get_template('templates/top.html')
        cities = [{
            'id': 'tokyo', 'label': 'Tokyo'
        }]
        cities.extend(CITIES)
        body = top_template.render({'cities': cities})
        self.response.write(base_template.render({'body': body}))


class CitiesHandler(webapp2.RequestHandler):
    def get(self, city):
        base_template = JINJA_ENVIRONMENT.get_template('templates/base.html')
        if city != '':
            frame_template = JINJA_ENVIRONMENT.get_template('templates/cities/frame.html')
            city_template = JINJA_ENVIRONMENT.get_template('templates/cities/%s.html' % city)
            city_body = city_template.render()
            info_template = JINJA_ENVIRONMENT.get_template('templates/cities/info_frame.html')
            info_body = info_template.render({
              'description': city_body,
              'meta': CITY_METAS[city],
              'city_id': city
            })
            body = frame_template.render({
                'info': info_body,
                'city_id': city,
                'cities': CITIES,
            })
            dir_list = ['cities', city]
        else:
            cities_template = JINJA_ENVIRONMENT.get_template('templates/cities.html')
            body = cities_template.render()
            dir_list = ['cities']
        self.response.write(base_template.render({
            'body': body, 'dir_list': dir_list}))


class ProjectsHandler(webapp2.RequestHandler):
  def get(self, project):
    print '|'.join([p['id'] for p in PROJECTS])
    is_projcet_top = project != ''
    base_template = JINJA_ENVIRONMENT.get_template('templates/base.html')
    frame_template = JINJA_ENVIRONMENT.get_template('templates/projects/frame.html')
    project_template = JINJA_ENVIRONMENT.get_template('templates/projects/%s.html' % project)
    project_body = project_template.render()
    frame_body = frame_template.render({
      'project_id': project,
      'projects': PROJECTS,
      'description': project_body,
      'meta': PROJECT_METAS[project]
    })
    dir_list = ['projects', project]
    self.response.write(base_template.render({
        'body': frame_body,
        'dir_list': dir_list
    }))

class AboutHandler(webapp2.RequestHandler):
    def get(self, topic):
        base_template = JINJA_ENVIRONMENT.get_template('templates/base.html')
        frame_template = JINJA_ENVIRONMENT.get_template('templates/about/frame.html')
        blog_template = JINJA_ENVIRONMENT.get_template(
            'templates/about/' + topic + '.html')
        body = blog_template.render()
        frame = frame_template.render({'body': body})
        self.response.write(base_template.render({
          'body': frame,
          'dir_list': ['about', topic]
        }))

class PeopleHandler(webapp2.RequestHandler):
    def get(self):
        base_template = JINJA_ENVIRONMENT.get_template('templates/base.html')
        people_template = JINJA_ENVIRONMENT.get_template('templates/people.html')
        people_body = people_template.render()
        self.response.write(base_template.render({
            'body': people_body,
            'dir_list': ['people']
        }))

class SponsorsHandler(webapp2.RequestHandler):
    def get(self):
        base_template = JINJA_ENVIRONMENT.get_template('templates/base.html')
        sponsors_template = JINJA_ENVIRONMENT.get_template('templates/sponsors.html')
        sponsors_body = sponsors_template.render()
        self.response.write(base_template.render({
            'body': sponsors_body,
            'dir_list': ['sponsors']
        }))

class TestCityHandler(webapp2.RequestHandler):
    def get(self):
        base_template = JINJA_ENVIRONMENT.get_template('templates/base.html')
        test_city_template = JINJA_ENVIRONMENT.get_template(
          'templates/cities/test_city_tokyo.html')
        info_template = JINJA_ENVIRONMENT.get_template('templates/cities/info_frame.html')
        tokyo_template = JINJA_ENVIRONMENT.get_template('templates/cities/tokyo.html')
        info = info_template.render({
          'description': tokyo_template.render(),
          'meta': CITY_METAS['tokyo'],
          'city_id': 'tokyo',
          'city_label': 'Tokyo'
        })
        body = test_city_template.render({
          'info': info
        })
        self.response.write(base_template.render({
            'body': body,
            'dir_list': ['test_city_tokyo']
        }))


app = webapp2.WSGIApplication([
    ('/', TopHandler),
    webapp2.Route(r'/about', webapp2.RedirectHandler, defaults={'_uri':
        '/about/wxii', '_code': 301}),
    webapp2.Route(r'/about/', webapp2.RedirectHandler, defaults={'_uri':
        '/about/wxii', '_code': 301}),
    (r'/about/(cities|projects|wxii|faq|rules)', AboutHandler),
    webapp2.Route(r'/cities', webapp2.RedirectHandler, defaults={'_uri':
        '/cities/sanfrancisco', '_code': 301}),
    webapp2.Route(r'/cities/', webapp2.RedirectHandler, defaults={'_uri':
        '/cities/sanfrancisco', '_code': 301}),
    (r'/cities/(%s)' % '|'.join([city['id'] for city in CITIES]), CitiesHandler),
    webapp2.Route(r'/projects', webapp2.RedirectHandler, defaults={'_uri':
        '/projects/musicians', '_code': 301}),
    webapp2.Route(r'/projects/', webapp2.RedirectHandler, defaults={'_uri':
        '/projects/musicians', '_code': 301}),
    (r'/projects/(%s)' % '|'.join([project['id'] for project in PROJECTS]), ProjectsHandler),
    ('/people', PeopleHandler),
    ('/sponsors', SponsorsHandler),
    ('/test_city_tokyo', TestCityHandler),
    (r'/cities/tokyo', TestCityHandler),
], debug=True)
