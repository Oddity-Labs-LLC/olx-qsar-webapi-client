# coding: utf-8

"""
    Toolbox WebAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.data_point import DataPoint

class TestDataPoint(unittest.TestCase):
    """DataPoint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataPoint:
        """Test DataPoint
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataPoint`
        """
        model = DataPoint()
        if include_optional:
            return DataPoint(
                data_type = '',
                rigid_path = '',
                endpoint = '',
                meta_data = [
                    ''
                    ],
                value = '',
                qualifier = '',
                min_value = '',
                min_qualifier = '',
                max_value = '',
                max_qualifier = '',
                unit = '',
                family = ''
            )
        else:
            return DataPoint(
        )
        """

    def testDataPoint(self):
        """Test DataPoint"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
