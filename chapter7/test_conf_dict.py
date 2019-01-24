# This file contains the unittests of the conf_dict.py. It is based on using
# pytest for unittesting.
import pytest
from conf_dict import ConfigDict, ConfigKeyError
import shutil
import os

class TestConfigDict:

    safety_file = './safety_copy.json'
    data_file_in_use = './temporary_data.json'

    def setup_class(self):
        shutil.copyfile(TestConfigDict.safety_file,
                    TestConfigDict.data_file_in_use)
        self.cd = ConfigDict(TestConfigDict.data_file_in_use)

    def teardown_class(self):
        os.remove(TestConfigDict.data_file_in_use)

    def test_obj(self):
        assert isinstance(self.cd, ConfigDict)
        assert isinstance(self.cd, dict)
        
    def test_filename_stored(self):
        assert self.cd.filename == TestConfigDict.data_file_in_use

    def test_insert_new_item(self):
        self.cd['some_key'] = 'some_value'
        assert self.cd['some_key'] == 'some_value'

    def test_illegal_key(self):
        with pytest.raises(ConfigKeyError):
            print(self.cd['non_existing_key'])

