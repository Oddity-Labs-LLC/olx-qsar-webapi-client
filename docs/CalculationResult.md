# CalculationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculator_guid** | **str** |  | [optional] 
**calculator_name** | **str** |  | [optional] 
**calculator_type** | **str** |  | [optional] 
**calculation** | [**DataEntry**](DataEntry.md) |  | [optional] 

## Example

```python
from openapi_client.models.calculation_result import CalculationResult

# TODO update the JSON string below
json = "{}"
# create an instance of CalculationResult from a JSON string
calculation_result_instance = CalculationResult.from_json(json)
# print the JSON string representation of the object
print(CalculationResult.to_json())

# convert the object into a dict
calculation_result_dict = calculation_result_instance.to_dict()
# create an instance of CalculationResult from a dict
calculation_result_from_dict = CalculationResult.from_dict(calculation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


