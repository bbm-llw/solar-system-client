# coding: utf-8

"""
    Solar System openData

    API to get all data about all solar system objects  # noqa: E501

    OpenAPI spec version: 1.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class BodiesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def bodies_get(self, **kwargs):  # noqa: E501
        """List  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bodies_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data: The data you want to retrieve (comma separated). Example: id,semimajorAxis,isPlanet.
        :param str exclude: One or more data you want to exclude (comma separated). Example: id,isPlanet.
        :param str order: A data you want to sort on and the sort direction (comma separated). Example: id,desc. Only one data is authorized.
        :param str page: Page number (number>=1) and page size (size>=1 and 20 by default) (comma separated). NB: You cannot use \"page\" without \"order\"! Example: 1,10.
        :param bool row_data: Transform the object in records. NB: This can also be done client-side in JavaScript!
        :param list[str] filter: Filters to be applied. Each filter consists of a data, an operator and a value (comma separated). Example: id,eq,mars. Accepted operators are : cs (like) - sw (start with) - ew (end with) - eq (equal) - lt (less than) - le (less or equal than) - ge (greater or equal than) - gt (greater than) - bt (between). And all opposites operators : ncs - nsw - new - neq - nlt - nle - nge - ngt - nbt. Note : if anyone filter is invalid, all filters will be ignore.
        :param str satisfy: Should all filters match (default)? Or any?
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.bodies_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.bodies_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def bodies_get_with_http_info(self, **kwargs):  # noqa: E501
        """List  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bodies_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data: The data you want to retrieve (comma separated). Example: id,semimajorAxis,isPlanet.
        :param str exclude: One or more data you want to exclude (comma separated). Example: id,isPlanet.
        :param str order: A data you want to sort on and the sort direction (comma separated). Example: id,desc. Only one data is authorized.
        :param str page: Page number (number>=1) and page size (size>=1 and 20 by default) (comma separated). NB: You cannot use \"page\" without \"order\"! Example: 1,10.
        :param bool row_data: Transform the object in records. NB: This can also be done client-side in JavaScript!
        :param list[str] filter: Filters to be applied. Each filter consists of a data, an operator and a value (comma separated). Example: id,eq,mars. Accepted operators are : cs (like) - sw (start with) - ew (end with) - eq (equal) - lt (less than) - le (less or equal than) - ge (greater or equal than) - gt (greater than) - bt (between). And all opposites operators : ncs - nsw - new - neq - nlt - nle - nge - ngt - nbt. Note : if anyone filter is invalid, all filters will be ignore.
        :param str satisfy: Should all filters match (default)? Or any?
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data', 'exclude', 'order', 'page', 'row_data', 'filter', 'satisfy']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bodies_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'data' in params:
            query_params.append(('data', params['data']))  # noqa: E501
        if 'exclude' in params:
            query_params.append(('exclude', params['exclude']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'row_data' in params:
            query_params.append(('rowData', params['row_data']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter[]', params['filter']))  # noqa: E501
            collection_formats['filter[]'] = 'multi'  # noqa: E501
        if 'satisfy' in params:
            query_params.append(('satisfy', params['satisfy']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/bodies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def bodies_id_get(self, id, **kwargs):  # noqa: E501
        """read  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bodies_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Identifier for item. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.bodies_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.bodies_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def bodies_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """read  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bodies_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Identifier for item. (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bodies_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `bodies_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/bodies/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
