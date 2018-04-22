#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 luna <luna@moon>
#
# Distributed under terms of the MIT license.

"""
Catches webhookx for comands
"""

import web
import json

urls = ('/.*', 'hooks')
app = web.application(urls, globals())

class hooks:
    def POST(self):
        data = web.data()
        print(data)
        return 'OK'

if __name__ == '__main__':
    app.run()
