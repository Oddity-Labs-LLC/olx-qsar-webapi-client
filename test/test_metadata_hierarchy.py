# coding: utf-8

"""
    Toolbox WebAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 6.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.metadata_hierarchy import MetadataHierarchy

class TestMetadataHierarchy(unittest.TestCase):
    """MetadataHierarchy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MetadataHierarchy:
        """Test MetadataHierarchy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MetadataHierarchy`
        """
        model = MetadataHierarchy()
        if include_optional:
            return MetadataHierarchy(
                rigid_path = '',
                labels = [
                    openapi_client.models.metadata_label.MetadataLabel(
                        name = '', 
                        is_numeric = True, 
                        is_automatic = True, )
                    ]
            )
        else:
            return MetadataHierarchy(
        )
        """

    def testMetadataHierarchy(self):
        """Test MetadataHierarchy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()