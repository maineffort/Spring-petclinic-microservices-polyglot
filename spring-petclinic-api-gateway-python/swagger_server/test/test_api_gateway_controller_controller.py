# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.owner_details import OwnerDetails  # noqa: E501
from swagger_server.test import BaseTestCase


class TestApiGatewayControllerController(BaseTestCase):
    """ApiGatewayControllerController integration test stubs"""

    def test_get_owner_details_using_get(self):
        """Test case for get_owner_details_using_get

        getOwnerDetails
        """
        response = self.client.open(
            '//owners/{ownerId}'.format(ownerId=56),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
