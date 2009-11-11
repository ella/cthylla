__all__ = ("get_buildmaster_config",)

import logging
import urllib2

from pickle import loads

REALM = "buildmaster"

def get_buildmaster_config(uri, username, password):
    auth_handler = urllib2.HTTPDigestAuthHandler()
    auth_handler.add_password(REALM, uri, username, password)
    opener = urllib2.build_opener(auth_handler)

    request = urllib2.Request(uri)
    try:
        response = opener.open(request)
    except urllib2.HTTPError, err:
        if err.fp:
            error = ": %s" % err.fp.read()
        else:
            error = ''
        logging.error("Error occured while opening HTTP %s" % error)
        raise
    res = response.read()
    response.close()
    return loads(res)
