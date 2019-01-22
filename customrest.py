#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
customer REST client service.
supports: Python 3.X
"""

import requests
from requests.auth import HTTPBasicAuth
from ipaddress import ip_address, IPv4Address, IPv6Address
from typing import Optional, List, Dict


class IpAddressError(Exception):
    """Generic IpAddress Error"""
    pass


class RESTClientObject(object):
    """
    Simple REST client object class.
    """
    def __init__(self,
                 ipaddress,
                 username,
                 password,
                 port=None,
                 headers={'Content-Type': 'application/json',
                          'Accept': 'application/json'},
                 timeout=None,
                 protocol="http",
                 base_uri="", ):
        """
        initialization of REST client service objects.

        param: ipaddress
        param: username
        param: password
        param: port
        param: headers
        param: timeout
        """
        self.ipaddress = ipaddress
        self.username = username
        self.password = password
        self.base_uri = base_uri
        self.port = port
        self.timeout = timeout
        self.protocol = protocol
        self.req = requests.session()
        self.req.headers = headers
        self.auth = HTTPBasicAuth(self.username, self.password)

    def get_uri(self):
        return f"{self.protocol}://{self.ipaddress}:{self.port}/{self.base_uri}"

    def __enter__(self):
        """Python context manager for connection"""
        data = self.req.get(self.get_uri(), auth=self.auth, verify=False)
        return data

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Python context manager for disconnection / deleting session"""
        del self.req
        return False


if __name__ == "__main__":
    args = ("xx.xx.xx.xx", "xxx", "xxx", )
    kwargs = {"port": xx, "protocol": "https", "base_uri": "/", }
    with RESTClientObject(*args, **kwargs) as data:
        print(data)
