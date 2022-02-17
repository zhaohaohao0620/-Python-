import sys
from configparser import ConfigParser
from os.path import join, dirname


class Comm:
    def __init__(self):
        file_name = 'files/test.ini'

        if getattr(sys, 'frozen', False):
            cur_path = dirname(sys.executable)
        elif __file__:
            cur_path = dirname(__file__)

        ini_path = join(dirname(cur_path), file_name)
        print(ini_path)

        self.test_section = self.getIniFilesSectionContent(ini_path, 'Test')

    def getIniFilesSectionContent(self, ini_path, section):
        cfg = ConfigParser()
        cfg.read(ini_path, 'utf-8-sig')
        con = dict(cfg.items(section))

        return con


if __name__ == '__main__':
    c = Comm()
    print(c.test_section)

