#! /usr/bin/env python

"""
Copyright (c) 2004-Present Pivotal Software, Inc.

This program and the accompanying materials are made available under
the terms of the under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from unittest2.main import USAGE_AS_MAIN
import tinctest

tinctest.TINCTestProgram.USAGE = USAGE_AS_MAIN
tinctest.TINCTestProgram(module = None, 
                testLoader = tinctest.default_test_loader,
                testRunner = tinctest.TINCTestRunner)