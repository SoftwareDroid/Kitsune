# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Patrick Mispelhorn <patrick.mispelhorn@web.de>
#
# Izumi is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Kitsune is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from typing import Sequence

import linking as linking


# class MangaHelperEntry:
#     def __init__(self, jap: str, pronunciation: str, description: str, linking: str):
#         self._jap = jap
#         self._pronunciations = pronunciation
#         self._description = description
#         self._linking = linking
#
#     def linking(self):
#         return self._linking
#
#     def jap(self) -> str:
#         return self._jap
#
#     def pronunciation(self) -> str:
#         return self._pronunciations
#
#     def description(self) -> str:
#         return self._description


class JapWord:
    def __init__(self, jap: str, hiragana: str, description: str, wtype: str):
        self._jap = jap
        self._hiragana = hiragana
        self._description = description
        self._word_type = wtype

    def jap(self):
        return self._jap

    def hiragana(self):
        return self._hiragana

    def description(self):
        return self._description

    def word_type(self):
        return self._word_type

    def get_practice_format(self) -> str:
        if self._jap != self._hiragana:
            return f"{self._jap} ({self._hiragana})"
        else:
            return self._jap



# class MangaHelperList:
#     def __init__(self, title: str, entries: Sequence[MangaHelperEntry]):
#         self._entries = entries
#         self._title = title
#
#     def get_filename(self):
#         return "helper_list.pdf"
#
#     def title(self):
#         return self._title
#
#     def rm_duplicates(self):
#         seen = set()
#         entries = []
#         for e in self._entries:
#             if e.jap() not in seen:
#                 entries.append(e)
#             seen.add(e.jap())
#         self._entries = entries
#
#     def get_entries(self):
#         return self._entries
#
#     def title(self):
#         return self._title
