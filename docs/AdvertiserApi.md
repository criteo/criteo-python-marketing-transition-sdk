# criteo_marketing_transition.AdvertiserApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_portfolio_get**](AdvertiserApi.md#api_portfolio_get) | **GET** /2021-04/advertisers/me | 
[**get_categories**](AdvertiserApi.md#get_categories) | **GET** /legacy/marketing/v1/advertisers/{advertiserId}/categories | Gets all advertiser&#39;s categories
[**get_category**](AdvertiserApi.md#get_category) | **GET** /legacy/marketing/v1/advertisers/{advertiserId}/categories/{categoryHashCode} | Gets a specific advertiser&#39;s category


# **api_portfolio_get**
> GetPortfolioResponse api_portfolio_get()



Use this call to fetch a list of all advertisers in your account.

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
api_instance = criteo_marketing_transition.AdvertiserApi(criteo_marketing_transition.ApiClient(configuration))

try:
    api_response = api_instance.api_portfolio_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvertiserApi->api_portfolio_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetPortfolioResponse**](GetPortfolioResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_categories**
> list[CategoryMessage] get_categories(advertiser_id, enabled_only=enabled_only)

Gets all advertiser's categories

Get the list of all the categories linked to the requested advertiser.

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
api_instance = criteo_marketing_transition.AdvertiserApi(criteo_marketing_transition.ApiClient(configuration))
advertiser_id = 56 # int | Mandatory. The id of the advertiser to return.
enabled_only = True # bool | Optional. Returns only categories you can bid on. Defaults to false. (optional)

try:
    # Gets all advertiser's categories
    api_response = api_instance.get_categories(advertiser_id, enabled_only=enabled_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvertiserApi->get_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| Mandatory. The id of the advertiser to return. | 
 **enabled_only** | **bool**| Optional. Returns only categories you can bid on. Defaults to false. | [optional] 

### Return type

[**list[CategoryMessage]**](CategoryMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Categories returned OK. |  -  |
**401** | Authentication failed. |  -  |
**403** | The requested advertiser is missing from current user’s portfolio. |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category**
> list[CategoryMessage] get_category(advertiser_id, category_hash_code)

Gets a specific advertiser's category

Get a specific category linked to the requested advertiser.

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
api_instance = criteo_marketing_transition.AdvertiserApi(criteo_marketing_transition.ApiClient(configuration))
advertiser_id = 56 # int | Mandatory. The id of the advertiser to return.
category_hash_code = 56 # int | Mandatory. The id of the category to return.

try:
    # Gets a specific advertiser's category
    api_response = api_instance.get_category(advertiser_id, category_hash_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvertiserApi->get_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advertiser_id** | **int**| Mandatory. The id of the advertiser to return. | 
 **category_hash_code** | **int**| Mandatory. The id of the category to return. | 

### Return type

[**list[CategoryMessage]**](CategoryMessage.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Category returned OK. |  -  |
**401** | Authentication failed. |  -  |
**403** | The requested advertiser is missing from current user’s portfolio. |  -  |
**404** | The requested category was not found for the advertiser. |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

