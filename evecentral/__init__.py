"""
Very small module to cache EVE Central prices results locally in memory

Also does a lookup of item_name so you don't need to know pesky item IDs
"""
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import requests

EVE_CENTRAL_QUERY="http://api.eve-central.com/api/marketstat?typeid={item}&regionlimit={region}"
FUZZWORKS_QUERY="https://www.fuzzwork.co.uk/api/typeid.php?typename={item}"
JITA_REGION_ID='10000002'

__all__ = ("get_price",)

PRICES = {}
def _price_request(item_id):
    shitxml = requests.get(EVE_CENTRAL_QUERY.format(item=item_id, region=JITA_REGION_ID))
    rootshit = ET.fromstring(shitxml.text)
    item = rootshit[0][0]
    price = {"maxbuy": float(item.find('buy').find('max').text),
            "minsell": float(item.find('sell').find('min').text),
            "cached_at": datetime.utcnow()
    }
    return price

def _get_item_id(item_name):
    resp = requests.get(FUZZWORKS_QUERY.format(item=item_name))
    if resp.status_code != 200:
        raise ItemNotFoundException()
    else:
        return resp.json()['typeID']


def get_price(item_name):
    if item_name in PRICES:
        item = PRICES[item_name]
        if item['cached_at'] + timedelta(hours=1) < datetime.utcnow():
            return item
    item_id = _get_item_id(item_name)
    item = _price_request(item_id)
    PRICES[item_id] = item
    #datetimes are not serializable and the user only cares about the price
    #so return a new dict w/o the cached_at time
    return {
        "maxbuy": item['maxbuy'],
        "minsell": item['minsell']
    }
