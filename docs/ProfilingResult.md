# ProfilingResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profiler_guid** | **str** |  | [optional] 
**profiler_name** | **str** |  | [optional] 
**profiler_type** | **str** |  | [optional] 
**categories** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.profiling_result import ProfilingResult

# TODO update the JSON string below
json = "{}"
# create an instance of ProfilingResult from a JSON string
profiling_result_instance = ProfilingResult.from_json(json)
# print the JSON string representation of the object
print(ProfilingResult.to_json())

# convert the object into a dict
profiling_result_dict = profiling_result_instance.to_dict()
# create an instance of ProfilingResult from a dict
profiling_result_from_dict = ProfilingResult.from_dict(profiling_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


