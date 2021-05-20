#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib, urllib.request
import json
import re
import os
from datetime import datetime, date, timedelta
from xml.dom import minidom
from json2html import *

# query from arxiv, using offical query API: https://arxiv.org/help/api/user-manual
config = json.load(open('config.json'))
subject = config['subject']
highlights = config['highlights']
max_results = config['max_results']
root_subject = subject.split('.')[0]

current_date = os.getenv("DATE")

def start_date():
  today = datetime.strptime(current_date, '%Y-%m-%d')
  if today.weekday() == 1:
    return (today + timedelta(days = -4)).strftime("%Y-%m-%d")
  else:
    return (today + timedelta(days = -2)).strftime("%Y-%m-%d")
start = start_date()

print(start, current_date)

# query = f"http://export.arxiv.org/api/query?search_query=all:{subject}&id_list=&start=0&sortBy=lastUpdatedDate&sortOrder=descending&max_results={max_results}"
query = f"http://export.arxiv.org/oai2?verb=ListRecords&from={start}&until={current_date}&metadataPrefix=arXivRaw&set={root_subject}"

data = urllib.request.urlopen(query).read().decode('utf-8')

def parse_authors(entry_obj):
  return entry_obj.getElementsByTagName('authors')[0].firstChild.nodeValue

def parse_title(entry_obj):
  title = entry_obj.getElementsByTagName('title')[0].firstChild.nodeValue
  return re.sub(r'\n\s+', ' ', title).strip()

def parse_categories(entry_obj):
  return entry_obj.getElementsByTagName("categories")[0].firstChild.nodeValue

def parse_id(entry_obj):
  return entry_obj.getElementsByTagName("id")[0].firstChild.nodeValue
  
def convert_field(entry):
  title = entry['title']
  for highlight in config['highlights']:
    title = title.replace(highlight, f'<font color="#d00000"><b>{highlight}</b></font>')
  entry['title'] = title
  id = entry['id']
  entry['id'] = f'<a href="https://arxiv.org/abs/{id}" target="_blank">{id}</a>'
  return entry

def check_sub_date(entry_obj):
  versions = entry_obj.getElementsByTagName("version")
  for version in versions:
    if version.getAttribute('version') == "v1":
      sub_date = version.getElementsByTagName("date")[0].firstChild.nodeValue
  sub_date = datetime.strptime(sub_date, "%a, %d %b %Y %H:%M:%S GMT")
  return sub_date >= start

def parse_updated(entry_obj):
  return len(entry_obj.getElementsByTagName('version')) > 1

entries = []
dom = minidom.parseString(data)
for entry_obj in dom.getElementsByTagName('record'):
  if subject not in parse_categories(entry_obj):
    continue
  entry = {}
  entry['title'] = parse_title(entry_obj)
  entry['authors'] = parse_authors(entry_obj)
  entry['id'] = parse_id(entry_obj)
  if not parse_updated(entry_obj) and check_sub_date((entry_obj):
    entries.append(convert_field(entry))

table = json2html.convert(json=entries, table_attributes="class=\"table table-bordered table-hover\"", escape=False)
print(table)

with open('./arxiv.html', 'w') as f:
  f.write(table)
  
    







