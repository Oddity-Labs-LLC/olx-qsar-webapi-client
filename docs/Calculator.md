# Calculator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **str** | Caption of the Toolbox Object | [optional] 
**guid** | **str** | Unique identifier of the Toolbox Object | [optional] 
**units** | **str** | Default units of the parameter | [optional] 
**is3_d** | **bool** | Indicates whether this is a 3D parameter | [optional] 
**is_experimental** | **bool** | Indicates whether this is a parameter related to observed (experimental) data | [optional] 
**description** | **str** | Descriptive information about the parameter | [optional] 

## Example

```python
from openapi_client.models.calculator import Calculator

# TODO update the JSON string below
json = "{}"
# create an instance of Calculator from a JSON string
calculator_instance = Calculator.from_json(json)
# print the JSON string representation of the object
print(Calculator.to_json())

# convert the object into a dict
calculator_dict = calculator_instance.to_dict()
# create an instance of Calculator from a dict
calculator_from_dict = Calculator.from_dict(calculator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


