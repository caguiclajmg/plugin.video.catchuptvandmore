# -*- coding: utf-8 -*-
"""
    Catch-up TV & More
    Copyright (C) 2017  SylvainCecchetto

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

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from resources.lib.hack_future import install_aliases
install_aliases()
from builtins import str
from builtins import *
from codequick import Route, Resolver, Listitem, utils, Script

from resources.lib.labels import LABELS
from resources.lib import web_utils
from resources.lib import download
from resources.lib.listitem_utils import item_post_treatment, item2dict

import re
import urlquick

# TO DO
# ....

URL_ROOT = 'https://www.tvlux.be'

URL_LIVE = URL_ROOT + '/live'

URL_VIDEOS = URL_ROOT + '/videos'

URL_EMISSIONS = URL_ROOT + '/emissions'


def replay_entry(plugin, item_id, **kwargs):
    """
    First executed function after replay_bridge
    """
    return list_categories(plugin, item_id)


@Route.register
def list_categories(plugin, item_id, **kwargs):
    """
    Build categories listing
    - Tous les programmes
    - Séries
    - Informations
    - ...
    """
    item = Listitem()
    item.label = plugin.localize(LABELS['All videos'])
    item.set_callback(list_videos,
                      item_id=item_id,
                      next_url=URL_VIDEOS,
                      page='0')
    item_post_treatment(item)
    yield item

    item = Listitem()
    item.label = plugin.localize(LABELS['All programs'])
    item.set_callback(list_programs, item_id=item_id)
    item_post_treatment(item)
    yield item


@Route.register
def list_programs(plugin, item_id, **kwargs):

    resp = resp = urlquick.get(URL_EMISSIONS)
    root = resp.parse()

    for program_datas in root.iterfind(".//div[@class='col-sm-4']"):

        program_title = program_datas.find('.//img').get('alt')
        program_image = program_datas.find('.//img').get('src')
        program_url = URL_ROOT + '/' + program_datas.find(".//a").get("href")

        item = Listitem()
        item.label = program_title
        item.art['thumb'] = program_image
        item.set_callback(list_videos,
                          item_id=item_id,
                          next_url=program_url,
                          page='0')
        item_post_treatment(item)
        yield item


@Route.register
def list_videos(plugin, item_id, next_url, page, **kwargs):

    resp = urlquick.get(next_url + '?lim_un=%s' % page)
    root = resp.parse()

    for video_datas in root.iterfind(".//div[@class='col-sm-4']"):
        video_title = video_datas.find('.//h3').text
        video_image = video_datas.find('.//img').get('src')
        video_url = video_datas.find('.//a').get('href')

        item = Listitem()
        item.label = video_title
        item.art['thumb'] = video_image

        item.set_callback(get_video_url,
                          item_id=item_id,
                          video_label=LABELS[item_id] + ' - ' + item.label,
                          video_url=video_url)
        item_post_treatment(item, is_playable=True, is_downloadable=True)
        yield item

    yield Listitem.next_page(item_id=item_id,
                             next_url=next_url,
                             page=str(int(page) + 12))


@Resolver.register
def get_video_url(plugin,
                  item_id,
                  video_url,
                  download_mode=False,
                  video_label=None,
                  **kwargs):

    resp = urlquick.get(video_url, max_age=-1)
    list_streams_datas = re.compile(r'src\: "(.*?)"').findall(resp.text)
    stream_url = ''
    for stream_datas in list_streams_datas:
        if 'm3u8' in stream_datas or \
                'mp4' in stream_datas:
            stream_url = stream_datas

    if download_mode:
        return download.download_video(stream_url, video_label)
    return stream_url


def live_entry(plugin, item_id, item_dict, **kwargs):
    return get_live_url(plugin, item_id, item_id.upper(), item_dict)


@Resolver.register
def get_live_url(plugin, item_id, video_id, item_dict, **kwargs):

    resp = urlquick.get(URL_LIVE, max_age=-1)
    return re.compile(r'"sourceURL":"(.*?)"').findall(resp.text)[0]
