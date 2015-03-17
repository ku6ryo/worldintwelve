#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Copyright 2014 The World in Twelve.


import jinja2
import os
import urllib
import webapp2


JINJA_ENVIRONMENT = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__).replace('handlers', 'templates')),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)


BREADCRUMB_DICT = {
  'sanfrancisco': 'San Francisco',
  'riodejaneiro': 'Rio de Janeiro',
  'family_recipes': 'Family Recipes',
  'whats_beauty': 'What is beauty?',
  'test_city_tokyo': 'TEST CITY: Tokyo',
  'whatis': 'What is Wxii?',
  'project_matrix': 'Project Matrix',
}


CITIES = [
  'sanfrancisco',
  'toronto',
  'newyork',
  'riodejaneiro',
  'london',
  'stockholm',
  'paris',
  'munich',
  'barcelona',
  'istanbul',
  'melbourne',
  'bangkok',
]


CITY_METAS = {
  'tokyo': {
    'id': 'tokyo',
    'label': 'Tokyo',
    'label_ja': u'東京',
    'population': '9,071,577',
    'area': '622.99',
    'urban_population': '37,239,000',
    'urban_area': '8,547',
    'num_districts': '23 Wards',
    'nicknames': '-',
    'month': '-',
    'color': '#565656'
  },
  'bangkok': {
    'id': 'bangkok',
    'label': 'Bangkok',
    'label_ja': u'バンコク',
    'population': '8,280,925',
    'area': '1,568.737',
    'urban_population': '14,565,547',
    'urban_area': '7,761.6',
    'num_districts': '50 Districts, 12 Clusters',
    'nicknames': 'Big Mango, Venice of the East',
    'month': 'Dec, 2015',
    'color': '#ff6d00'
  },
  'barcelona': {
    'id': 'barcelona',
    'label': 'Barcelona',
    'label_ja': u'バルセロナ',
    'population': '1,620,943',
    'area': '101.9',
    'urban_population': '5,375,774',
    'urban_area': '803',
    'num_districts': '10 Districts',
    'nicknames': 'The City of Counts, The City of Gaudi',
    'month': 'Sep, 2015',
    'color': '#AC0D19'
  },
  'istanbul': {
    'id': 'istanbul',
    'label': 'Istanbul',
    'label_ja': u'イスタンブール',
    'population': '14,160,467',
    'area': '5,343',
    'urban_population': '14,160,467',
    'urban_area': '5,343',
    'num_districts': '39 Districts',
    'nicknames': 'The City on Seven Hills, Queen of Cities, City of World\'s Desires',
    'month': 'Oct, 2015',
    'color': '#A3860C'
  },
  'london': {
    'id': 'london',
    'label': 'London',
    'label_ja': u'ロンドン',
    'population': '8,416,535',
    'area': '1,572.15',
    'urban_population': '9,576,000',
    'urban_area': '1,623',
    'num_districts': '33 Local Authorities',
    'nicknames': 'The Square Mile, The (Big) Smoke',
    'month': 'May, 2015',
    'color': '#08B29A'
  },
  'melbourne': {
    'id': 'melbourne',
    'label': 'Melbourne',
    'label_ja': u'メルボルン',
    'population': '116,431',
    'area': '33.7',
    'urban_population': '4,347,955',
    'urban_area': '9,990.5',
    'num_districts': '31 Municipalities',
    'nicknames': 'The Second City',
    'month': 'Nov, 2015',
    'color': '#22ADF2'
  },
  'munich': {
    'id': 'munich',
    'label': 'Munich',
    'label_ja': u'ミュンヘン',
    'population': '1,388,308',
    'area': '310.43',
    'urban_population': '',
    'urban_area': '',
    'num_districts': '25 Boroughs',
    'nicknames': 'World City with Heart',
    'month': 'July, 2015',
    'color': '#F49F08'
  },
  'newyork': {
    'id': 'newyork',
    'label': 'New York',
    'label_ja': u'ニューヨーク',
    'population': '8,405,837',
    'area': '783.84',
    'urban_population': '20,673,000',
    'urban_area': '11,642',
    'num_districts': '5 Boroughs',
    'nicknames': 'The Big Apple, Gotham',
    'month': 'Mar, 2015',
    'color': '#82A81A'
  },
  'paris': {
    'id': 'paris',
    'label': 'Paris',
    'label_ja': u'パリ',
    'population': '2,211,297',
    'area': '105',
    'urban_population': '12,292,895',
    'urban_area': '17,174.4',
    'num_districts': '20 arrondissements',
    'nicknames': 'la Ville Lumiere (City of Lights), City of Love',
    'month': 'Aug, 2015',
    'color': '#F93EA5'
  },
  'riodejaneiro': {
    'id': 'riodejaneiro',
    'label': 'Rio de Janeiro',
    'label_ja': u'リオ デ ジャネイロ',
    'population': '6,429,923',
    'area': '1,200.27',
    'urban_population': '11,616,000',
    'urban_area': '2,020',
    'num_districts': '5 Districts',
    'nicknames': 'Cidade Maravilhosa (Marvelous City)',
    'month': 'Apr, 2015',
    'color': '#457012'
  },
  'sanfrancisco': {
    'id': 'sanfrancisco',
    'label': 'San Francisco',
    'label_ja': u'サンフランシスコ',
    'population': '837,442',
    'area': '600.6',
    'urban_population': '4,516,276',
    'urban_area': '9,128',
    'num_districts': '10 Neighborhoods (Unofficial)',
    'nicknames': 'San Fran, Frisco',
    'month': 'Jan, 2015',
    'color': '#7436C6'
  },
  'stockholm': {
    'id': 'stockholm',
    'label': 'Stockholm',
    'label_ja': u'ストックホルム',
    'population': '905,184',
    'area': '188',
    'urban_population': '2,171,459',
    'urban_area': '6,519',
    'num_districts': '14 Districts (3 Divisions)',
    'nicknames': 'Eken (The Oak)',
    'month': 'Jun, 2015',
    'color': '#1D3C7F'
  },
  'toronto': {
    'id': 'toronto',
    'label': 'Toronto',
    'label_ja': u'トロント',
    'population': '2,615,060',
    'area': '630',
    'urban_population': '5,583,064',
    'urban_area': '7,125',
    'num_districts': '140 Neighborhodds, 6 Districts',
    'nicknames': '-',
    'month': 'Feb, 2015',
    'color': '#6B3E0D'
  }
}


