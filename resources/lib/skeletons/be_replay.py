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
from future import standard_library
standard_library.install_aliases()
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
    'rtl_tvi': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/rtltvi.png',
        'fanart': 'channels/be/rtltvi_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe'
    },
    'plug_rtl': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/plugrtl.png',
        'fanart': 'channels/be/plugrtl_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe'
    },
    'club_rtl': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/clubrtl.png',
        'fanart': 'channels/be/clubrtl_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe'
    },
    'rtl_info': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/rtlinfo.png',
        'fanart': 'channels/be/rtlinfo_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe'
    },
    'bel_rtl': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/belrtl.png',
        'fanart': 'channels/be/belrtl_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe'
    },
    'contact': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/contact.png',
        'fanart': 'channels/be/contact_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe'
    },
    'rtl_sport': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/rtlsport.png',
        'fanart': 'channels/be/rtlsport_fanart.jpg',
        'module': 'resources.lib.channels.be.rtlplaybe'
    },
    'brf': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/brf.png',
        'fanart': 'channels/be/brf_fanart.jpg',
        'module': 'resources.lib.channels.be.brf'
    },
    'bx1': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/bx1.png',
        'fanart': 'channels/be/bx1_fanart.jpg',
        'module': 'resources.lib.channels.be.bx1'
    },
    'nrjhitstvbe': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/nrjhitstvbe.png',
        'fanart': 'channels/be/nrjhitstvbe_fanart.jpg',
        'module': 'resources.lib.channels.be.nrjhitstvbe'
    },
    'auvio': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/auvio.png',
        'fanart': 'channels/be/auvio_fanart.jpg',
        'module': 'resources.lib.channels.be.rtbf'
    },
    'rtc': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/rtc.png',
        'fanart': 'channels/be/rtc_fanart.jpg',
        'module': 'resources.lib.channels.be.rtc'
    },
    'telemb': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/telemb.png',
        'fanart': 'channels/be/telemb_fanart.jpg',
        'module': 'resources.lib.channels.be.telemb'
    },
    'tvlux': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/tvlux.png',
        'fanart': 'channels/be/tvlux_fanart.jpg',
        'module': 'resources.lib.channels.be.tvlux'
    },
    'vrt': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/vrt.png',
        'fanart': 'channels/be/vrt_fanart.jpg',
        'module': 'resources.lib.channels.be.vrt'
    },
    'tvcom': {
        'callback': 'replay_bridge',
        'thumb': 'channels/be/tvcom.png',
        'fanart': 'channels/be/tvcom_fanart.jpg',
        'module': 'resources.lib.channels.be.tvcom'
    }
}
