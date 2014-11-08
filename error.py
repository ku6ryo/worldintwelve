#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2014 The World in Twelve.

import webapp2


def Handle404(request, response, exception):
  response.set_status(404)

def Handle500(request, response, exception):
  response.set_status(500)
