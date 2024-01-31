from requests.api import request


def post(url, data=None, json=None, proxies=None, timeout=None, port=None, **kwargs):
    r"""Sends a POST request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """
    if(proxies != None):
            if(port != None):
                response = request("post",url,data=data,json=json,proxies=proxies,timeout=timeout,port=port, **kwargs)
            else:
                response = request("post",url,data=data,json=json,proxies=proxies,timeout=timeout, **kwargs)
    else:
            if(port != None):
                response = request("post",url,data=data,json=json,timeout=timeout,port=port, **kwargs)
            else:
                response = request("post",url,data=data,json=json,timeout=timeout, **kwargs)
    return response

def get(url, data=None, json=None, proxies=None, timeout=None, port=None, **kwargs):
    r"""Sends a POST request.

    :param url: URL for the new :class:`Request` object.
    :param data: (optional) Dictionary, list of tuples, bytes, or file-like
        object to send in the body of the :class:`Request`.
    :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
    :param \*\*kwargs: Optional arguments that ``request`` takes.
    :return: :class:`Response <Response>` object
    :rtype: requests.Response
    """
    if(proxies != None):
            if(port != None):
                response = request("get",url,data=data,json=json,proxies=proxies,timeout=timeout,port=port, **kwargs)
            else:
                response = request("get",url,data=data,json=json,proxies=proxies,timeout=timeout, **kwargs)
    else:
            if(port != None):
                response = request("get",url,data=data,json=json,timeout=timeout,port=port, **kwargs)
            else:
                response = request("get",url,data=data,json=json,timeout=timeout, **kwargs)
    return response