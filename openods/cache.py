import logging
import urllib.parse
from flask_cacheify import init_cacheify

from openods import app
from flask import request, g

cache = init_cacheify(app)


def generate_cache_key():

    logger = logging.getLogger(__name__)

    args = request.args
    key = request.path + '?' + urllib.parse.urlencode([
        (k, v) for k in sorted(args) for v in sorted(args.getlist(k))
    ])

    logger.debug(str.format('requestId="{0}"|cacheKey={1}|', g.request_id, key))

    return key
