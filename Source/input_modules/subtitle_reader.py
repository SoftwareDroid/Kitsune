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

import pysubs2

def read_subs_file(file: str):
    subs = pysubs2.load(file)
    results = []
    for line in subs:
        results.append(line.plaintext)
    return results

