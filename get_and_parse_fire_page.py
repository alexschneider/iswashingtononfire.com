import requests
import xmltodict
import time
import sys

FIRE_PAGE_URL = 'https://gacc.nifc.gov/nwcc/assets/xml/active_fires.xml'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
CACHE_LIFETIME_IN_SECONDS = 5

updated = 0
current_fires = None

def _get_fire_xml():
    r = requests.get(FIRE_PAGE_URL, headers=HEADERS)
    r.raise_for_status()
    if r.text[0] == u'\ufeff':
        r.encoding = 'utf-8-sig' # Strips BOM (\ufeff causes problems)
    return r.text

def _get_fire_dict():
    fires = xmltodict.parse(_get_fire_xml())
    date = fires['fires']['date']
    fires = [x for x in fires['fires']['fire'] if x['incident_number'].startswith('WA')]
    return {'date': date, 'fires': fires}

def get_fire_dict():
    global updated
    global current_fires
    current_time = time.time()
    if updated + CACHE_LIFETIME_IN_SECONDS < current_time:
        current_fires = _get_fire_dict()
        updated = current_time
    return current_fires