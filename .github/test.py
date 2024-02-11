from confygure import setup, config, configuration_file

setup(files=('./.github/config.yml',))

assert config('test') == 'some value'
