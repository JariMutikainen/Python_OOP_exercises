# This file contains the unittests of the conf_dict.py. It is based on using
# pytest for unittesting.
import pytest
from conf_dict import ConfigDict, ConfigKeyError
import subprocess

class TestConfigDict:

    safety_file = './safety_copy.json'
    data_file_in_use = './data.json'

    def setup_class(self):
        subprocess.call('cp', safety_file, data_file_in_use)

    def teardown_class(self):
        pass
        

