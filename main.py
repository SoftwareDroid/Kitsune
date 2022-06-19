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
import toml
from Source.lookup_modules.nihongodera import Nihongodera
from Source.core.jap_word import JapWord
from Source.output_modules.output_text_writer import create_text_output
from Source.input_modules.subtitle_reader import read_subs_srt_file




def main():
    settings = toml.load("settings/config.toml")
    # print(settings)
    subs = read_subs_srt_file(settings["input"]["filename"])
    subs: Sequence[str] = subs[settings["input"]["lines"][0]:settings["input"]["lines"][1]]
    # print(subs)
    sentences = subs
    tool = Nihongodera()
    analysed = []
    for sentence in sentences:
        # print("Lookup")
        results = tool.analyse(sentence)
        print(f"Lookup finished: {sentence}")
        analysed.append((sentence, results))
    practice_sheet, cheat_sheet = create_text_output(analysed,settings)
    folder = settings["output"]["folder"]
    mode = settings["output"]["mode"]
    file1 = settings["output"]["practice_sheet"]
    file2 = settings["output"]["word_sheet"]
    text_file = open(f"{folder}/{file1}.{mode}", "w")
    text_file.write(practice_sheet)
    text_file.close()

    text_file = open(f"{folder}/{file2}.{mode}", "w")
    text_file.write(cheat_sheet)
    text_file.close()


if __name__ == '__main__':
    main()

#  PyCharm  at https://www.jetbrains.com/help/pycharm/
