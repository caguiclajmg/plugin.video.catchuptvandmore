# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import *
import sys
import mock

mock_codequick = mock.MagicMock()

# Say to Python that the codequick module is mock_codequick
sys.modules['codequick'] = mock_codequick
