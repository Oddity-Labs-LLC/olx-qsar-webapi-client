# openapi_client.SearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v6_search_cas_cas_ignore_stereo_get**](SearchApi.md#api_v6_search_cas_cas_ignore_stereo_get) | **GET** /api/v6/search/cas/{cas}/{ignoreStereo} | Performs a search by CAS number
[**api_v6_search_chemical_chem_id_get**](SearchApi.md#api_v6_search_chemical_chem_id_get) | **GET** /api/v6/search/chemical/{chemId} | Returns a chemical structure from the provided chemId containing CAS# and Smiles
[**api_v6_search_databases_get**](SearchApi.md#api_v6_search_databases_get) | **GET** /api/v6/search/databases | Lists all databases and inventories
[**api_v6_search_ecnumber_ecnumber_ignore_stereo_get**](SearchApi.md#api_v6_search_ecnumber_ecnumber_ignore_stereo_get) | **GET** /api/v6/search/ecnumber/{ecnumber}/{ignoreStereo} | Performs a search by EC number
[**api_v6_search_name_name_options_ignore_stereo_get**](SearchApi.md#api_v6_search_name_name_options_ignore_stereo_get) | **GET** /api/v6/search/name/{name}/{options}/{ignoreStereo} | Performs a search by name
[**api_v6_search_smiles_register_unknown_ignore_stereo_get**](SearchApi.md#api_v6_search_smiles_register_unknown_ignore_stereo_get) | **GET** /api/v6/search/smiles/{registerUnknown}/{ignoreStereo} | Performs a search by SMILES and returns a SmilesSearchResult object as a result


# **api_v6_search_cas_cas_ignore_stereo_get**
> List[Chemical] api_v6_search_cas_cas_ignore_stereo_get(cas, ignore_stereo)

Performs a search by CAS number

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
    api_instance = openapi_client.SearchApi(api_client)
    cas = 56 # int | The CAS to search for
    ignore_stereo = True # bool | When true, stereo information will be ignored (default to True)

    try:
        # Performs a search by CAS number
        api_response = api_instance.api_v6_search_cas_cas_ignore_stereo_get(cas, ignore_stereo)
        print("The response of SearchApi->api_v6_search_cas_cas_ignore_stereo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->api_v6_search_cas_cas_ignore_stereo_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cas** | **int**| The CAS to search for | 
 **ignore_stereo** | **bool**| When true, stereo information will be ignored | [default to True]

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

# **api_v6_search_chemical_chem_id_get**
> Chemical api_v6_search_chemical_chem_id_get(chem_id)

Returns a chemical structure from the provided chemId containing CAS# and Smiles

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
    api_instance = openapi_client.SearchApi(api_client)
    chem_id = 'chem_id_example' # str | The chemical id to search for

    try:
        # Returns a chemical structure from the provided chemId containing CAS# and Smiles
        api_response = api_instance.api_v6_search_chemical_chem_id_get(chem_id)
        print("The response of SearchApi->api_v6_search_chemical_chem_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->api_v6_search_chemical_chem_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chem_id** | **str**| The chemical id to search for | 

### Return type

[**Chemical**](Chemical.md)

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

# **api_v6_search_databases_get**
> List[Database] api_v6_search_databases_get()

Lists all databases and inventories

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
    api_instance = openapi_client.SearchApi(api_client)

    try:
        # Lists all databases and inventories
        api_response = api_instance.api_v6_search_databases_get()
        print("The response of SearchApi->api_v6_search_databases_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->api_v6_search_databases_get: %s\n" % e)
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

# **api_v6_search_ecnumber_ecnumber_ignore_stereo_get**
> List[Chemical] api_v6_search_ecnumber_ecnumber_ignore_stereo_get(ecnumber, ignore_stereo)

Performs a search by EC number

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
    api_instance = openapi_client.SearchApi(api_client)
    ecnumber = 56 # int | The EC to search for
    ignore_stereo = True # bool | When true, stereo information will be ignored (default to True)

    try:
        # Performs a search by EC number
        api_response = api_instance.api_v6_search_ecnumber_ecnumber_ignore_stereo_get(ecnumber, ignore_stereo)
        print("The response of SearchApi->api_v6_search_ecnumber_ecnumber_ignore_stereo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->api_v6_search_ecnumber_ecnumber_ignore_stereo_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ecnumber** | **int**| The EC to search for | 
 **ignore_stereo** | **bool**| When true, stereo information will be ignored | [default to True]

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

# **api_v6_search_name_name_options_ignore_stereo_get**
> List[Chemical] api_v6_search_name_name_options_ignore_stereo_get(name, options, ignore_stereo)

Performs a search by name

### Example


```python
import openapi_client
from openapi_client.models.chemical import Chemical
from openapi_client.models.search_name_options import SearchNameOptions
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
    api_instance = openapi_client.SearchApi(api_client)
    name = 'name_example' # str | The name to search for
    options = openapi_client.SearchNameOptions() # SearchNameOptions | 0 - ExactMatch, 1 - StartsWith, 2 - Contains
    ignore_stereo = True # bool | When true, stereo information will be ignored (default to True)

    try:
        # Performs a search by name
        api_response = api_instance.api_v6_search_name_name_options_ignore_stereo_get(name, options, ignore_stereo)
        print("The response of SearchApi->api_v6_search_name_name_options_ignore_stereo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->api_v6_search_name_name_options_ignore_stereo_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name to search for | 
 **options** | [**SearchNameOptions**](.md)| 0 - ExactMatch, 1 - StartsWith, 2 - Contains | 
 **ignore_stereo** | **bool**| When true, stereo information will be ignored | [default to True]

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

# **api_v6_search_smiles_register_unknown_ignore_stereo_get**
> List[Chemical] api_v6_search_smiles_register_unknown_ignore_stereo_get(register_unknown, ignore_stereo, smiles=smiles)

Performs a search by SMILES and returns a SmilesSearchResult object as a result

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
    api_instance = openapi_client.SearchApi(api_client)
    register_unknown = True # bool | When true, unknown structures will be added to the database
    ignore_stereo = True # bool | When true, stereo information will be ignored
    smiles = 'smiles_example' # str | The smiles to search for (optional)

    try:
        # Performs a search by SMILES and returns a SmilesSearchResult object as a result
        api_response = api_instance.api_v6_search_smiles_register_unknown_ignore_stereo_get(register_unknown, ignore_stereo, smiles=smiles)
        print("The response of SearchApi->api_v6_search_smiles_register_unknown_ignore_stereo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->api_v6_search_smiles_register_unknown_ignore_stereo_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_unknown** | **bool**| When true, unknown structures will be added to the database | 
 **ignore_stereo** | **bool**| When true, stereo information will be ignored | 
 **smiles** | **str**| The smiles to search for | [optional] 

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

