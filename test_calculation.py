import os
import pytest
import calculation

# setup and teardown
class TestCal(object):
    def setup_method(self, method):
        print('method={}'.format(method.__name__))
        self.cal = calculation.Cal()

    def teardown_method(self, method):
        print('method={}'.format(method.__name__))
        del self.cal

    def test_add_num_and_double(self):
        cal = calculation.Cal()
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')


"""
    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path) is True
            
    def test_add_num_and_double(self, request):
        os_name = request.config.getoption('--os-name')
        print(os_name)
        if os_name == 'mac':
            print('ls')
        elif os_name == 'windows':
            print('dir')
        assert self.cal.add_num_and_double(1, 1) == 4
"""