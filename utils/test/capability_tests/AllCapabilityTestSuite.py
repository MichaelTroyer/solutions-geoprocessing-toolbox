# coding: utf-8
'''
-----------------------------------------------------------------------------
Copyright 2015 Esri
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-----------------------------------------------------------------------------

==================================================
AllCapabilityTestSuite.py
--------------------------------------------------
requirments:
* ArcGIS Desktop 10.X+ or ArcGIS Pro 1.X+
* Python 2.7 or Python 3.4
author: ArcGIS Solutions
company: Esri
==================================================
description:
This test suite collects all of the capability toolbox test suites:
* HelicopterLandingZoneToolsTestSuite.py
* ERGToolsTestSuite.py
* PointOfOriginToolsTestSuite.py

==================================================
history:
10/23/2015 - MF - placeholder
==================================================
'''

import unittest
import os
import HelicopterLandingZoneToolsTestSuite
import PointOfOriginToolsTestSuite
import ERGToolsTestSuite


class AllCapabilityTestSuite(unittest.TestSuite):
    ''' This class is a test suite collecting all of the capability toolbox test suites '''

    def runCapabilityTestSuite(self, testSuite, platform):
        '''  '''
        HelicopterLandingZoneToolsTestSuite.HelicopterLandingZoneTestSuite.runHLZTestSuite(testSuite, platform)

        #TODO: Add PointOfOriginTestSuite
        #TODO: Add ERGToolsTestSuite
