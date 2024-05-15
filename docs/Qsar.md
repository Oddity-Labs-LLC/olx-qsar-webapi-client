# Qsar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **str** | Caption of the Toolbox Object | [optional] 
**guid** | **str** | Unique identifier of the Toolbox Object | [optional] 
**position** | **str** |  | [optional] 
**donator** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.qsar import Qsar

# TODO update the JSON string below
json = "{}"
# create an instance of Qsar from a JSON string
qsar_instance = Qsar.from_json(json)
# print the JSON string representation of the object
print(Qsar.to_json())

# convert the object into a dict
qsar_dict = qsar_instance.to_dict()
# create an instance of Qsar from a dict
qsar_from_dict = Qsar.from_dict(qsar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


