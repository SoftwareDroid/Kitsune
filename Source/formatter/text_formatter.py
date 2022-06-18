from typing import Sequence, Tuple

from Source.formatter.manga_helper_list import JapWord
from deep_translator import GoogleTranslator
# translated = Go/ogleTranslator(source='auto', target='de').translate("keep it up, you are awesome")  # output -> Weiter so, du bist großartig

def create_text_output(sentences: Sequence[Tuple[str, Sequence[JapWord]]]):
    linking = {}
    # practice sheet
    practice_sheet = "Practice Sheet\n\n"
    counter = 0
    for sentence in sentences:
        copy: str = sentence[0]
        translated: str = GoogleTranslator(source="ja",target="en").translate(copy)
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
    cheat_sheet = "cheat Sheet\n\n"

    for link in linking:
        entry: JapWord = linking[link][1]
        references = linking[link][0]
        cheat_sheet += f"{entry.jap()} ({entry.hiragana()}) \n   {entry.description()} \n   {references} \n"

    return practice_sheet, cheat_sheet
