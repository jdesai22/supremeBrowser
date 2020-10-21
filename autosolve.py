from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import os
import speech_recognition as sr
# import ffmpy
import requests
import urllib
import pydub

import time


def autosolve():
    driver.get("https://www.google.com/recaptcha/api2/demo")
    # switch to recaptcha frame


if __name__ == "__main__":
    chrome_options = Options()

    # driver = webdriver.Chrome('driver/chromedriver.exe')
    driver = webdriver.Chrome(options=chrome_options, executable_path='driver/chromedriver')


    autosolve()