PROJECTS = [
  'musicians',
  'soundscape',
  'treasure_box',
  'twelve_twelve', 
  'whats_beauty', 
  'real_dates', 
  'family_recipes', 
  'micro_guide', 
  'misc', 
  'twelve_questions', 
  'bck', 
  'marketplace'
]


PROJECT_MATRIX_META = {
  'musicians': {
    'is_multiple_pages': True,
    'tokyo': [
      {
        'id': 'looprider',
        'label': 'Loop Rider'
      },
      {
        'id': 'corkbird',
        'label': 'Corkbird'
      },
       {
        'id': 'junkondo',
        'label': 'junkondo'
      },
    ],
    'sanfrancisco': [
      {
        'id': 'thetropics',
        'label': 'The Tropics'
      },
    ],
  },
  'soundscape': {
    'is_multiple_pages': False
  },
  'treasure_box': {
    'is_multiple_pages': False
  },
  'twelve_twelve': {
    'is_multiple_pages': True,
    'sanfrancisco': [
      {
        'id': 'animals',
        'label': 'animals'
      },
      {
        'id': 'books',
        'label': 'books'
      },
    ],
  }, 
  'whats_beauty': {
    'is_multiple_pages': True,
    'tokyo': [
      {
        'id': 'yuko',
        'label': 'Yuko'
      },
      {
        'id': 'saori',
        'label': 'Saori'
      },
      {
        'id': 'nana',
        'label': 'Nana'
      },
    ],
  }, 
  'real_dates': {
  'is_multiple_pages': True,
    'tokyo': [
      {
        'id': 'madoka_roch',
        'label': 'Madoka & Roch'
      },
    ],
  }, 
  'family_recipes': {
    'is_multiple_pages': True,
    'sanfrancisco': [
      {
        'id': 'alexandeve',
        'label': 'Alex and Eve'
      },
      {
        'id': 'brunch',
        'label': 'Brunch'
      },
    ],
  }, 
  'micro_guide': {
    'is_multiple_pages': True,
    'tokyo': [
      {
        'id': 'shigusa',
        'label': 'Shigusa'
      },
      {
        'id': 'meetup',
        'label': 'Meet Up'
      },
      {
        'id': 'slang',
        'label': 'Slang'
      },
      {
        'id': 'ingredients',
        'label': 'Ingredients'
      },
      {
        'id': 'proverbs',
        'label': 'Proverbs'
      },
      {
        'id': 'places',
        'label': 'Places'
      },
    ],
  }, 
  'misc': {
    'is_multiple_pages': False,
  },
  'twelve_questions': {
    'is_multiple_pages': True,
    'tokyo': [
      {
        'id': 'nanako',
        'label': 'Nanako Level'
      },
      {
        'id': 'yamato',
        'label': 'Yamato Watanabe'
      },
      {
        'id': 'onochan',
        'label': 'Ono Shinya'
      },
       {
        'id': 'sayaka',
        'label': 'Sayaka Yamaguchi'
      },
      {
        'id': 'kamiken',
        'label': 'Kamiyama Kentaro'
      },
      {
        'id': 'karly',
        'label': 'Kaori Yagi'
      },
    ],
    'sanfrancisco': [
      {
        'id': 'kai',
        'label': 'Kai Hirota'
      },
       {
        'id': 'stong',
        'label': 'Stephanie Tong'
      },
       {
        'id': 'geoff',
        'label': 'Geoff Taylor'
      },
        {
        'id': 'aspen',
        'label': 'Aspen Jordan'
      },
    ],
  }, 
  'bck': {
  'is_multiple_pages': False,
  }, 
  'marketplace': {
  'is_multiple_pages': False,
  }
}


