# coding: utf-8

"""
    Criteo API Transition Swagger

    This is used to help Criteo clients transition from MAPI to Criteo API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from criteo_marketing_transition.api_client import ApiClient
from criteo_marketing_transition.exceptions import (
    ApiTypeError,
    ApiValueError
)


class AudienceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_audience(self, new_audience_request, **kwargs):  # noqa: E501
        """create_audience  # noqa: E501

        Create an Audience for an Advertiser  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_audience(new_audience_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param NewAudienceRequest new_audience_request: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: NewAudienceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_audience_with_http_info(new_audience_request, **kwargs)  # noqa: E501

    def create_audience_with_http_info(self, new_audience_request, **kwargs):  # noqa: E501
        """create_audience  # noqa: E501

        Create an Audience for an Advertiser  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_audience_with_http_info(new_audience_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param NewAudienceRequest new_audience_request: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(NewAudienceResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['new_audience_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_audience" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'new_audience_request' is set
        if ('new_audience_request' not in local_var_params or
                local_var_params['new_audience_request'] is None):
            raise ApiValueError("Missing the required parameter `new_audience_request` when calling `create_audience`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'new_audience_request' in local_var_params:
            body_params = local_var_params['new_audience_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/2021-04/audiences', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NewAudienceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_identifiers(self, audience_id, **kwargs):  # noqa: E501
        """delete_identifiers  # noqa: E501

        delete all identifiers from an Audience  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_identifiers(audience_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str audience_id: The id of the audience to amend (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DeleteAudienceContactListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_identifiers_with_http_info(audience_id, **kwargs)  # noqa: E501

    def delete_identifiers_with_http_info(self, audience_id, **kwargs):  # noqa: E501
        """delete_identifiers  # noqa: E501

        delete all identifiers from an Audience  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_identifiers_with_http_info(audience_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str audience_id: The id of the audience to amend (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DeleteAudienceContactListResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['audience_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_identifiers" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'audience_id' is set
        if ('audience_id' not in local_var_params or
                local_var_params['audience_id'] is None):
            raise ApiValueError("Missing the required parameter `audience_id` when calling `delete_identifiers`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'audience_id' in local_var_params:
            path_params['audience-id'] = local_var_params['audience_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/2021-04/audiences/{audience-id}/contactlist', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeleteAudienceContactListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_audiences(self, **kwargs):  # noqa: E501
        """get_audiences  # noqa: E501

        Get a list of all the audiences for the user or for the given advertiser_id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audiences(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str advertiser_id: The advertiser id to get all the audiences for. Mandatory for internal users. For external users,            if you don't provide it, we will take into account the advertisers from your portfolio
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: GetAudiencesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_audiences_with_http_info(**kwargs)  # noqa: E501

    def get_audiences_with_http_info(self, **kwargs):  # noqa: E501
        """get_audiences  # noqa: E501

        Get a list of all the audiences for the user or for the given advertiser_id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_audiences_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str advertiser_id: The advertiser id to get all the audiences for. Mandatory for internal users. For external users,            if you don't provide it, we will take into account the advertisers from your portfolio
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(GetAudiencesResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['advertiser_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_audiences" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'advertiser_id' in local_var_params:
            query_params.append(('advertiser-id', local_var_params['advertiser_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/2021-04/audiences', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetAudiencesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_audience(self, audience_id, replace_audience_request, **kwargs):  # noqa: E501
        """modify_audience  # noqa: E501

        Update user audience specified by the audience id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_audience(audience_id, replace_audience_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str audience_id: The id of the audience to amend (required)
        :param ReplaceAudienceRequest replace_audience_request: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ReplaceAudienceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.modify_audience_with_http_info(audience_id, replace_audience_request, **kwargs)  # noqa: E501

    def modify_audience_with_http_info(self, audience_id, replace_audience_request, **kwargs):  # noqa: E501
        """modify_audience  # noqa: E501

        Update user audience specified by the audience id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_audience_with_http_info(audience_id, replace_audience_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str audience_id: The id of the audience to amend (required)
        :param ReplaceAudienceRequest replace_audience_request: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ReplaceAudienceResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['audience_id', 'replace_audience_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_audience" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'audience_id' is set
        if ('audience_id' not in local_var_params or
                local_var_params['audience_id'] is None):
            raise ApiValueError("Missing the required parameter `audience_id` when calling `modify_audience`")  # noqa: E501
        # verify the required parameter 'replace_audience_request' is set
        if ('replace_audience_request' not in local_var_params or
                local_var_params['replace_audience_request'] is None):
            raise ApiValueError("Missing the required parameter `replace_audience_request` when calling `modify_audience`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'audience_id' in local_var_params:
            path_params['audience-id'] = local_var_params['audience_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'replace_audience_request' in local_var_params:
            body_params = local_var_params['replace_audience_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/2021-04/audiences/{audience-id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReplaceAudienceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_audience_users(self, audience_id, contactlist_amendment_request, **kwargs):  # noqa: E501
        """modify_audience_users  # noqa: E501

        Add/remove users to or from an audience  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_audience_users(audience_id, contactlist_amendment_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str audience_id: The id of the audience to amend (required)
        :param ContactlistAmendmentRequest contactlist_amendment_request: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ModifyAudienceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.modify_audience_users_with_http_info(audience_id, contactlist_amendment_request, **kwargs)  # noqa: E501

    def modify_audience_users_with_http_info(self, audience_id, contactlist_amendment_request, **kwargs):  # noqa: E501
        """modify_audience_users  # noqa: E501

        Add/remove users to or from an audience  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_audience_users_with_http_info(audience_id, contactlist_amendment_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str audience_id: The id of the audience to amend (required)
        :param ContactlistAmendmentRequest contactlist_amendment_request: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ModifyAudienceResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['audience_id', 'contactlist_amendment_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_audience_users" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'audience_id' is set
        if ('audience_id' not in local_var_params or
                local_var_params['audience_id'] is None):
            raise ApiValueError("Missing the required parameter `audience_id` when calling `modify_audience_users`")  # noqa: E501
        # verify the required parameter 'contactlist_amendment_request' is set
        if ('contactlist_amendment_request' not in local_var_params or
                local_var_params['contactlist_amendment_request'] is None):
            raise ApiValueError("Missing the required parameter `contactlist_amendment_request` when calling `modify_audience_users`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'audience_id' in local_var_params:
            path_params['audience-id'] = local_var_params['audience_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'contactlist_amendment_request' in local_var_params:
            body_params = local_var_params['contactlist_amendment_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/2021-04/audiences/{audience-id}/contactlist', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModifyAudienceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_audience(self, audience_id, **kwargs):  # noqa: E501
        """remove_audience  # noqa: E501

        Delete an audience by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_audience(audience_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str audience_id: The id of the audience to amend (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: DeleteAudienceResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.remove_audience_with_http_info(audience_id, **kwargs)  # noqa: E501

    def remove_audience_with_http_info(self, audience_id, **kwargs):  # noqa: E501
        """remove_audience  # noqa: E501

        Delete an audience by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_audience_with_http_info(audience_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str audience_id: The id of the audience to amend (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(DeleteAudienceResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['audience_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_audience" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'audience_id' is set
        if ('audience_id' not in local_var_params or
                local_var_params['audience_id'] is None):
            raise ApiValueError("Missing the required parameter `audience_id` when calling `remove_audience`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'audience_id' in local_var_params:
            path_params['audience-id'] = local_var_params['audience_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/2021-04/audiences/{audience-id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeleteAudienceResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
