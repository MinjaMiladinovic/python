# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_flocker_volume_source import V1FlockerVolumeSource


class TestV1FlockerVolumeSource(unittest.TestCase):
    """ V1FlockerVolumeSource unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1FlockerVolumeSource(self):
        """
        Test V1FlockerVolumeSource
        """
        model = kubernetes.client.models.v1_flocker_volume_source.V1FlockerVolumeSource()


if __name__ == '__main__':
    unittest.main()
