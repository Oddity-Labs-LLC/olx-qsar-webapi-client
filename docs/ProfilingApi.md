# openapi_client.ProfilingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v6_profiling_all_chem_id_get**](ProfilingApi.md#api_v6_profiling_all_chem_id_get) | **GET** /api/v6/profiling/all/{chemId} | Profiles the provided chemical with all available profilers
[**api_v6_profiling_get**](ProfilingApi.md#api_v6_profiling_get) | **GET** /api/v6/profiling | Requests all available profilers
[**api_v6_profiling_profiler_guid_chem_id_simulator_guid_get**](ProfilingApi.md#api_v6_profiling_profiler_guid_chem_id_simulator_guid_get) | **GET** /api/v6/profiling/{profilerGuid}/{chemId}/{simulatorGuid} | Profiles the provided chemical with the specified profiler
[**api_v6_profiling_profiler_guid_get**](ProfilingApi.md#api_v6_profiling_profiler_guid_get) | **GET** /api/v6/profiling/{profilerGuid} | Returns all of the available categories for a provided profiler
[**api_v6_profiling_profiler_guid_info_get**](ProfilingApi.md#api_v6_profiling_profiler_guid_info_get) | **GET** /api/v6/profiling/{profilerGuid}/info | Provides general information for the specified profiler
[**api_v6_profiling_profiler_guid_literature_get**](ProfilingApi.md#api_v6_profiling_profiler_guid_literature_get) | **GET** /api/v6/profiling/{profilerGuid}/literature | Provides literature for the given category in the specified profiler
[**api_v6_profiling_relevancies_get**](ProfilingApi.md#api_v6_profiling_relevancies_get) | **GET** /api/v6/profiling/relevancies | Requests profiles that are relevant to the specified endpoint position and metadata


# **api_v6_profiling_all_chem_id_get**
> List[ProfilingResult] api_v6_profiling_all_chem_id_get(chem_id)

Profiles the provided chemical with all available profilers

### Example


```python
import openapi_client
from openapi_client.models.profiling_result import ProfilingResult
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
    api_instance = openapi_client.ProfilingApi(api_client)
    chem_id = 'chem_id_example' # str | The ChemID of the chemical to be profiled

    try:
        # Profiles the provided chemical with all available profilers
        api_response = api_instance.api_v6_profiling_all_chem_id_get(chem_id)
        print("The response of ProfilingApi->api_v6_profiling_all_chem_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilingApi->api_v6_profiling_all_chem_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chem_id** | **str**| The ChemID of the chemical to be profiled | 

### Return type

[**List[ProfilingResult]**](ProfilingResult.md)

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

# **api_v6_profiling_get**
> List[Profiler] api_v6_profiling_get()

Requests all available profilers

### Example


```python
import openapi_client
from openapi_client.models.profiler import Profiler
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
    api_instance = openapi_client.ProfilingApi(api_client)

    try:
        # Requests all available profilers
        api_response = api_instance.api_v6_profiling_get()
        print("The response of ProfilingApi->api_v6_profiling_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilingApi->api_v6_profiling_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Profiler]**](Profiler.md)

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

# **api_v6_profiling_profiler_guid_chem_id_simulator_guid_get**
> List[str] api_v6_profiling_profiler_guid_chem_id_simulator_guid_get(chem_id, profiler_guid, simulator_guid)

Profiles the provided chemical with the specified profiler

### Example


```python
import openapi_client
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
    api_instance = openapi_client.ProfilingApi(api_client)
    chem_id = 'chem_id_example' # str | The ChemID of the chemical to be profiled
    profiler_guid = 'profiler_guid_example' # str | GUID of the profiler to be used
    simulator_guid = 'simulator_guid_example' # str | GUID of the profiler to be used

    try:
        # Profiles the provided chemical with the specified profiler
        api_response = api_instance.api_v6_profiling_profiler_guid_chem_id_simulator_guid_get(chem_id, profiler_guid, simulator_guid)
        print("The response of ProfilingApi->api_v6_profiling_profiler_guid_chem_id_simulator_guid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilingApi->api_v6_profiling_profiler_guid_chem_id_simulator_guid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chem_id** | **str**| The ChemID of the chemical to be profiled | 
 **profiler_guid** | **str**| GUID of the profiler to be used | 
 **simulator_guid** | **str**| GUID of the profiler to be used | 

### Return type

**List[str]**

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

# **api_v6_profiling_profiler_guid_get**
> List[str] api_v6_profiling_profiler_guid_get(profiler_guid)

Returns all of the available categories for a provided profiler

### Example


```python
import openapi_client
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
    api_instance = openapi_client.ProfilingApi(api_client)
    profiler_guid = 'profiler_guid_example' # str | The profile for which to retrieve the categories

    try:
        # Returns all of the available categories for a provided profiler
        api_response = api_instance.api_v6_profiling_profiler_guid_get(profiler_guid)
        print("The response of ProfilingApi->api_v6_profiling_profiler_guid_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilingApi->api_v6_profiling_profiler_guid_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profiler_guid** | **str**| The profile for which to retrieve the categories | 

### Return type

**List[str]**

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

# **api_v6_profiling_profiler_guid_info_get**
> ITbObjectAbout api_v6_profiling_profiler_guid_info_get(profiler_guid)

Provides general information for the specified profiler

### Example


```python
import openapi_client
from openapi_client.models.itb_object_about import ITbObjectAbout
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
    api_instance = openapi_client.ProfilingApi(api_client)
    profiler_guid = 'profiler_guid_example' # str | GUID of the Profiler

    try:
        # Provides general information for the specified profiler
        api_response = api_instance.api_v6_profiling_profiler_guid_info_get(profiler_guid)
        print("The response of ProfilingApi->api_v6_profiling_profiler_guid_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilingApi->api_v6_profiling_profiler_guid_info_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profiler_guid** | **str**| GUID of the Profiler | 

### Return type

[**ITbObjectAbout**](ITbObjectAbout.md)

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

# **api_v6_profiling_profiler_guid_literature_get**
> api_v6_profiling_profiler_guid_literature_get(profiler_guid, category=category)

Provides literature for the given category in the specified profiler

### Example


```python
import openapi_client
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
    api_instance = openapi_client.ProfilingApi(api_client)
    profiler_guid = 'profiler_guid_example' # str | GUID of the profiler
    category = 'category_example' # str | Name of the category (optional)

    try:
        # Provides literature for the given category in the specified profiler
        api_instance.api_v6_profiling_profiler_guid_literature_get(profiler_guid, category=category)
    except Exception as e:
        print("Exception when calling ProfilingApi->api_v6_profiling_profiler_guid_literature_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profiler_guid** | **str**| GUID of the profiler | 
 **category** | **str**| Name of the category | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v6_profiling_relevancies_get**
> RelevantProfiles api_v6_profiling_relevancies_get(position=position, metadata=metadata)

Requests profiles that are relevant to the specified endpoint position and metadata

### Example


```python
import openapi_client
from openapi_client.models.relevant_profiles import RelevantProfiles
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
    api_instance = openapi_client.ProfilingApi(api_client)
    position = 'position_example' # str | A #-delimited endpoint tree position> (optional)
    metadata = {'key': 'metadata_example'} # Dict[str, str] | A set of metadata key-value pairs (optional)

    try:
        # Requests profiles that are relevant to the specified endpoint position and metadata
        api_response = api_instance.api_v6_profiling_relevancies_get(position=position, metadata=metadata)
        print("The response of ProfilingApi->api_v6_profiling_relevancies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilingApi->api_v6_profiling_relevancies_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position** | **str**| A #-delimited endpoint tree position&gt; | [optional] 
 **metadata** | [**Dict[str, str]**](str.md)| A set of metadata key-value pairs | [optional] 

### Return type

[**RelevantProfiles**](RelevantProfiles.md)

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

