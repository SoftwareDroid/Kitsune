from typing import Sequence, Tuple
import datetime
from Source.core.jap_word import JapWord
from deep_translator import GoogleTranslator


def create_text_output(sentences: Sequence[Tuple[str, Sequence[JapWord]]], settings):
    linking = {}
    # practice sheet
    title1 = settings["output"]["practice_sheet"]
    version = settings["main"]["version"]
    now = datetime.datetime.now()
    input_file = settings["input"]["filename"]
    timestamp = now.strftime("%d.%m.%Y %H:%M:%S")
    practice_sheet = f"{title1}\nInput: {input_file}\nKitsune Version: {version}\nTimestamp: {timestamp}\nSentences\n\n"
    counter = 0
    for sentence in sentences:
        copy: str = sentence[0]
        translated: str = GoogleTranslator(source="ja", target=settings["output"]["language"]).translate(copy)
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
    title2 = settings["output"]["word_sheet"]
    cheat_sheet = f"{title2}\nInput: {input_file} \nKitsune Version: {version}\nTimestamp: {timestamp}\n\nWords:\n"

    for link in linking:
        entry: JapWord = linking[link][1]
        references = linking[link][0]
        cheat_sheet += f"{entry.jap()} ({entry.hiragana()}) \n   {entry.description()} \n   {references} \n"

    return practice_sheet, cheat_sheet
