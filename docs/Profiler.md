# Profiler


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **str** | Caption of the Toolbox Object | [optional] 
**guid** | **str** | Unique identifier of the Toolbox Object | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.profiler import Profiler

# TODO update the JSON string below
json = "{}"
# create an instance of Profiler from a JSON string
profiler_instance = Profiler.from_json(json)
# print the JSON string representation of the object
print(Profiler.to_json())

# convert the object into a dict
profiler_dict = profiler_instance.to_dict()
# create an instance of Profiler from a dict
profiler_from_dict = Profiler.from_dict(profiler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


