# IuclidResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chemical** | [**IChemIUCLID**](IChemIUCLID.md) |  | [optional] 
**echa_entity_url** | **str** |  | [optional] 
**echa_section_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.iuclid_result import IuclidResult

# TODO update the JSON string below
json = "{}"
# create an instance of IuclidResult from a JSON string
iuclid_result_instance = IuclidResult.from_json(json)
# print the JSON string representation of the object
print(IuclidResult.to_json())

# convert the object into a dict
iuclid_result_dict = iuclid_result_instance.to_dict()
# create an instance of IuclidResult from a dict
iuclid_result_from_dict = IuclidResult.from_dict(iuclid_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


