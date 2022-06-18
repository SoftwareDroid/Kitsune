from enum import Enum

def read_subs(file: str):
    results = []
    file1 = open(file, 'r')

    class LineState(Enum):
        number = 0,
        time = 1,
        sub = 3,

    state = LineState.number

    new_file = ""
    for line in file1.readlines():
        if state == LineState.number:
            new_file += line
            state = LineState.time
        elif state == LineState.time:
            assert "-->" in line
            new_file += line
            state = LineState.sub
        elif LineState.sub:
            if len(line) == 1:
                new_file += line
                state = LineState.number
            else:
                assert "-->" not in line
                # print(line,end="")
                results.append(line[:-1])
    return results
