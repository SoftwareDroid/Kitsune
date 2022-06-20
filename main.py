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
import pathlib
import os
from typing import Sequence
import toml
from Source.lookup_modules.nihongodera import Nihongodera
from Source.core.jap_word import JapWord
from Source.output_modules.output_text_writer import create_text_output
from Source.input_modules.subtitle_reader import read_subs_file
import argparse
from pathlib import Path


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def main():
    parser = argparse.ArgumentParser(description='Converts a subtitle file into a format for learning Japanese.')
    parser.add_argument("subtitles_file", help="the subtitle file", type=str)
    parser.add_argument("-out_lang", type=str, default="en", help="translation help")
    parser.add_argument("-out_folder", type=str, default="Kitsune_out", help="the output is written in this folder")
    parser.add_argument("-max_lines", type=int, default=50, help="splits the input in serveral in needed")
    parser.add_argument("-start_by", type=int, default=0)
    parser.add_argument("-end_by", type=int, default=99999)
    args = parser.parse_args()

    print(args.out_folder)
    print(args)
    all_subs = read_subs_file(args.subtitles_file)
    all_subs = all_subs[args.start_by:min(len(all_subs), args.end_by)]
    os.makedirs(args.out_folder, exist_ok=True)
    chunk_counter = 0
    link_counter = 0
    tool = Nihongodera()
    for sentences in chunks(all_subs, args.max_lines):
        chunk_counter += 1
        analysed = []
        for sentence in sentences:
            # print("Lookup")
            results = tool.analyse(sentence)
            print(f"Lookup finished: {sentence}")
            analysed.append((sentence, results))
        practice_sheet, cheat_sheet = create_text_output(analysed, args, link_counter)
        link_counter += args.max_lines

        folder = args.out_folder
        mode = "txt"
        base_name = pathlib.Path(args.subtitles_file).name.split(".")[0]
        file1 = f"practice_sheet_n_{chunk_counter}_cs_{args.max_lines}__" + base_name
        file2 = f"helper_sheet_n_{chunk_counter}_cs_{args.max_lines}__" + base_name
        text_file = open(f"{folder}/{file1}.{mode}", "w")
        text_file.write(practice_sheet)
        text_file.close()

        text_file = open(f"{folder}/{file2}.{mode}", "w")
        text_file.write(cheat_sheet)
        text_file.close()


if __name__ == '__main__':
    main()

#  PyCharm  at https://www.jetbrains.com/help/pycharm/
