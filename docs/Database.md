# Database


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Database ID | [optional] 
**name** | **str** | Database name | [optional] 
**type** | **str** | Database or Inventory | [optional] 
**url_base** | **str** | Url base of the host containing the IUCLID database | [optional] 

## Example

```python
from openapi_client.models.database import Database

# TODO update the JSON string below
json = "{}"
# create an instance of Database from a JSON string
database_instance = Database.from_json(json)
# print the JSON string representation of the object
print(Database.to_json())

# convert the object into a dict
database_dict = database_instance.to_dict()
# create an instance of Database from a dict
database_from_dict = Database.from_dict(database_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


