# openapi-client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 6.0
- Package version: 1.0.0
- Generator version: 7.5.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
    api_instance = openapi_client.AboutApi(api_client)
    object_guid = 'object_guid_example' # str | GUID of the Toolbox object

    try:
        # Provides general information for the specified Toolbox object
        api_response = api_instance.api_v6_about_object_object_guid_get(object_guid)
        print("The response of AboutApi->api_v6_about_object_object_guid_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AboutApi->api_v6_about_object_object_guid_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AboutApi* | [**api_v6_about_object_object_guid_get**](docs/AboutApi.md#api_v6_about_object_object_guid_get) | **GET** /api/v6/about/object/{objectGuid} | Provides general information for the specified Toolbox object
*CalculationApi* | [**api_v6_calculation_all_chem_id_get**](docs/CalculationApi.md#api_v6_calculation_all_chem_id_get) | **GET** /api/v6/calculation/all/{chemId} | Applies all available calculators to the given chemical
*CalculationApi* | [**api_v6_calculation_calculator_guid_chem_id_get**](docs/CalculationApi.md#api_v6_calculation_calculator_guid_chem_id_get) | **GET** /api/v6/calculation/{calculatorGuid}/{chemId} | Applies the given calculator to the given chemical
*CalculationApi* | [**api_v6_calculation_calculator_guid_info_get**](docs/CalculationApi.md#api_v6_calculation_calculator_guid_info_get) | **GET** /api/v6/calculation/{calculatorGuid}/info | 
*CalculationApi* | [**api_v6_calculation_get**](docs/CalculationApi.md#api_v6_calculation_get) | **GET** /api/v6/calculation | Returns all available calculators
*DataApi* | [**api_v6_data_all_chem_id_get**](docs/DataApi.md#api_v6_data_all_chem_id_get) | **GET** /api/v6/data/all/{chemId} | Retrieves all data for the selected chemical
*DataApi* | [**api_v6_data_chem_id_get**](docs/DataApi.md#api_v6_data_chem_id_get) | **GET** /api/v6/data/{chemId} | Retrieves data for the specified endpoint at the given position for the selected chemical
*DataApi* | [**api_v6_data_databases_get**](docs/DataApi.md#api_v6_data_databases_get) | **GET** /api/v6/data/databases | Retrieves a list with databases containing data for the specified endpoint
*DataApi* | [**api_v6_data_endpoint_get**](docs/DataApi.md#api_v6_data_endpoint_get) | **GET** /api/v6/data/endpoint | Retrieves all endpoints available at the given position of the endpoint tree
*DataApi* | [**api_v6_data_endpointtree_get**](docs/DataApi.md#api_v6_data_endpointtree_get) | **GET** /api/v6/data/endpointtree | Returns the entire endpoint tree
*DataApi* | [**api_v6_data_metadatahierarchy_get**](docs/DataApi.md#api_v6_data_metadatahierarchy_get) | **GET** /api/v6/data/metadatahierarchy | Returns the default metadata hierarchy in one call (optimization)
*DataApi* | [**api_v6_data_metadatavalues_post**](docs/DataApi.md#api_v6_data_metadatavalues_post) | **POST** /api/v6/data/metadatavalues | Returns the suggested metadata values for a given metadata label based on the already defined ones (in the same branch)
*DataApi* | [**api_v6_data_units_get**](docs/DataApi.md#api_v6_data_units_get) | **GET** /api/v6/data/units | Provides the units for the endpoint at the given endpoint tree position
*ExportApi* | [**api_v6_export_list_smi_get**](docs/ExportApi.md#api_v6_export_list_smi_get) | **GET** /api/v6/export/list/smi | Exports the given chemicals as a .smi text file
*GroupingApi* | [**api_v6_grouping_chem_id_profiler_guid_get**](docs/GroupingApi.md#api_v6_grouping_chem_id_profiler_guid_get) | **GET** /api/v6/grouping/{chemId}/{profilerGuid} | Creates a group of chemicals from the given databases having same profiles as the target chemical by the specified profiler
*IuclidApi* | [**api_v6_iuclid_cas_cas_get**](docs/IuclidApi.md#api_v6_iuclid_cas_cas_get) | **GET** /api/v6/iuclid/cas/{cas} | Find IUCLID entities by CAS Number
*IuclidApi* | [**api_v6_iuclid_databases_get**](docs/IuclidApi.md#api_v6_iuclid_databases_get) | **GET** /api/v6/iuclid/databases | Retrieve a list of databases with IUCLID imports
*IuclidApi* | [**api_v6_iuclid_ecnumber_ecnumber_get**](docs/IuclidApi.md#api_v6_iuclid_ecnumber_ecnumber_get) | **GET** /api/v6/iuclid/ecnumber/{ecnumber} | Find IUCLID entities by EC Number
*IuclidApi* | [**api_v6_iuclid_name_get**](docs/IuclidApi.md#api_v6_iuclid_name_get) | **GET** /api/v6/iuclid/name | Find IUCLID entities by Chemical name
*IuclidApi* | [**api_v6_iuclid_smiles_is_subfragment_search_get**](docs/IuclidApi.md#api_v6_iuclid_smiles_is_subfragment_search_get) | **GET** /api/v6/iuclid/smiles/{isSubfragmentSearch} | Find IUCLID entities by SMILES (exact or substructure)
*MetabolismApi* | [**api_v6_metabolism_get**](docs/MetabolismApi.md#api_v6_metabolism_get) | **GET** /api/v6/metabolism | Requests all available simulators
*MetabolismApi* | [**api_v6_metabolism_simulator_guid_chem_id_get**](docs/MetabolismApi.md#api_v6_metabolism_simulator_guid_chem_id_get) | **GET** /api/v6/metabolism/{simulatorGuid}/{chemId} | Applies the given simulator to the given chemical returning the produced metabolites
*MetabolismApi* | [**api_v6_metabolism_simulator_guid_get**](docs/MetabolismApi.md#api_v6_metabolism_simulator_guid_get) | **GET** /api/v6/metabolism/{simulatorGuid} | Applies the given simulator to the given SMILES returning the produced metabolites
*MetabolismApi* | [**api_v6_metabolism_simulator_guid_info_get**](docs/MetabolismApi.md#api_v6_metabolism_simulator_guid_info_get) | **GET** /api/v6/metabolism/{simulatorGuid}/info | Provides general information for the specified simulator
*ProfilingApi* | [**api_v6_profiling_all_chem_id_get**](docs/ProfilingApi.md#api_v6_profiling_all_chem_id_get) | **GET** /api/v6/profiling/all/{chemId} | Profiles the provided chemical with all available profilers
*ProfilingApi* | [**api_v6_profiling_get**](docs/ProfilingApi.md#api_v6_profiling_get) | **GET** /api/v6/profiling | Requests all available profilers
*ProfilingApi* | [**api_v6_profiling_profiler_guid_chem_id_simulator_guid_get**](docs/ProfilingApi.md#api_v6_profiling_profiler_guid_chem_id_simulator_guid_get) | **GET** /api/v6/profiling/{profilerGuid}/{chemId}/{simulatorGuid} | Profiles the provided chemical with the specified profiler
*ProfilingApi* | [**api_v6_profiling_profiler_guid_get**](docs/ProfilingApi.md#api_v6_profiling_profiler_guid_get) | **GET** /api/v6/profiling/{profilerGuid} | Returns all of the available categories for a provided profiler
*ProfilingApi* | [**api_v6_profiling_profiler_guid_info_get**](docs/ProfilingApi.md#api_v6_profiling_profiler_guid_info_get) | **GET** /api/v6/profiling/{profilerGuid}/info | Provides general information for the specified profiler
*ProfilingApi* | [**api_v6_profiling_profiler_guid_literature_get**](docs/ProfilingApi.md#api_v6_profiling_profiler_guid_literature_get) | **GET** /api/v6/profiling/{profilerGuid}/literature | Provides literature for the given category in the specified profiler
*ProfilingApi* | [**api_v6_profiling_relevancies_get**](docs/ProfilingApi.md#api_v6_profiling_relevancies_get) | **GET** /api/v6/profiling/relevancies | Requests profiles that are relevant to the specified endpoint position and metadata
*QsarApi* | [**api_v6_qsar_apply_qsar_guid_chem_id_get**](docs/QsarApi.md#api_v6_qsar_apply_qsar_guid_chem_id_get) | **GET** /api/v6/qsar/apply/{qsarGuid}/{chemId} | Applies the specified QSAR model onto the provided chemical
*QsarApi* | [**api_v6_qsar_domain_qsar_guid_chem_id_get**](docs/QsarApi.md#api_v6_qsar_domain_qsar_guid_chem_id_get) | **GET** /api/v6/qsar/domain/{qsarGuid}/{chemId} | Checks whether the chemicals falls within the domain of the specified QSAR model
*QsarApi* | [**api_v6_qsar_list_position_get**](docs/QsarApi.md#api_v6_qsar_list_position_get) | **GET** /api/v6/qsar/list/{position} | Retrieves all QSAR models that are associated to the provided position of the endpoint tree
*SearchApi* | [**api_v6_search_cas_cas_ignore_stereo_get**](docs/SearchApi.md#api_v6_search_cas_cas_ignore_stereo_get) | **GET** /api/v6/search/cas/{cas}/{ignoreStereo} | Performs a search by CAS number
*SearchApi* | [**api_v6_search_chemical_chem_id_get**](docs/SearchApi.md#api_v6_search_chemical_chem_id_get) | **GET** /api/v6/search/chemical/{chemId} | Returns a chemical structure from the provided chemId containing CAS# and Smiles
*SearchApi* | [**api_v6_search_databases_get**](docs/SearchApi.md#api_v6_search_databases_get) | **GET** /api/v6/search/databases | Lists all databases and inventories
*SearchApi* | [**api_v6_search_ecnumber_ecnumber_ignore_stereo_get**](docs/SearchApi.md#api_v6_search_ecnumber_ecnumber_ignore_stereo_get) | **GET** /api/v6/search/ecnumber/{ecnumber}/{ignoreStereo} | Performs a search by EC number
*SearchApi* | [**api_v6_search_name_name_options_ignore_stereo_get**](docs/SearchApi.md#api_v6_search_name_name_options_ignore_stereo_get) | **GET** /api/v6/search/name/{name}/{options}/{ignoreStereo} | Performs a search by name
*SearchApi* | [**api_v6_search_smiles_register_unknown_ignore_stereo_get**](docs/SearchApi.md#api_v6_search_smiles_register_unknown_ignore_stereo_get) | **GET** /api/v6/search/smiles/{registerUnknown}/{ignoreStereo} | Performs a search by SMILES and returns a SmilesSearchResult object as a result
*StructureApi* | [**api_v6_structure_canonize_get**](docs/StructureApi.md#api_v6_structure_canonize_get) | **GET** /api/v6/structure/canonize | Returns the canonized version of the provided smiles
*StructureApi* | [**api_v6_structure_connectivity_get**](docs/StructureApi.md#api_v6_structure_connectivity_get) | **GET** /api/v6/structure/connectivity | Returns connectivity string for the supplied smiles
*WorkflowsApi* | [**api_v6_workflows_get**](docs/WorkflowsApi.md#api_v6_workflows_get) | **GET** /api/v6/workflows | Requests all available workflows
*WorkflowsApi* | [**api_v6_workflows_workflow_guid_chem_id_get**](docs/WorkflowsApi.md#api_v6_workflows_workflow_guid_chem_id_get) | **GET** /api/v6/workflows/{workflowGuid}/{chemId} | Executes a workflow with a given chemical


## Documentation For Models

 - [AboutTextPair](docs/AboutTextPair.md)
 - [AlreadyDefinedMetadata](docs/AlreadyDefinedMetadata.md)
 - [CalculationResult](docs/CalculationResult.md)
 - [Calculator](docs/Calculator.md)
 - [Chemical](docs/Chemical.md)
 - [DataEntry](docs/DataEntry.md)
 - [DataPoint](docs/DataPoint.md)
 - [DataUnit](docs/DataUnit.md)
 - [Database](docs/Database.md)
 - [IChemIUCLID](docs/IChemIUCLID.md)
 - [ITbObjectAbout](docs/ITbObjectAbout.md)
 - [IUCLIDIdRawToolboxId](docs/IUCLIDIdRawToolboxId.md)
 - [IUCLIDIdType](docs/IUCLIDIdType.md)
 - [IuclidResult](docs/IuclidResult.md)
 - [IuclidSearchEntity](docs/IuclidSearchEntity.md)
 - [IuclidSearchSection](docs/IuclidSearchSection.md)
 - [IuclidSearchSubstanceType](docs/IuclidSearchSubstanceType.md)
 - [MetadataHierarchy](docs/MetadataHierarchy.md)
 - [MetadataLabel](docs/MetadataLabel.md)
 - [Profiler](docs/Profiler.md)
 - [ProfilingResult](docs/ProfilingResult.md)
 - [Qsar](docs/Qsar.md)
 - [RelevantProfiles](docs/RelevantProfiles.md)
 - [SearchNameOptions](docs/SearchNameOptions.md)
 - [Simulator](docs/Simulator.md)
 - [SubstanceType](docs/SubstanceType.md)
 - [ToolboxObjectAbout](docs/ToolboxObjectAbout.md)
 - [Workflow](docs/Workflow.md)
 - [WorkflowResult](docs/WorkflowResult.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




