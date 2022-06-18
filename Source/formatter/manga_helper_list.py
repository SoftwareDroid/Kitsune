from typing import Sequence

import linking as linking


class MangaHelperEntry:
    def __init__(self, jap: str, pronunciation: str, description: str, linking: str):
        self._jap = jap
        self._pronunciations = pronunciation
        self._description = description
        self._linking = linking

    def linking(self):
        return self._linking

    def jap(self) -> str:
        return self._jap

    def pronunciation(self) -> str:
        return self._pronunciations

    def description(self) -> str:
        return self._description


class JapWord:
    def __init__(self, jap: str, hiragana: str, description: str, wtype: str):
        self._jap = jap
        self._hiragana = hiragana
        self._description = description
        self._wtype = wtype

    def jap(self):
        return self._jap

    def hiragana(self):
        return self._hiragana

    def description(self):
        return self._description

    def wtype(self):
        return self._wtype

    def get_practice_format(self) -> str:
        if self._jap != self._hiragana:
            return f"{self._jap} ({self._hiragana})"
        else:
            return self._jap

    def get_help_format(self, linking: str) -> MangaHelperEntry:
        return MangaHelperEntry(self._jap, self._hiragana, self._description, linking)


class MangaHelperList:
    def __init__(self, title: str, entries: Sequence[MangaHelperEntry]):
        self._entries = entries
        self._title = title

    def get_filename(self):
        return "helper_list.pdf"

    def title(self):
        return self._title

    def rm_duplicates(self):
        seen = set()
        entries = []
        for e in self._entries:
            if e.jap() not in seen:
                entries.append(e)
            seen.add(e.jap())
        self._entries = entries

    def get_entries(self):
        return self._entries

    def title(self):
        return self._title
