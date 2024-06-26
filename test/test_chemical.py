# coding: utf-8

"""
    Toolbox WebAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.chemical import Chemical

class TestChemical(unittest.TestCase):
    """Chemical unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Chemical:
        """Test Chemical
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Chemical`
        """
        model = Chemical()
        if include_optional:
            return Chemical(
                substance_type = 'Unknown',
                chem_id = '',
                cas = 56,
                ec_number = '',
                smiles = '',
                names = [
                    ''
                    ],
                cas_smiles_relation = ''
            )
        else:
            return Chemical(
        )
        """

    def testChemical(self):
        """Test Chemical"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
