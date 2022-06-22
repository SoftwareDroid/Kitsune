import datetime


class MemoryWords:

    def __init__(self, file: str, writeable: bool):
        self._skip_words = set()
        self._learned_words = []
        self._never_skip_words = set()
        self._file = file
        self._write = writeable
        if file is None:
            return

        try:
            file1 = open(file, 'r')
        except OSError as e:
            print("Memory file not found")
            return

        for line in file1.readlines():
            line = line[:-1]
            # comment
            if line.startswith("#"):
                continue
            if line.startswith(" "):
                self._never_skip_words.add(line)
            else:
                self._skip_words.add(line)
        print("skip words: ",self._skip_words)

    def __del__(self):
        if self._file is None or not self._write:
            return

        file_object = open(self._file, 'a')
        timestamp = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        file_object.write(f"# {timestamp}\n")
        for line in self._learned_words:
            file_object.write(line + "\n")
        file_object.close()

    def skip_word(self, word) -> bool:
        return word in self._skip_words

    def learn_word(self, word):
        if word not in self._never_skip_words and word not in self._skip_words:
            self._learned_words.append(word)
