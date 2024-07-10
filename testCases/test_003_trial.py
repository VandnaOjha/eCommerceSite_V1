import os
import time

from pageObjects.Homepage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.logs import LogGen
from utilities.readProperties import ReadConfig


class Test_005_trial:
    def print_name(self):
        print("hello,git")