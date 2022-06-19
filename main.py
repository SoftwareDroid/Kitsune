from typing import Sequence
import toml
from Source.nihongodera import Nihongodera
from Source.formatter.text_formatter import create_text_output
from Source.subtitle_reader import read_subs


def main():
    settings = toml.load("settings/config.toml")
    print(settings)
    subs = read_subs(settings["input"]["filename"])
    subs: Sequence[str] = subs[settings["input"]["lines"][0]:settings["input"]["lines"][1]]
    print(subs)
    sentences = subs
    tool = Nihongodera()
    analysed = []
    for sentence in sentences:
        print("Lookup")
        results = tool.analyse(sentence)
        print(f"lookup finished: {sentence}")
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
