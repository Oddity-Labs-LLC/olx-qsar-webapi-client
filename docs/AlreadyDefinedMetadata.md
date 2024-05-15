# AlreadyDefinedMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Metadata label with defined values, e.g. \&quot;Endpoint\&quot; | [optional] 
**values** | **List[str]** | Already defined metadata values by the user.  The TE dialog can be configured to accept multiple OR-ed values by the user hence we expect a collection of strings | [optional] 

## Example

```python
from openapi_client.models.already_defined_metadata import AlreadyDefinedMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AlreadyDefinedMetadata from a JSON string
already_defined_metadata_instance = AlreadyDefinedMetadata.from_json(json)
# print the JSON string representation of the object
print(AlreadyDefinedMetadata.to_json())

# convert the object into a dict
already_defined_metadata_dict = already_defined_metadata_instance.to_dict()
# create an instance of AlreadyDefinedMetadata from a dict
already_defined_metadata_from_dict = AlreadyDefinedMetadata.from_dict(already_defined_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


