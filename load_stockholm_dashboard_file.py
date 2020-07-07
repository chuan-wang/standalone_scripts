#!/usr/bin/env/python
"""
*** ARCHIVED *************************************************************
The Stockholm dashboard is no longer shown on the Order Portal
website after the new NGI website was launched in May 2020.
As such, this script is no longer needed. The cron job has been disabled.
Leaving the script here in case it is useful at some point in the future.
Phil Ewels 2020-05-06
**************************************************************************

Load the HTML file as a document programmatically into the web site.
The file is a self-contained HTML file showing the current state of
operations at the Stockholm node of NGI. It is generated by software
external to the OrderPortal system from NGI Stockholm's internal systems.

This script assumes that there already exists a document in the Order Portal
with the given entity name, which it edits.

Per Kraulis 2016-09-09
Modified by Johannes Alneberg
"""

from __future__ import print_function, absolute_import
import requests
import sys
import yaml

API_KEY_HEADER = 'X-OrderPortal-API-key'

if len(sys.argv) != 2:
    raise ValueError('settings filepath argument is required')

with open(sys.argv[1]) as infile:
    settings = yaml.safe_load(infile)

headers = { API_KEY_HEADER: settings['API_KEY'] }

url = settings['TEMPLATE_URL'].format(settings['ENTITY_NAME'])

files = {
    'file': (
        settings['ENTITY_NAME'],
        open(settings['FILEPATH'], 'rb'),
        settings['CONTENT_TYPE']
    )
}

data = {
    'description': settings['DESCRIPTION'],
    'hidden': True
}

response = requests.post(
    url,
    headers = headers,
    data = data,
    files = files
)
response.raise_for_status()