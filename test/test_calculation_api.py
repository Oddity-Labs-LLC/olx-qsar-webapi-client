# coding: utf-8

"""
    Toolbox WebAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.calculation_api import CalculationApi


class TestCalculationApi(unittest.TestCase):
    """CalculationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CalculationApi()

    def tearDown(self) -> None:
        pass

    def test_api_v6_calculation_all_chem_id_get(self) -> None:
        """Test case for api_v6_calculation_all_chem_id_get

        Applies all available calculators to the given chemical
        """
        pass

    def test_api_v6_calculation_calculator_guid_chem_id_get(self) -> None:
        """Test case for api_v6_calculation_calculator_guid_chem_id_get

        Applies the given calculator to the given chemical
        """
        pass

    def test_api_v6_calculation_calculator_guid_info_get(self) -> None:
        """Test case for api_v6_calculation_calculator_guid_info_get

        """
        pass

    def test_api_v6_calculation_get(self) -> None:
        """Test case for api_v6_calculation_get

        Returns all available calculators
        """
        pass


if __name__ == '__main__':
    unittest.main()
