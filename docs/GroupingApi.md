# openapi_client.GroupingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v6_grouping_chem_id_profiler_guid_get**](GroupingApi.md#api_v6_grouping_chem_id_profiler_guid_get) | **GET** /api/v6/grouping/{chemId}/{profilerGuid} | Creates a group of chemicals from the given databases having same profiles as the target chemical by the specified profiler


# **api_v6_grouping_chem_id_profiler_guid_get**
> List[Chemical] api_v6_grouping_chem_id_profiler_guid_get(chem_id, profiler_guid, database_ids=database_ids)

Creates a group of chemicals from the given databases having same profiles as the target chemical by the specified profiler

### Example


```python
import openapi_client
from openapi_client.models.chemical import Chemical
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.GroupingApi(api_client)
    chem_id = 'chem_id_example' # str | Target chemical
    profiler_guid = 'profiler_guid_example' # str | Profiler
    database_ids = ['database_ids_example'] # List[str] | List of databases (optional)

    try:
        # Creates a group of chemicals from the given databases having same profiles as the target chemical by the specified profiler
        api_response = api_instance.api_v6_grouping_chem_id_profiler_guid_get(chem_id, profiler_guid, database_ids=database_ids)
        print("The response of GroupingApi->api_v6_grouping_chem_id_profiler_guid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupingApi->api_v6_grouping_chem_id_profiler_guid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chem_id** | **str**| Target chemical | 
 **profiler_guid** | **str**| Profiler | 
 **database_ids** | [**List[str]**](str.md)| List of databases | [optional] 

### Return type

[**List[Chemical]**](Chemical.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

