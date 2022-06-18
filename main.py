# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Source.nihongodera import Nihongodera
from Source.formatter.text_formatter import create_text_output
from Source.subtitle_reader import read_subs
def main(name):
    file = "/home/patrick/Desktop/Learning/Little witch/Little Witch Academia (01-25) (Webrip)/Little Witch Academia.S01E01.CC.ja.srt"
    subs = read_subs(file)
    subs = subs[:5]
    print(subs)
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    sentences = ["この子は今日もムラムラしています","たまねぎを食べる"]
    sentences = subs
    tool = Nihongodera()
    analysed = []
    for sentence in sentences:
        print("Lookup")
        results = tool.analyse(sentence)
        print(f"lookup finished: {sentence}")
        analysed.append((sentence,results))
    practice_sheet,cheat_sheet = create_text_output(analysed)

    text_file = open("out/practice_sheet.txt", "w")
    n = text_file.write(practice_sheet)
    text_file.close()

    text_file = open("out/cheat_sheet.txt", "w")
    n = text_file.write(cheat_sheet)
    text_file.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('PyCharm')

#  PyCharm  at https://www.jetbrains.com/help/pycharm/
