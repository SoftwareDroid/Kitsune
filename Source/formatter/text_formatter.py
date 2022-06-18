from typing import Sequence, Tuple

import link as link

from Source.formatter.manga_helper_list import JapWord


def create_text_output(sentences: Sequence[Tuple[str,Sequence[JapWord]]]):
    linking = {}
    # practice sheet
    practice_sheet = "Practice Sheet\n\n"
    counter = 0
    for sentence in sentences:
        words = ""
        for entry in sentence[1]:
            entry: JapWord
            words += entry.get_practice_format() + " "
            # collect linking
            if entry.jap() not in linking:
                linking[entry.jap()] = ([],entry)
            linking[entry.jap()][0].append(counter)
        practice_sheet += f"{counter}. {words} \n"
        counter += 1
        # create cheat sheet
    cheat_sheet = "cheat Sheet\n\n"

    for link in linking:
        entry: JapWord = linking[link][1]
        references = linking[link][0]
        cheat_sheet += f"{entry.jap()} ({entry.hiragana()}) \n   {entry.description()} \n   {references} \n"

    return practice_sheet, cheat_sheet