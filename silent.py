import os
import requests
import shutil
import time


key = 'https://raw.githubusercontent.com/ilyhalight/AkiRAR-Activator/master/rarreg.key'
default_dir = 'C:\Program Files\WinRAR'

def download(link):
    filename = link.split('/')[-1]
    r = requests.get(link, allow_redirects=True)
    open(filename, 'wb').write(r.content)

def activate(dir):
    file_path = dir + '/rarreg.key'
    if os.path.isfile(file_path):
        try:
            os.remove(file_path)
        except PermissionError:
            print('������������� ��������� � ������� ��������������')
    else:
        pass

    try:
        download(key)
    except:
        print('��������� ���������� � ����������')
    try:
        shutil.copy2('rarreg.key', dir)
    except PermissionError:
        print('������������� ��������� � ������� ��������������')
    download_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'rarreg.key')
    try:
        os.remove(download_file)
    except:
        pass

    print('WinRAR ��� ������� �����������')


def check_activate():
    if os.path.isdir(default_dir):
        activate(default_dir)
    else:
        print('����� WinRAR ��������� �� � ����������� �����')

if __name__ == '__main__':
    if os.name == 'nt':
        check_activate()
        print('�����...')
        time.sleep(3)
    else:
        print('������ OS �� ��������������')
        time.sleep(3)