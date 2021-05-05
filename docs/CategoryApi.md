# criteo_marketing_transition.CategoryApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_categories**](CategoryApi.md#get_categories) | **GET** /legacy/marketing/v1/categories | Gets categories
[**update_categories**](CategoryApi.md#update_categories) | **PUT** /legacy/marketing/v1/categories | Enables/disables categories


# **get_categories**
> list[CategoryMessage] get_categories(campaign_ids=campaign_ids, advertiser_ids=advertiser_ids, category_hash_codes=category_hash_codes, enabled_only=enabled_only)

Gets categories

Get the list of categories with the specified filters.  If a category is requested but is missing from current user's portfolio, it will not be included in the list.  If neither campaign ids nor advertisers ids are provided, then the user's portfolio will be used.

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
api_instance = criteo_marketing_transition.CategoryApi(criteo_marketing_transition.ApiClient(configuration))
campaign_ids = 'campaign_ids_example' # str | Optional. One or more campaign ids, E.g., 78, 12932, 45236. If the campaign ids requested are not liked to advertisers in the user's portfolio, they will be skipped. (optional)
advertiser_ids = 'advertiser_ids_example' # str | Optional. One or more advertiser ids, E.g., 78, 12932, 45236. If the advertiser ids requested are not part of the user's portfolio, they will be skipped. (optional)
category_hash_codes = 'category_hash_codes_example' # str | Optional. One or more category hash codes. (optional)
enabled_only = True # bool | Optional. Returns only categories you can bid on. Defaults to false. (optional)

try:
    # Gets categories
    api_response = api_instance.get_categories(campaign_ids=campaign_ids, advertiser_ids=advertiser_ids, category_hash_codes=category_hash_codes, enabled_only=enabled_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->get_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_ids** | **str**| Optional. One or more campaign ids, E.g., 78, 12932, 45236. If the campaign ids requested are not liked to advertisers in the user&#39;s portfolio, they will be skipped. | [optional] 
 **advertiser_ids** | **str**| Optional. One or more advertiser ids, E.g., 78, 12932, 45236. If the advertiser ids requested are not part of the user&#39;s portfolio, they will be skipped. | [optional] 
 **category_hash_codes** | **str**| Optional. One or more category hash codes. | [optional] 
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
**400** | There is not even one valid advertiserId or campaignId requested. |  -  |
**401** | Authentication failed. |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_categories**
> list[CategoryUpdatesPerCatalog] update_categories(categories_per_catalog)

Enables/disables categories

Update categories for multiple catalogs.<br />  Please note that all validations need to pass before applying the requested changes;  the subsequent validation error messages will be returned in the response.<br />  Please note that bidding will still happen for disabled categories, but using the Camapign's bid.  If the call is successful, full details about the changed categories will be returned.

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
api_instance = criteo_marketing_transition.CategoryApi(criteo_marketing_transition.ApiClient(configuration))
categories_per_catalog = [criteo_marketing_transition.CategoryUpdatesPerCatalog()] # list[CategoryUpdatesPerCatalog] | The list of categories to be enabled/disabled, grouped by catalog.

try:
    # Enables/disables categories
    api_response = api_instance.update_categories(categories_per_catalog)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoryApi->update_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categories_per_catalog** | [**list[CategoryUpdatesPerCatalog]**](CategoryUpdatesPerCatalog.md)| The list of categories to be enabled/disabled, grouped by catalog. | 

### Return type

[**list[CategoryUpdatesPerCatalog]**](CategoryUpdatesPerCatalog.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded, text/html
 - **Accept**: application/json, text/json, application/xml, text/xml, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Categories updated OK. |  -  |
**400** | Invalid input. Please check returned message for details. |  -  |
**401** | Authentication failed. |  -  |
**429** | Throttling failure. Maximum sending rate exceeded. |  -  |
**500** | Unknown error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

