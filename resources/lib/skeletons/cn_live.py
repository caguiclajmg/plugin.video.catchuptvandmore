# -*- coding: utf-8 -*-
"""
    Catch-up TV & More
    Copyright (C) 2016  SylvainCecchetto

    This file is part of Catch-up TV & More.

    Catch-up TV & More is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    Catch-up TV & More is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with Catch-up TV & More; if not, write to the Free Software Foundation,
    Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

# The unicode_literals import only has
# an effect on Python 2.
# It makes string literals as unicode like in Python 3
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from resources.lib.hack_future import install_aliases
install_aliases()
from builtins import *
from codequick import Script
"""
The following dictionaries describe
the addon's tree architecture.
* Key: item id
* Value: item infos
    - callback: Callback function to run once this item is selected
    - thumb: Item thumb path relative to "media" folder
    - fanart: Item fanart path relative to "meia" folder
    - module: Item module to load in order to work (like 6play.py)
"""

menu = {
    'cctv1': {
        'callback': 'live_bridge',
        'thumb': 'channels/cn/cctv1.png',
        'fanart': 'channels/cn/cctv1_fanart.jpg',
        'module': 'resources.lib.channels.cn.cctv'
    },
    'cctv2': {
        'callback': 'live_bridge',
        'thumb': 'channels/cn/cctv2.png',
        'fanart': 'channels/cn/cctv2_fanart.jpg',
        'module': 'resources.lib.channels.cn.cctv'
    },
    'cctv3': {
        'callback': 'live_bridge',
        'thumb': 'channels/cn/cctv3.png',
        'fanart': 'channels/cn/cctv3_fanart.jpg',
        'module': 'resources.lib.channels.cn.cctv'
    },
    'cctv4': {
        'callback': 'live_bridge',
        'thumb': 'channels/cn/cctv4.png',
        'fanart': 'channels/cn/cctv4_fanart.jpg',
        'module': 'resources.lib.channels.cn.cctv'
    },
    'cctveurope': {
        'callback': 'live_bridge',
        'thumb': 'channels/cn/cctveurope.png',
        'fanart': 'channels/cn/cctveurope_fanart.jpg',
        'module': 'resources.lib.channels.cn.cctv'
    },
    'cctvamerica': {
        'callback': 'live_bridge',
        'thumb': 'channels/cn/cctvamerica.png',
        'fanart': 'channels/cn/cctvamerica_fanart.jpg',
        'module': 'resources.lib.channels.cn.cctv'
    },
    'cctv5': {
        'callback': 'live_bridge',
        'thumb': 'channels/cn/cctv5.png',
        'fanart': 'channels/cn/cctv5_fanart.jpg',
        'module': 'resources.lib.channels.cn.cctv'
    },
    'cctv5plus': {
        'callback': 'live_bridge',
        'thumb': 'channels/cn/cctv5plus.png',
        'fanart': 'channels/cn/cctv5plus_fanart.jpg',
        'module': 'resources.lib.channels.cn.cctv'
    },
    'cctv6': {
        'callback': 'live_bridge',
        'thumb': 'channels/cn/cctv6.png',
        'fanart': 'channels/cn/cctv6_fanart.jpg',
        'module': 'resources.lib.channels.cn.cctv'
    },
    'cctv7': {
        'callback': 'live_bridge',
        'thumb': 'channels/cn/cctv7.png',
        'fanart': 'channels/cn/cctv7_fanart.jpg',
        'module': 'resources.lib.channels.cn.cctv'
    },
    'cctv8': {
        'callback': 'live_bridge',
        'thumb': 'channels/cn/cctv8.png',
        'fanart': 'channels/cn/cctv8_fanart.jpg',
        'module': 'resources.lib.channels.cn.cctv'
    },
    'cctvjilu': {
        'callback': 'live_bridge',
        'thumb': 'channels/cn/cctvjilu.png',
        'fanart': 'channels/cn/cctvjilu_fanart.jpg',
        'module': 'resources.lib.channels.cn.cctv'
    },
    'cctv10': {
        'callback': 'live_bridge',
        'thumb': 'channels/cn/cctv10.png',
        'fanart': 'channels/cn/cctv10_fanart.jpg',
        'module': 'resources.lib.channels.cn.cctv'
    },
    'cctv11': {
        'callback': 'live_bridge',
        'thumb': 'channels/cn/cctv11.png',
        'fanart': 'channels/cn/cctv11_fanart.jpg',
        'module': 'resources.lib.channels.cn.cctv'
    },
    'cctv12': {
        'callback': 'live_bridge',
        'thumb': 'channels/cn/cctv12.png',
        'fanart': 'channels/cn/cctv12_fanart.jpg',
        'module': 'resources.lib.channels.cn.cctv'
    },
    'cctv13': {
        'callback': 'live_bridge',
        'thumb': 'channels/cn/cctv13.png',
        'fanart': 'channels/cn/cctv13_fanart.jpg',
        'module': 'resources.lib.channels.cn.cctv'
    },
    'cctvchild': {
        'callback': 'live_bridge',
        'thumb': 'channels/cn/cctvchild.png',
        'fanart': 'channels/cn/cctvchild_fanart.jpg',
        'module': 'resources.lib.channels.cn.cctv'
    },
    'cctv15': {
        'callback': 'live_bridge',
        'thumb': 'channels/cn/cctv15.png',
        'fanart': 'channels/cn/cctv15_fanart.jpg',
        'module': 'resources.lib.channels.cn.cctv'
    }
}
