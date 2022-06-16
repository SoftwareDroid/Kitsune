import time
import json
from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver  # Import from seleniumwire
from selenium.webdriver.common.keys import Keys

class SeleniumDeeplTranslator:
    def __init__(self):
        options = Options()
        # We need a window size for clicking in headless mode
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        self._driver = webdriver.Chrome(options=options)
        self._driver.implicitly_wait(30)
        self._driver.maximize_window()
        self._driver.response_interceptor = SeleniumDeeplTranslator._Interceptor.interceptor
        # Webanwendung aufrufen
        self._driver.get("https://www.deepl.com/translator")
        assert len(self._driver.page_source) != 0, "Page get failed. Decoding Error?"
                #print(len(self._driver.page_source))
        #print(self._driver.page_source)
        #time.sleep(10)
        self._input_field = self._driver.find_element_by_xpath("//textarea[contains(@class, 'lmt__source_textarea')]")
        #assert len(self._input_field) == 1, "process field not unique"
        #self._input_field = self._input_field[0]
        self._input_lang = None
        self._output_lang = None

    def __del__(self):
        self._driver.quit()

    def config(self, input_lang: str, output_lang: str):
        if input_lang != "auto" and input_lang != self._input_lang:
            button = self._driver.find_element_by_xpath("//button[@dl-test='translator-source-lang-btn']")
            button.click()
            button = self._driver.find_element_by_xpath('//button[@dl-test="translator-lang-option-{}"]'.format(input_lang))
            button.click()
            self._input_lang = input_lang
        if output_lang != "auto" and output_lang != self._output_lang:
            button = self._driver.find_element_by_xpath("//button[@dl-test='translator-target-lang-btn']")
            button.click()
            lang_code_out = "fr-FR"
            button = self._driver.find_element_by_xpath(
                '//button[@dl-test="translator-lang-option-{}"]'.format(output_lang))
            button.click()
            self._output_lang =output_lang
    def translate(self,text: str, input_lang_code: str, output_language_code: str, timeout: float):
        self.config(input_lang_code,output_language_code)

        self._input_field.send_keys(Keys.CONTROL + "a")
        self._input_field.send_keys(Keys.DELETE)
        self._input_field.send_keys(text)
        result = SeleniumDeeplTranslator._Interceptor.retrieve_result(timeout_in_s=timeout)
        return result
    class _Interceptor:
        translation: str = None

        # from selenium import webdriver
        def interceptor(request, response):  # A response interceptor takes two args

            if request.url.endswith("LMT_handle_jobs"):

                data = response.body.decode("utf-8")
                # print(json.loads(data))
                data = json.loads(data)
                translations = data["result"]["translations"]
                sentance = translations[0]["beams"][0]["postprocessed_sentence"]

                if len(sentance) > 1:
                    SeleniumDeeplTranslator._Interceptor.translation = sentance

        @staticmethod
        def retrieve_result(timeout_in_s: float):
            start = time.time()
            # and (time.time() - start < timeout_in_s)
            # spin wait
            while SeleniumDeeplTranslator._Interceptor.translation is None and ((time.time() - start) < timeout_in_s):
                time.sleep(0.1)
            copy = SeleniumDeeplTranslator._Interceptor.translation
            SeleniumDeeplTranslator._Interceptor.translation = None
            return copy