PROJECT_METAS_EN = {
  'musicians': {
    'id': 'musicians',
    'label': 'Artists / Musicians',
    'metas': ['Base Format: Music', 'Songs: 12', 'Length: --', 'Participants: 12 bands / artists'],
    'description': u'Make music. Play music. Live music. I know what <i>I’m</i> becoming in my next life.'
  },
  'bck': {
    'id': 'bck',
    'label': 'Blind Cheap Kudos',
    'metas': ['Base Format: Music', 'Overview Format: Movie', 'Length: --', 'Songs: 1', 'Participants: --'],
    'description': u'Welcome to the world of Blind Cheap Kudos. Don’t be scared, take a look!!'
  },
  'whats_beauty': {
      'id': 'whats_beauty',
      'label': 'What is beauty?',
      'metas': ['Base Format: Movie', 'Episodes: 12', 'Length: 5 min',
'Participants: 4 people for each city'],
    'description': u'What is beauty? Is it personal? Is it relative? Is there true, universal beauty? These are quesions human kind has held, ever since existence. Let’s see what people have to say.'
  },
  'real_dates': {
      'id': 'real_dates',
      'label': 'Real Dates',
      'metas': ['Base Format: Movie', 'Episodes: 12',
          'Length: 2 min 24 sec', 'Participants: 12 couples(total: 24 people)'],
      'description': u'We laugh, we fight, we eat, we cry, we sleep, we smile. These are the days we live together.'
  },
  'family_recipes': {
      'id': 'family_recipes',
      'label': 'Family Recipes',
      'metas': ['Base Format: Movie', 'Overview Format: Photos / Articles',
      'Episodes: 1', 'Participants: --'],
      'description': u'\"Mine would be home made pecan pie and lemon bars\" (Robin, Tallahassee). Let’s see what everyone grew up eating!!'
  },
  'micro_guide': {
      'id': 'micro_guide',
      'label': 'Micro Guide',
      'metas': ['Base Format: Illustrations / Articles', 'Overview Format: Movie', 'Participants: --'],
      'description': u'Practically none of the information you\'ll read here will be of any use. And thats exactly why you should check it out.'
  },
  'soundscape': {
      'id': 'soundscape',
      'label': 'Soundscape',
      'metas': ['Base Fromat: Music / Movie', 'Songs: 12', 'Length: --', 'Participants: --'],
      'description': u'Close your eyes. Let your imagination roam. The world is surrounded with beautiful sounds.'
  },
  'misc': {
      'id': 'misc',
      'label': 'Misc',
      'metas': ['Base Format: Photos / Articles', 'Overview Format: Movie',
      'Episodes: 1', 'Participants: --'],
      'description': u'Who knows what’s going to happen in life? That\'s why we have The Miscellaneous.'
  },
  'treasure_box': {
      'id': 'treasure_box',
      'label': 'Treasure Box',
      'metas': ['Base Format: Photos / Articles', 'Sub-format: Movie',
      'Episodes: 1', 'Participants: Leo + 2~3'],
      'description': u'A battle using treasures from each city? Get me my parrot and pirates hat!!'
  },
  'twelve_questions': {
      'id': 'twelve_questions',
      'label': '12 Questions',
      'metas': ['Base Format: Photos / Articles', 'Overview Format: Movie',
      'Episodes: 12', 'Participants: 12'],
      'description': u'12 questions. 12 cities. 144 people, all living different lives.'
  },
  'marketplace': {
      'id': 'marketplace',
      'label': 'Marketplace',
      'metas': ['Base Format: Photos / Web', 'Participants: 12 groups at least'],
      'description': u'Buy, sell, sell, buy. Yep, the World in Twelve has now officially joined capitalistic society.'
  },
  'twelve_twelve': {
      'id': 'twelve_twelve',
      'label': 'Twelve x Twelve',
      'metas': [],
      'description': u'A mini-project truly depicting the essence of the number 12… You have any wacky ideas for combinations? Let your voice be heard!!'
  }
}


