# criteo_marketing_transition.AnalyticsApi

All URIs are relative to *https://api.criteo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_adset_report**](AnalyticsApi.md#get_adset_report) | **POST** /2021-04/statistics/report | 
[**get_transactions_report**](AnalyticsApi.md#get_transactions_report) | **POST** /2021-04/transactions/report | 


# **get_adset_report**
> str get_adset_report(statistics_report_query_message=statistics_report_query_message)



This Statistics endpoint provides adset related data. It is an upgrade of our previous Statistics endpoint, and includes new metrics and customization capabilities.

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
api_instance = criteo_marketing_transition.AnalyticsApi(criteo_marketing_transition.ApiClient(configuration))
statistics_report_query_message = criteo_marketing_transition.StatisticsReportQueryMessage() # StatisticsReportQueryMessage |  (optional)

try:
    api_response = api_instance.get_adset_report(statistics_report_query_message=statistics_report_query_message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_adset_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statistics_report_query_message** | [**StatisticsReportQueryMessage**](StatisticsReportQueryMessage.md)|  | [optional] 

### Return type

**str**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_report**
> str get_transactions_report(transactions_report_query_data_message=transactions_report_query_data_message)



This Transactions endpoint provides transactions id related data.

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
api_instance = criteo_marketing_transition.AnalyticsApi(criteo_marketing_transition.ApiClient(configuration))
transactions_report_query_data_message = criteo_marketing_transition.TransactionsReportQueryDataMessage() # TransactionsReportQueryDataMessage |  (optional)

try:
    api_response = api_instance.get_transactions_report(transactions_report_query_data_message=transactions_report_query_data_message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->get_transactions_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transactions_report_query_data_message** | [**TransactionsReportQueryDataMessage**](TransactionsReportQueryDataMessage.md)|  | [optional] 

### Return type

**str**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

