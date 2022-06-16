# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Source.nihongodera import Nihongodera

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    text = "この子は今日もムラムラしています"
    tool = Nihongodera()
    results = tool.analyse(text)
    print(results)
    text2 = "たまねぎを食べる"
    results = tool.analyse(text2)
    print(results)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

#  PyCharm  at https://www.jetbrains.com/help/pycharm/
