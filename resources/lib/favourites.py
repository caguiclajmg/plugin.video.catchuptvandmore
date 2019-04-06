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

import xbmc

from codequick import Route, utils, storage
from hashlib import md5

from resources.lib.labels import LABELS


@Route.register
def add_item_to_favourites(plugin, item_dict={}):
    """
    Callback function called when the user click
    on 'add item to favourite' from an item
    context menu
    """

    # Ask the user to edit the label
    item_dict['label'] = utils.keyboard(plugin.localize(LABELS['Favorite name']), item_dict['label'])

    # If user aborded do not add this item to favourite
    if item_dict['label'] == '':
        # TODO: Notify the user that the action aborded
        return False

    # Add this item to favourite db
    with storage.PersistentDict("favourites.pickle") as db:
        item_path = xbmc.getInfoLabel('ListItem.Path')
        item_hash = md5(str(item_dict)).hexdigest()

        if 'is_folder' not in item_dict:
            item_dict['params']['is_folder'] = True
        item_dict['callback'] = item_path
        item_dict['params']['order'] = len(db)

        db[item_hash] = item_dict
    return False


@Route.register
def rename_favourite_item(plugin, item_hash):
    """
    Callback function called when the user click
    on 'rename' from a favourite item
    context menu
    """
    item_label = utils.keyboard(plugin.localize(LABELS['Favorite name']), xbmc.getInfoLabel('ListItem.Label'))

    # If user aborded do not edit this item
    if item_label == '':
        return False
    with storage.PersistentDict("favourites.pickle") as db:
        db[item_hash]['label'] = item_label
    xbmc.executebuiltin('XBMC.Container.Refresh()')
    return False


@Route.register
def remove_favourite_item(plugin, item_hash):
    """
    Callback function called when the user click
    on 'remove' from a favourite item
    context menu
    """
    with storage.PersistentDict("favourites.pickle") as db:
        del db[item_hash]
    xbmc.executebuiltin('XBMC.Container.Refresh()')
    return False


@Route.register
def move_favourite_item(plugin, direction, item_hash):
    """
    Callback function called when the user click
    on 'Move up/down' from a favourite item
    context menu
    """
    if direction == 'down':
        offset = 1
    elif direction == 'up':
        offset = -1

    with storage.PersistentDict("favourites.pickle") as db:
        item_to_move_id = item_hash
        item_to_move_order = db[item_hash]['params']['order']

        menu = []
        for item_hash, item_dict in db.items():
            item = (
                item_dict['params']['order'],
                item_hash,
                item_dict
            )

            menu.append(item)
        menu = sorted(menu, key=lambda x: x[0])

        for k in range(0, len(menu)):
            item = menu[k]
            item_hash = item[1]
            if item_to_move_id == item_hash:
                item_to_swap = menu[k + offset]
                item_to_swap_order = item_to_swap[0]
                item_to_swap_id = item_to_swap[1]
                db[item_to_move_id]['params']['order'] = item_to_swap_order
                db[item_to_swap_id]['params']['order'] = item_to_move_order
                xbmc.executebuiltin('XBMC.Container.Refresh()')
                break

        return False

