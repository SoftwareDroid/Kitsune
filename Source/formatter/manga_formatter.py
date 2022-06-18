class MangaFormatter:
    def __init__(self, insert_spaces: bool, insert_furigana: bool, restrict_result_len: int):
        self._insert_spaces = insert_spaces
        self.insert_furigana = insert_furigana
        self.restrict_result_len = restrict_result_len

    def format(self, results) -> str:
        ret = ""
        for e in results:
            ret
        pass
