# openapi_client.IuclidApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v6_iuclid_cas_cas_get**](IuclidApi.md#api_v6_iuclid_cas_cas_get) | **GET** /api/v6/iuclid/cas/{cas} | Find IUCLID entities by CAS Number
[**api_v6_iuclid_databases_get**](IuclidApi.md#api_v6_iuclid_databases_get) | **GET** /api/v6/iuclid/databases | Retrieve a list of databases with IUCLID imports
[**api_v6_iuclid_ecnumber_ecnumber_get**](IuclidApi.md#api_v6_iuclid_ecnumber_ecnumber_get) | **GET** /api/v6/iuclid/ecnumber/{ecnumber} | Find IUCLID entities by EC Number
[**api_v6_iuclid_name_get**](IuclidApi.md#api_v6_iuclid_name_get) | **GET** /api/v6/iuclid/name | Find IUCLID entities by Chemical name
[**api_v6_iuclid_smiles_is_subfragment_search_get**](IuclidApi.md#api_v6_iuclid_smiles_is_subfragment_search_get) | **GET** /api/v6/iuclid/smiles/{isSubfragmentSearch} | Find IUCLID entities by SMILES (exact or substructure)


# **api_v6_iuclid_cas_cas_get**
> List[IuclidResult] api_v6_iuclid_cas_cas_get(cas, entity=entity, section=section, substance_type=substance_type, sources=sources)

Find IUCLID entities by CAS Number

### Example


```python
import openapi_client
from openapi_client.models.iuclid_result import IuclidResult
from openapi_client.models.iuclid_search_entity import IuclidSearchEntity
from openapi_client.models.iuclid_search_section import IuclidSearchSection
from openapi_client.models.iuclid_search_substance_type import IuclidSearchSubstanceType
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
    api_instance = openapi_client.IuclidApi(api_client)
    cas = 56 # int | 
    entity = openapi_client.IuclidSearchEntity() # IuclidSearchEntity |  (optional)
    section = openapi_client.IuclidSearchSection() # IuclidSearchSection |  (optional)
    substance_type = openapi_client.IuclidSearchSubstanceType() # IuclidSearchSubstanceType |  (optional)
    sources = ['sources_example'] # List[str] |  (optional)

    try:
        # Find IUCLID entities by CAS Number
        api_response = api_instance.api_v6_iuclid_cas_cas_get(cas, entity=entity, section=section, substance_type=substance_type, sources=sources)
        print("The response of IuclidApi->api_v6_iuclid_cas_cas_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IuclidApi->api_v6_iuclid_cas_cas_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cas** | **int**|  | 
 **entity** | [**IuclidSearchEntity**](.md)|  | [optional] 
 **section** | [**IuclidSearchSection**](.md)|  | [optional] 
 **substance_type** | [**IuclidSearchSubstanceType**](.md)|  | [optional] 
 **sources** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[IuclidResult]**](IuclidResult.md)

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

# **api_v6_iuclid_databases_get**
> List[Database] api_v6_iuclid_databases_get()

Retrieve a list of databases with IUCLID imports

### Example


```python
import openapi_client
from openapi_client.models.database import Database
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
    api_instance = openapi_client.IuclidApi(api_client)

    try:
        # Retrieve a list of databases with IUCLID imports
        api_response = api_instance.api_v6_iuclid_databases_get()
        print("The response of IuclidApi->api_v6_iuclid_databases_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IuclidApi->api_v6_iuclid_databases_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Database]**](Database.md)

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

# **api_v6_iuclid_ecnumber_ecnumber_get**
> List[IuclidResult] api_v6_iuclid_ecnumber_ecnumber_get(ecnumber, entity=entity, section=section, substance_type=substance_type, sources=sources)

Find IUCLID entities by EC Number

### Example


```python
import openapi_client
from openapi_client.models.iuclid_result import IuclidResult
from openapi_client.models.iuclid_search_entity import IuclidSearchEntity
from openapi_client.models.iuclid_search_section import IuclidSearchSection
from openapi_client.models.iuclid_search_substance_type import IuclidSearchSubstanceType
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
    api_instance = openapi_client.IuclidApi(api_client)
    ecnumber = 56 # int | 
    entity = openapi_client.IuclidSearchEntity() # IuclidSearchEntity |  (optional)
    section = openapi_client.IuclidSearchSection() # IuclidSearchSection |  (optional)
    substance_type = openapi_client.IuclidSearchSubstanceType() # IuclidSearchSubstanceType |  (optional)
    sources = ['sources_example'] # List[str] |  (optional)

    try:
        # Find IUCLID entities by EC Number
        api_response = api_instance.api_v6_iuclid_ecnumber_ecnumber_get(ecnumber, entity=entity, section=section, substance_type=substance_type, sources=sources)
        print("The response of IuclidApi->api_v6_iuclid_ecnumber_ecnumber_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IuclidApi->api_v6_iuclid_ecnumber_ecnumber_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ecnumber** | **int**|  | 
 **entity** | [**IuclidSearchEntity**](.md)|  | [optional] 
 **section** | [**IuclidSearchSection**](.md)|  | [optional] 
 **substance_type** | [**IuclidSearchSubstanceType**](.md)|  | [optional] 
 **sources** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[IuclidResult]**](IuclidResult.md)

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

# **api_v6_iuclid_name_get**
> List[IuclidResult] api_v6_iuclid_name_get(name=name, entity=entity, section=section, substance_type=substance_type, sources=sources)

Find IUCLID entities by Chemical name

### Example


```python
import openapi_client
from openapi_client.models.iuclid_result import IuclidResult
from openapi_client.models.iuclid_search_entity import IuclidSearchEntity
from openapi_client.models.iuclid_search_section import IuclidSearchSection
from openapi_client.models.iuclid_search_substance_type import IuclidSearchSubstanceType
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
    api_instance = openapi_client.IuclidApi(api_client)
    name = 'name_example' # str |  (optional)
    entity = openapi_client.IuclidSearchEntity() # IuclidSearchEntity |  (optional)
    section = openapi_client.IuclidSearchSection() # IuclidSearchSection |  (optional)
    substance_type = openapi_client.IuclidSearchSubstanceType() # IuclidSearchSubstanceType |  (optional)
    sources = ['sources_example'] # List[str] |  (optional)

    try:
        # Find IUCLID entities by Chemical name
        api_response = api_instance.api_v6_iuclid_name_get(name=name, entity=entity, section=section, substance_type=substance_type, sources=sources)
        print("The response of IuclidApi->api_v6_iuclid_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IuclidApi->api_v6_iuclid_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **entity** | [**IuclidSearchEntity**](.md)|  | [optional] 
 **section** | [**IuclidSearchSection**](.md)|  | [optional] 
 **substance_type** | [**IuclidSearchSubstanceType**](.md)|  | [optional] 
 **sources** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[IuclidResult]**](IuclidResult.md)

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

# **api_v6_iuclid_smiles_is_subfragment_search_get**
> List[IuclidResult] api_v6_iuclid_smiles_is_subfragment_search_get(is_subfragment_search, smiles=smiles, entity=entity, section=section, substance_type=substance_type, sources=sources)

Find IUCLID entities by SMILES (exact or substructure)

### Example


```python
import openapi_client
from openapi_client.models.iuclid_result import IuclidResult
from openapi_client.models.iuclid_search_entity import IuclidSearchEntity
from openapi_client.models.iuclid_search_section import IuclidSearchSection
from openapi_client.models.iuclid_search_substance_type import IuclidSearchSubstanceType
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
    api_instance = openapi_client.IuclidApi(api_client)
    is_subfragment_search = True # bool | 
    smiles = 'smiles_example' # str |  (optional)
    entity = openapi_client.IuclidSearchEntity() # IuclidSearchEntity |  (optional)
    section = openapi_client.IuclidSearchSection() # IuclidSearchSection |  (optional)
    substance_type = openapi_client.IuclidSearchSubstanceType() # IuclidSearchSubstanceType |  (optional)
    sources = ['sources_example'] # List[str] |  (optional)

    try:
        # Find IUCLID entities by SMILES (exact or substructure)
        api_response = api_instance.api_v6_iuclid_smiles_is_subfragment_search_get(is_subfragment_search, smiles=smiles, entity=entity, section=section, substance_type=substance_type, sources=sources)
        print("The response of IuclidApi->api_v6_iuclid_smiles_is_subfragment_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IuclidApi->api_v6_iuclid_smiles_is_subfragment_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_subfragment_search** | **bool**|  | 
 **smiles** | **str**|  | [optional] 
 **entity** | [**IuclidSearchEntity**](.md)|  | [optional] 
 **section** | [**IuclidSearchSection**](.md)|  | [optional] 
 **substance_type** | [**IuclidSearchSubstanceType**](.md)|  | [optional] 
 **sources** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**List[IuclidResult]**](IuclidResult.md)

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

