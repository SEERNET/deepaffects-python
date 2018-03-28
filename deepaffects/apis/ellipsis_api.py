# coding: utf-8

"""
    DeepAffects

    OpenAPI spec version: v1
"""


from __future__ import absolute_import

# python 2 and python 3 compatibility library
from six import iteritems

from ..api_client import ApiClient
from ..configuration import Configuration


class EllipsisAPI(object):

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def async_is_depressed(self, body, webhook, **kwargs):
        """
        Detect whether the person in audio clip is depressed
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.async_is_depressed(body, webhook, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Audio body: Audio object to predict depression. (required)
        :param str webhook: The webhook url where result from async resource is posted (required)
        :param str request_id: Unique identifier for the request
        :return: AsyncResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.async_is_depressed_with_http_info(body, webhook, **kwargs)
        else:
            (data) = self.async_is_depressed_with_http_info(body, webhook, **kwargs)
            return data

    def async_is_depressed_with_http_info(self, body, webhook, **kwargs):
        """
        Detect whether the person in audio clip is depressed
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.async_is_depressed_with_http_info(body, webhook, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Audio body: Audio object to predict depression. (required)
        :param str webhook: The webhook url where result from async resource is posted (required)
        :param str request_id: Unique identifier for the request
        :return: AsyncResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'webhook', 'request_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method async_is_depressed" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `async_is_depressed`")
        # verify the required parameter 'webhook' is set
        if ('webhook' not in params) or (params['webhook'] is None):
            raise ValueError("Missing the required parameter `webhook` when calling `async_is_depressed`")


        collection_formats = {}

        resource_path = '/audio/custom/ellipsis/api/v1/async/is_depressed'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'webhook' in params:
            query_params['webhook'] = params['webhook']
        if 'request_id' in params:
            query_params['request_id'] = params['request_id']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['UserSecurity']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='AsyncResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def sync_is_depressed(self, body, **kwargs):
        """
        Detect whether the person in audio clip is depressed
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sync_is_depressed(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Audio body: Audio object to predict depression. (required)
        :return: boolean
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.sync_is_depressed_with_http_info(body, **kwargs)
        else:
            (data) = self.sync_is_depressed_with_http_info(body, **kwargs)
            return data

    def sync_is_depressed_with_http_info(self, body, **kwargs):
        """
        Detect whether the person in audio clip is depressed
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.sync_is_depressed_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Audio body: Audio object to predict depression. (required)
        :return: boolean
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sync_is_depressed" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `sync_is_depressed`")


        collection_formats = {}

        resource_path = '/audio/custom/ellipsis/api/v1/sync/is_depressed'.replace('{format}', 'json')
        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['UserSecurity']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='bool',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
