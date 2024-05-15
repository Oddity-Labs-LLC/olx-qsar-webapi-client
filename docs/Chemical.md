# Chemical


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**substance_type** | [**SubstanceType**](SubstanceType.md) |  | [optional] 
**chem_id** | **str** | Id of the chemical in the QSAR Toolbox | [optional] 
**cas** | **int** | CAS# of the chemical | [optional] 
**ec_number** | **str** | EC Number | [optional] 
**smiles** | **str** | SMILES of the chemical | [optional] 
**names** | **List[str]** | Chemical name(s) | [optional] 
**cas_smiles_relation** | **str** | QA estimation of the CAS-SMILES relation | [optional] 

## Example

```python
from openapi_client.models.chemical import Chemical

# TODO update the JSON string below
json = "{}"
# create an instance of Chemical from a JSON string
chemical_instance = Chemical.from_json(json)
# print the JSON string representation of the object
print(Chemical.to_json())

# convert the object into a dict
chemical_dict = chemical_instance.to_dict()
# create an instance of Chemical from a dict
chemical_from_dict = Chemical.from_dict(chemical_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


