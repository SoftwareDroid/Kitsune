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

from typing import Sequence, Tuple
import datetime
from Source.core.jap_word import JapWord
from deep_translator import GoogleTranslator


def create_text_output(sentences: Sequence[Tuple[str, Sequence[JapWord]]], args, link_counter):
    linking = {}
    # practice sheet
    title1 = "Practice Sheet"
    version = 1.0
    now = datetime.datetime.now()
    input_file = args.subtitles_file
    timestamp = now.strftime("%d.%m.%Y %H:%M:%S")
    lines = args.max_lines
    practice_sheet = f"{title1}\nInput: {input_file}\nLines: {lines}\nKitsune Version: {version}\nTimestamp: {timestamp}\nSentences\n\n"
    counter = link_counter
    for sentence in sentences:
        copy: str = sentence[0]
        translated: str = GoogleTranslator(source="ja", target=args.out_lang).translate(copy)
        for entry in sentence[1]:
            entry: JapWord
            if entry.jap() != entry.hiragana():
                copy = copy.replace(entry.jap(), f"{entry.jap()}[{entry.hiragana()}] ")
            # collect linking
            if entry.jap() not in linking:
                linking[entry.jap()] = ([], entry)
            linking[entry.jap()][0].append(counter)
        practice_sheet += f"{counter}. {copy}\n{translated}\n\n"
        counter += 1
    # create cheat sheet
    title2 = "Helper Sheet"
    cheat_sheet = f"{title2}\nInput: {input_file}\nLines: {lines} \nKitsune Version: {version}\nTimestamp: {timestamp}\n\nWords:\n"

    for link in linking:
        entry: JapWord = linking[link][1]
        references = linking[link][0]

        if entry.jap() != entry.hiragana():
            cheat_sheet += f"{entry.jap()} ({entry.hiragana()}) \n   {entry.description()} \n   {references} \n"
        else:
            cheat_sheet += f"{entry.jap()}\n   {entry.description()} \n   {references} \n"

    return practice_sheet, cheat_sheet
