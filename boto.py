#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 17:48:25 2021

@author: nishi
"""

from boto.s3.connection import S3Connection
conn = S3Connection ('AKIA2IKGRGRRGMMHMXC6','Lglg/YOlCXWsWqY0N3m9qLLQj3opX2b2ov1L8fGM')

rs = conn.get_all_buckets()
for b in rs:
        print (b.name)