PROJECT_METAS_JA = {
  'musicians': {
      'id': 'musicians',
      'label': u'アーティスト・ミュージシャン',
      'metas': [u'基本フォーマット：音楽', u'曲数：12曲', u'尺：−−', u'参加人数：12組（バンド・アーティスト）'],
      'description': u'本気で作り、本気で奏で、本気で唄う。そんな人生に憧れます。'
  },
  'bck': {
      'id': 'bck',
      'label': 'Blind Cheap Kudos',
      'metas': [u'基本フォーマット：音楽', u'概要フォーマット：映像', u'尺：−−',
          u'曲数：1', u'参加人数：--'],
      'description': u'和名「盲目な安い賞賛」。本気でふざけよ。ただそれだけ。'
  },
  'whats_beauty': {
      'id': 'whats_beauty',
      'label': u'美とは？',
      'metas': [u'基本フォーマット：映像', u'エピソード数：12本', u'尺：５分', u'参加人数：各都市４人'],
      'description': u'人類の永遠の質問…美とはなんぞや？普遍的なものなのか、人それぞれなのか。「美」の概念に迫ります！'
  },
  'real_dates': {
      'id': 'real_dates',
      'label': u'リアルデート',
      'metas': [u'基本フォーマット：映像', u'エピソード数：12本',
          u'尺：2分24秒', u'参加人数：カップル12組（計24人）'],
      'description': u'笑いあって、手をつないで、そばにいて、喧嘩したあとは仲直りする。そんな日々がありました。'
  },
  'family_recipes': {
      'id': 'family_recipes',
      'label': u'家庭の味',
      'metas': [u'基本フォーマット：映像', u'概要フォーマット：写真・文章',
      u'エピソード数：1', u'参加人数：--'],
      'description': u'「僕は唐揚げ、卵焼き、そしておかかと梅のおにぎり」（S君・25歳）。みんなの家庭の味、見てみましょ。'
  },
  'micro_guide': {
      'id': 'micro_guide',
      'label': u'細かすぎて伝わらないトリセツ',
      'metas': [u'基本フォーマット：イラスト・文章', u'概要フォーマット：映像',
          u'参加人数：−−'],
      'description': u'ここにある情報のはほとんどはなんの役にも立たないですけど、だからこそクリック！ここをクリック！'
  },
  'soundscape': {
      'id': 'soundscape',
      'label': u'サウンドスケープ',
      'metas': [u'基本フォーマット：音楽・映像', u'曲数：12曲', u'尺：−−',
      u'参加人数：−−'],
      'description': u'耳を澄ませてごらん、世界は音に満ちあふれている。ってだれかカッコいい人が言ってた気がする。'
  },
  'misc': {
      'id': 'misc',
      'label': u'ザ・その時決める',
      'metas': [u'基本フォーマット：写真・文章', u'概要フォーマット：映像',
          u'エピソード数：1', u'参加人数：--'],
      'description': u'そのとき、そのとき、決めるのだ。楽しく、楽しく、生きるのだ。'
  },
  'treasure_box': {
      'id': 'treasure_box',
      'label': u'宝箱バトル',
      'metas': [u'基本フォーマット：写真・文章', u'サブフォーマット：映像',
      u'エピソード数：１回', u'参加人数：自分＋2~3人'],
      'description': u'その都市その都市の「ひとつなぎの大秘ほ．．．」なんでもありません笑'
  },
  'twelve_questions': {
      'id': 'twelve_questions',
      'label': u'１２の質問',
      'metas': [u'基本フォーマット：写真・文章', u'概要フォーマット：映像',
      u'エピソード数：12回', u'参加人数：12人'],
      'description': u'12の質問、12の都市。144人の人生観、ここにあり！'
  },
  'marketplace': {
      'id': 'marketplace',
      'label': u'マーケット',
      'metas': [u'基本フォーマット：写真・ウェブ', u'尺：−−',
          u'参加人数：最低12組'],
      'description': u'買って、売る。売って、買う。資本主義社会の輪廻の一部となりました。'
  },
  'twelve_twelve': {
      'id': 'twelve_twelve',
      'label': u'Twelve x Twelve',
      'metas': [],
      'description':
      u'12という概念をこれでもか！って込めました！（笑）みんなもいい組み合わせがあったら教えてね！'
  }
}


def GetTemplate(path):
  return JINJA_ENVIRONMENT.get_template(path)


def existTemplate(path):
  return path in JINJA_ENVIRONMENT.list_templates()


def WrapWithBaseTemplate(content, lang, dirs):
  base_template = GetTemplate('base.html')
  breadcrumbs = []
  for i in range(len(dirs)):
    d = dirs[i]
    breadcrumbs.append({
      'href': '/'.join(dirs[:i+1]),
      'label': BREADCRUMB_DICT[d] if d in BREADCRUMB_DICT else d
    })

  return base_template.render({
    'content': content,
    'breadcrumbs': breadcrumbs,
    'lang': lang
  })
