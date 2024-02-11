from confygure import setup, config, config_t, config_rt

setup(files=('./.github/config.yml',))

assert config('test') == 'some value'
assert config('nonexist') == None
assert config_t(str, 'test') == 'some value'
assert config_t(str, 'nonexist') == None
try:
    config_t(int, 'test')
    raise AssertionError('config_t should have raised a TypeError')
except TypeError:
    pass
assert config_rt(str, 'test') == 'some value'
try:
    config_rt(str, 'nonexist')
    raise AssertionError('config_rt should have raised a KeyError')
except KeyError:
    pass
