# openapi_client.DataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v6_data_all_chem_id_get**](DataApi.md#api_v6_data_all_chem_id_get) | **GET** /api/v6/data/all/{chemId} | Retrieves all data for the selected chemical
[**api_v6_data_chem_id_get**](DataApi.md#api_v6_data_chem_id_get) | **GET** /api/v6/data/{chemId} | Retrieves data for the specified endpoint at the given position for the selected chemical
[**api_v6_data_databases_get**](DataApi.md#api_v6_data_databases_get) | **GET** /api/v6/data/databases | Retrieves a list with databases containing data for the specified endpoint
[**api_v6_data_endpoint_get**](DataApi.md#api_v6_data_endpoint_get) | **GET** /api/v6/data/endpoint | Retrieves all endpoints available at the given position of the endpoint tree
[**api_v6_data_endpointtree_get**](DataApi.md#api_v6_data_endpointtree_get) | **GET** /api/v6/data/endpointtree | Returns the entire endpoint tree
[**api_v6_data_metadatahierarchy_get**](DataApi.md#api_v6_data_metadatahierarchy_get) | **GET** /api/v6/data/metadatahierarchy | Returns the default metadata hierarchy in one call (optimization)
[**api_v6_data_metadatavalues_post**](DataApi.md#api_v6_data_metadatavalues_post) | **POST** /api/v6/data/metadatavalues | Returns the suggested metadata values for a given metadata label based on the already defined ones (in the same branch)
[**api_v6_data_units_get**](DataApi.md#api_v6_data_units_get) | **GET** /api/v6/data/units | Provides the units for the endpoint at the given endpoint tree position


# **api_v6_data_all_chem_id_get**
> List[DataPoint] api_v6_data_all_chem_id_get(chem_id, include_metadata=include_metadata)

Retrieves all data for the selected chemical

### Example


```python
import openapi_client
from openapi_client.models.data_point import DataPoint
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
    api_instance = openapi_client.DataApi(api_client)
    chem_id = 'chem_id_example' # str | ChemID of the chemical to look for
    include_metadata = False # bool | If metadata should be provided with the endpoint (optional) (default to False)

    try:
        # Retrieves all data for the selected chemical
        api_response = api_instance.api_v6_data_all_chem_id_get(chem_id, include_metadata=include_metadata)
        print("The response of DataApi->api_v6_data_all_chem_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->api_v6_data_all_chem_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chem_id** | **str**| ChemID of the chemical to look for | 
 **include_metadata** | **bool**| If metadata should be provided with the endpoint | [optional] [default to False]

### Return type

[**List[DataPoint]**](DataPoint.md)

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

# **api_v6_data_chem_id_get**
> List[DataPoint] api_v6_data_chem_id_get(chem_id, position=position, endpoint=endpoint, include_metadata=include_metadata)

Retrieves data for the specified endpoint at the given position for the selected chemical

### Example


```python
import openapi_client
from openapi_client.models.data_point import DataPoint
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
    api_instance = openapi_client.DataApi(api_client)
    chem_id = 'chem_id_example' # str | ChemID of the chemical to look for
    position = 'position_example' # str | A #-delimited endpoint tree position (optional)
    endpoint = 'endpoint_example' # str | The name of the endpoint (optional)
    include_metadata = False # bool | If metadata should be provided with the endpoint (optional) (default to False)

    try:
        # Retrieves data for the specified endpoint at the given position for the selected chemical
        api_response = api_instance.api_v6_data_chem_id_get(chem_id, position=position, endpoint=endpoint, include_metadata=include_metadata)
        print("The response of DataApi->api_v6_data_chem_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->api_v6_data_chem_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chem_id** | **str**| ChemID of the chemical to look for | 
 **position** | **str**| A #-delimited endpoint tree position | [optional] 
 **endpoint** | **str**| The name of the endpoint | [optional] 
 **include_metadata** | **bool**| If metadata should be provided with the endpoint | [optional] [default to False]

### Return type

[**List[DataPoint]**](DataPoint.md)

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

# **api_v6_data_databases_get**
> List[str] api_v6_data_databases_get(position=position, endpoint=endpoint)

Retrieves a list with databases containing data for the specified endpoint

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
    api_instance = openapi_client.DataApi(api_client)
    position = 'position_example' # str | A #-delimited endpoint tree position (optional)
    endpoint = 'endpoint_example' # str | The name of the endpoint (optional)

    try:
        # Retrieves a list with databases containing data for the specified endpoint
        api_response = api_instance.api_v6_data_databases_get(position=position, endpoint=endpoint)
        print("The response of DataApi->api_v6_data_databases_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->api_v6_data_databases_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position** | **str**| A #-delimited endpoint tree position | [optional] 
 **endpoint** | **str**| The name of the endpoint | [optional] 

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

# **api_v6_data_endpoint_get**
> List[str] api_v6_data_endpoint_get(position=position)

Retrieves all endpoints available at the given position of the endpoint tree

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
    api_instance = openapi_client.DataApi(api_client)
    position = 'position_example' # str | A #-delimited endpoint tree position (optional)

    try:
        # Retrieves all endpoints available at the given position of the endpoint tree
        api_response = api_instance.api_v6_data_endpoint_get(position=position)
        print("The response of DataApi->api_v6_data_endpoint_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->api_v6_data_endpoint_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position** | **str**| A #-delimited endpoint tree position | [optional] 

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

# **api_v6_data_endpointtree_get**
> List[str] api_v6_data_endpointtree_get()

Returns the entire endpoint tree

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
    api_instance = openapi_client.DataApi(api_client)

    try:
        # Returns the entire endpoint tree
        api_response = api_instance.api_v6_data_endpointtree_get()
        print("The response of DataApi->api_v6_data_endpointtree_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->api_v6_data_endpointtree_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **api_v6_data_metadatahierarchy_get**
> List[MetadataHierarchy] api_v6_data_metadatahierarchy_get()

Returns the default metadata hierarchy in one call (optimization)

### Example


```python
import openapi_client
from openapi_client.models.metadata_hierarchy import MetadataHierarchy
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
    api_instance = openapi_client.DataApi(api_client)

    try:
        # Returns the default metadata hierarchy in one call (optimization)
        api_response = api_instance.api_v6_data_metadatahierarchy_get()
        print("The response of DataApi->api_v6_data_metadatahierarchy_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->api_v6_data_metadatahierarchy_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[MetadataHierarchy]**](MetadataHierarchy.md)

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

# **api_v6_data_metadatavalues_post**
> List[str] api_v6_data_metadatavalues_post(rigid_path=rigid_path, metadata_label=metadata_label, already_defined_metadata=already_defined_metadata)

Returns the suggested metadata values for a given metadata label based on the already defined ones (in the same branch)

### Example


```python
import openapi_client
from openapi_client.models.already_defined_metadata import AlreadyDefinedMetadata
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
    api_instance = openapi_client.DataApi(api_client)
    rigid_path = 'rigid_path_example' # str | Rigid path (optional)
    metadata_label = 'metadata_label_example' # str | Metadata label for which to retrieve suggested values (optional)
    already_defined_metadata = [openapi_client.AlreadyDefinedMetadata()] # List[AlreadyDefinedMetadata] | Already defined text metadata values along the branch (optional)

    try:
        # Returns the suggested metadata values for a given metadata label based on the already defined ones (in the same branch)
        api_response = api_instance.api_v6_data_metadatavalues_post(rigid_path=rigid_path, metadata_label=metadata_label, already_defined_metadata=already_defined_metadata)
        print("The response of DataApi->api_v6_data_metadatavalues_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->api_v6_data_metadatavalues_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rigid_path** | **str**| Rigid path | [optional] 
 **metadata_label** | **str**| Metadata label for which to retrieve suggested values | [optional] 
 **already_defined_metadata** | [**List[AlreadyDefinedMetadata]**](AlreadyDefinedMetadata.md)| Already defined text metadata values along the branch | [optional] 

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v6_data_units_get**
> List[DataUnit] api_v6_data_units_get(position=position, endpoint=endpoint)

Provides the units for the endpoint at the given endpoint tree position

### Example


```python
import openapi_client
from openapi_client.models.data_unit import DataUnit
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
    api_instance = openapi_client.DataApi(api_client)
    position = 'position_example' # str | A #-delimited endpoint tree position (optional)
    endpoint = 'endpoint_example' # str | The name of the endpoint (optional)

    try:
        # Provides the units for the endpoint at the given endpoint tree position
        api_response = api_instance.api_v6_data_units_get(position=position, endpoint=endpoint)
        print("The response of DataApi->api_v6_data_units_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataApi->api_v6_data_units_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position** | **str**| A #-delimited endpoint tree position | [optional] 
 **endpoint** | **str**| The name of the endpoint | [optional] 

### Return type

[**List[DataUnit]**](DataUnit.md)

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

