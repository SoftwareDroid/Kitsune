# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Patrick Mispelhorn <patrick.mispelhorn@web.de>
#
# Izumi is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Kitsune is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import time
import json
from typing import Sequence

from selenium.webdriver.chrome.options import Options
# from seleniumwire import webdriver  # Import from seleniumwire
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Source.core.jap_word import JapWord


# この子は今日もムラムラしています
class Nihongodera:
    def __init__(self):
        options = Options()
        # We need a window size for clicking in headless mode
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self._driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

        # self._driver = webdriver.Chrome(options=options)
        self._driver.implicitly_wait(1)
        self._driver.maximize_window()

    def __del__(self):
        self._driver.quit()

    def analyse(self, text: str) -> Sequence[JapWord]:
        self._driver.get(f"https://nihongodera.com/tools/text-analyzer")
        assert len(self._driver.page_source) != 0, "Page get failed. Decoding Error?"
        # self._input_field = self._driver.find_element_by_xpath("//textarea[contains(@class, 'lmt__source_textarea')]")
        self._input_field = self._driver.find_element_by_xpath("//textarea[@id='toolInput']")

        results_of_text = []
        # input text
        self._input_field.send_keys(Keys.CONTROL + "a")
        self._input_field.send_keys(Keys.DELETE)
        self._input_field.send_keys(text)
        # print(self._driver.page_source)
        button = self._driver.find_element_by_xpath("//input[@id='toolSubmit']")
        button.click()
        self._driver.refresh()
        self._driver.implicitly_wait(2)
        # get results

        div_results = self._driver.find_elements_by_xpath("//div[contains(@class, 'tool__results')]/a")
        self._driver.implicitly_wait(2)
        for element in div_results:
            content = element.get_attribute("data-tooltip")
            tag = "<br>"
            p1 = content.find(tag)
            p2 = content.find(tag, p1 + len(tag))

            # def __init__(self, jap: str, hiragana: str, description: str, word_type: str):
            # JapWord(element.text,content[0:p1],content[p2 + len(tag):],content[p1 + len(tag):p2])
            # ret["jap"] = element.text
            # ret["hira"] = content[0:p1]
            # ret["type"] = content[p1 + len(tag):p2]
            # ret["desc"] = content[p2 + len(tag):]
            word = JapWord(element.text, content[0:p1], content[p2 + len(tag):], content[p1 + len(tag):p2])
            # print(word.jap()," d: ", len(word.description())," hira ",len(word.hiragana()), " tt ",word.word_type() )
            # ignore lookup fails
            if len(word.description()) > 0:
                results_of_text.append(word)
        self._driver.implicitly_wait(2)
        # print(results_of_text)
        return results_of_text
