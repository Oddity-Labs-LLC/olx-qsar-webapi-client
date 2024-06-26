# coding: utf-8

"""
    Toolbox WebAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.metabolism_api import MetabolismApi


class TestMetabolismApi(unittest.TestCase):
    """MetabolismApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MetabolismApi()

    def tearDown(self) -> None:
        pass

    def test_api_v6_metabolism_get(self) -> None:
        """Test case for api_v6_metabolism_get

        Requests all available simulators
        """
        pass

    def test_api_v6_metabolism_simulator_guid_chem_id_get(self) -> None:
        """Test case for api_v6_metabolism_simulator_guid_chem_id_get

        Applies the given simulator to the given chemical returning the produced metabolites
        """
        pass

    def test_api_v6_metabolism_simulator_guid_get(self) -> None:
        """Test case for api_v6_metabolism_simulator_guid_get

        Applies the given simulator to the given SMILES returning the produced metabolites
        """
        pass

    def test_api_v6_metabolism_simulator_guid_info_get(self) -> None:
        """Test case for api_v6_metabolism_simulator_guid_info_get

        Provides general information for the specified simulator
        """
        pass


if __name__ == '__main__':
    unittest.main()
