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
from kubernetes.client.models.v2alpha1_horizontal_pod_autoscaler_status import V2alpha1HorizontalPodAutoscalerStatus


class TestV2alpha1HorizontalPodAutoscalerStatus(unittest.TestCase):
    """ V2alpha1HorizontalPodAutoscalerStatus unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV2alpha1HorizontalPodAutoscalerStatus(self):
        """
        Test V2alpha1HorizontalPodAutoscalerStatus
        """
        model = kubernetes.client.models.v2alpha1_horizontal_pod_autoscaler_status.V2alpha1HorizontalPodAutoscalerStatus()


if __name__ == '__main__':
    unittest.main()
