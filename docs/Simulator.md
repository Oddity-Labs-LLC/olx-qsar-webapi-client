# Simulator

A representation of a metabolism simulator

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **str** | Caption of the Toolbox Object | [optional] 
**guid** | **str** | Unique identifier of the Toolbox Object | [optional] 
**is_observed** | **bool** | Boolean indicating whether this is Observed (documented) or Simmulated metabolism | [optional] 
**product_name** | **str** | Common name of the generated metabolites | [optional] 

## Example

```python
from openapi_client.models.simulator import Simulator

# TODO update the JSON string below
json = "{}"
# create an instance of Simulator from a JSON string
simulator_instance = Simulator.from_json(json)
# print the JSON string representation of the object
print(Simulator.to_json())

# convert the object into a dict
simulator_dict = simulator_instance.to_dict()
# create an instance of Simulator from a dict
simulator_from_dict = Simulator.from_dict(simulator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


