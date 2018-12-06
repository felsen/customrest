#! /usr/bin/python
# -*- coding: utf-8 -*-

from typing import Optional, List, Dict


class RESTClientObject(object):

    """
    Simple REST client object class.
    """

    def __init__(self,
                 ipaddress: str,
                 username: str,
                 password: str,
                 port: int=None,
                 headers: Optional[Dict[str, str]]=None,
                 timeout: int=None, ):
        """
        initialization of python objects.

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
        self.port = port
        self.headers = headers
        self.timeout = timeout


    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

