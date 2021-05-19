#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib, urllib.request
import json
from xml.dom import minidom
from json2html import *


# query from arxiv, using offical query API: https://arxiv.org/help/api/user-manua
config = json.load(open('config.json'))
query = f"http://export.arxiv.org/api/query?search_query=all:{config['subject']}&id_list=&start=0&sortBy=lastUpdatedDate&sortOrder=descending&max_results=30"
data = urllib.request.urlopen(query).read().decode('utf-8')

# parse fetched results
attr_mapping = {'id': 'link', 'name': 'authors'}
map_attr = lambda x: attr_mapping[x] if x in attr_mapping else x

def convert_field(entry):
  new_entry = entry.copy()
  if 'link' in entry:
    new_entry['title'] = f'<a href="{entry['link']}" target="_blank">{entry['title']}</a>'
    new_entry.pop('title')
  return new_entry

entries = []
dom = minidom.parseString(data)
for entry_obj in dom.getElementsByTagName('entry'):
  entry = {}
  for field in config['fields']:
    property_list = entry_obj.getElementsByTagName(field)
    entry[map_attr(field)] = ', '.join(map(lambda x: x.childNodes[0].nodeValue, property_list))
  entry['update'] = '*' if entry_obj.getElementsByTagName('updated')[0].childNodes[0].nodeValue != \
      entry_obj.getElementsByTagName('published')[0].childNodes[0].nodeValue else ' '
  entries.append(convert_field(entry))
 
# print(entries)
table = json2html.convert(json=entries, table_attributes="class=\"table table-bordered table-hover\"", escape=False)
print(table)

with open('./arxiv.html', 'w') as f:
  f.write(table)
  
    







