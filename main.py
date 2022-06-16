# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Source.test2 import SeleniumDeeplTranslator

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    text = "この子は今日もムラムラしています"
    tool = SeleniumDeeplTranslator()
    tool.analyse(text)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

#  PyCharm  at https://www.jetbrains.com/help/pycharm/
