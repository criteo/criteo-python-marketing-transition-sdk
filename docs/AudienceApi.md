# criteo_marketing_transition.AudienceApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_audience**](AudienceApi.md#create_audience) | **POST** /2021-04/audiences | 
[**delete_identifiers**](AudienceApi.md#delete_identifiers) | **DELETE** /2021-04/audiences/{audience-id}/contactlist | 
[**get_audiences**](AudienceApi.md#get_audiences) | **GET** /2021-04/audiences | 
[**modify_audience**](AudienceApi.md#modify_audience) | **PATCH** /2021-04/audiences/{audience-id} | 
[**modify_audience_users**](AudienceApi.md#modify_audience_users) | **PATCH** /2021-04/audiences/{audience-id}/contactlist | 
[**remove_audience**](AudienceApi.md#remove_audience) | **DELETE** /2021-04/audiences/{audience-id} | 


# **create_audience**
> NewAudienceResponse create_audience(new_audience_request)



Create an Audience for an Advertiser

### Example

* OAuth Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing_transition
from criteo_marketing_transition.rest import ApiException
from pprint import pprint
configuration = criteo_marketing_transition.Configuration()
# Configure OAuth2 access token for authorization: Authorization
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.criteo.com
configuration.host = "https://api.criteo.com"
# Create an instance of the API class
api_instance = criteo_marketing_transition.AudienceApi(criteo_marketing_transition.ApiClient(configuration))
new_audience_request = criteo_marketing_transition.NewAudienceRequest() # NewAudienceRequest | 

try:
    api_response = api_instance.create_audience(new_audience_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudienceApi->create_audience: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_audience_request** | [**NewAudienceRequest**](NewAudienceRequest.md)|  | 

### Return type

[**NewAudienceResponse**](NewAudienceResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The audience was created |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identifiers**
> DeleteAudienceContactListResponse delete_identifiers(audience_id)



delete all identifiers from an Audience

### Example

* OAuth Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing_transition
from criteo_marketing_transition.rest import ApiException
from pprint import pprint
configuration = criteo_marketing_transition.Configuration()
# Configure OAuth2 access token for authorization: Authorization
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.criteo.com
configuration.host = "https://api.criteo.com"
# Create an instance of the API class
api_instance = criteo_marketing_transition.AudienceApi(criteo_marketing_transition.ApiClient(configuration))
audience_id = 'audience_id_example' # str | The id of the audience to amend

try:
    api_response = api_instance.delete_identifiers(audience_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudienceApi->delete_identifiers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_id** | **str**| The id of the audience to amend | 

### Return type

[**DeleteAudienceContactListResponse**](DeleteAudienceContactListResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The contactlist was deleted |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audiences**
> GetAudiencesResponse get_audiences(advertiser_id=advertiser_id)



Get a list of all the audiences for the user or for the given advertiser_id

### Example

* OAuth Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing_transition
from criteo_marketing_transition.rest import ApiException
from pprint import pprint
configuration = criteo_marketing_transition.Configuration()
# Configure OAuth2 access token for authorization: Authorization
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.criteo.com
configuration.host = "https://api.criteo.com"
# Create an instance of the API class
api_instance = criteo_marketing_transition.AudienceApi(criteo_marketing_transition.ApiClient(configuration))
advertiser_id = 'advertiser_id_example' # str | The advertiser id to get all the audiences for. Mandatory for internal users. For external users,            if you don't provide it, we will take into account the advertisers from your portfolio (optional)

try:
    api_response = api_instance.get_audiences(advertiser_id=advertiser_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudienceApi->get_audiences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **str**| The advertiser id to get all the audiences for. Mandatory for internal users. For external users,            if you don&#39;t provide it, we will take into account the advertisers from your portfolio | [optional] 

### Return type

[**GetAudiencesResponse**](GetAudiencesResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list was retrieved. |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_audience**
> ReplaceAudienceResponse modify_audience(audience_id, replace_audience_request)



Update user audience specified by the audience id

### Example

* OAuth Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing_transition
from criteo_marketing_transition.rest import ApiException
from pprint import pprint
configuration = criteo_marketing_transition.Configuration()
# Configure OAuth2 access token for authorization: Authorization
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.criteo.com
configuration.host = "https://api.criteo.com"
# Create an instance of the API class
api_instance = criteo_marketing_transition.AudienceApi(criteo_marketing_transition.ApiClient(configuration))
audience_id = 'audience_id_example' # str | The id of the audience to amend
replace_audience_request = criteo_marketing_transition.ReplaceAudienceRequest() # ReplaceAudienceRequest | 

try:
    api_response = api_instance.modify_audience(audience_id, replace_audience_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudienceApi->modify_audience: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_id** | **str**| The id of the audience to amend | 
 **replace_audience_request** | [**ReplaceAudienceRequest**](ReplaceAudienceRequest.md)|  | 

### Return type

[**ReplaceAudienceResponse**](ReplaceAudienceResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The audience was updated |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_audience_users**
> ModifyAudienceResponse modify_audience_users(audience_id, contactlist_amendment_request)



Add/remove users to or from an audience

### Example

* OAuth Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing_transition
from criteo_marketing_transition.rest import ApiException
from pprint import pprint
configuration = criteo_marketing_transition.Configuration()
# Configure OAuth2 access token for authorization: Authorization
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.criteo.com
configuration.host = "https://api.criteo.com"
# Create an instance of the API class
api_instance = criteo_marketing_transition.AudienceApi(criteo_marketing_transition.ApiClient(configuration))
audience_id = 'audience_id_example' # str | The id of the audience to amend
contactlist_amendment_request = criteo_marketing_transition.ContactlistAmendmentRequest() # ContactlistAmendmentRequest | 

try:
    api_response = api_instance.modify_audience_users(audience_id, contactlist_amendment_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudienceApi->modify_audience_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_id** | **str**| The id of the audience to amend | 
 **contactlist_amendment_request** | [**ContactlistAmendmentRequest**](ContactlistAmendmentRequest.md)|  | 

### Return type

[**ModifyAudienceResponse**](ModifyAudienceResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Summary of created request |  -  |
**403** | Forbidden |  -  |
**404** | Audience 123 not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_audience**
> DeleteAudienceResponse remove_audience(audience_id)



Delete an audience by id

### Example

* OAuth Authentication (Authorization):
```python
from __future__ import print_function
import time
import criteo_marketing_transition
from criteo_marketing_transition.rest import ApiException
from pprint import pprint
configuration = criteo_marketing_transition.Configuration()
# Configure OAuth2 access token for authorization: Authorization
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.criteo.com
configuration.host = "https://api.criteo.com"
# Create an instance of the API class
api_instance = criteo_marketing_transition.AudienceApi(criteo_marketing_transition.ApiClient(configuration))
audience_id = 'audience_id_example' # str | The id of the audience to amend

try:
    api_response = api_instance.remove_audience(audience_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AudienceApi->remove_audience: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audience_id** | **str**| The id of the audience to amend | 

### Return type

[**DeleteAudienceResponse**](DeleteAudienceResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The audience was deleted |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

