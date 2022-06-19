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

from enum import Enum

def read_subs_srt_file(file: str):
    results = []
    file1 = open(file, 'r')

    class LineState(Enum):
        number = 0,
        time = 1,
        sub = 3,

    state = LineState.number

    new_file = ""
    for line in file1.readlines():
        if state == LineState.number:
            new_file += line
            state = LineState.time
        elif state == LineState.time:
            assert "-->" in line
            new_file += line
            state = LineState.sub
        elif LineState.sub:
            if len(line) == 1:
                new_file += line
                state = LineState.number
            else:
                assert "-->" not in line
                # print(line,end="")
                results.append(line[:-1])
    return results
