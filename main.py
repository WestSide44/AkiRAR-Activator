import os
import requests
import shutil



key = 'https://raw.githubusercontent.com/ilyhalight/AkiRAR-Activator/master/rarreg.key'
default_dir = 'C:\Program Files\WinRAR'

def download(link):
    filename = link.split('/')[-1]
    r = requests.get(link, allow_redirects=True)
    open(filename, 'wb').write(r.content)

def activate(dir):
    file_path = dir + '/rarreg.key'
    vote = ''
    if os.path.isfile(file_path):
        while True:
            print('�������� WinRAR ��� ����������� � ������� rarreg.key. �� ������ ������������ ����? [y/n]')
            vote = input('>>> ')
            if vote.lower() == 'y':
                try:
                    os.remove(file_path)
                except PermissionError:
                    print('������������� ��������� � ������� ��������������')
                break
            elif vote.lower() == 'n':
                print('�� ���������� �� ���������� ����� rarreg.key')
                break
            else:
                pass
    else:
        pass

    if vote.lower() == 'n':
        print(file_path, '��� ����������')
    else:
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

def deactivate(dir):
    file_path = dir + '/rarreg.key'
    vote = ''
    if os.path.isfile(file_path):
        while True:
            print('�� �������, ��� ������ �������������� WinRAR? [y/n]')
            vote = input('>>> ')
            if vote.lower() == 'y':
                try:
                    os.remove(file_path)
                    print('WinRAR ��� ������� �������������')
                except PermissionError:
                    print('������������� ��������� � ������� ��������������')
                break
            elif vote.lower() == 'n':
                print('�� ���������� �� ����������� WinRAR')
                break
            else:
                pass
    else:
        print('������ �������������� ����.')

def check_deactivate():
    if os.path.isdir(default_dir):
        deactivate(default_dir)
    else:
        while True:
            print('������� ���� �� ����� WinRAR')
            dir = input('>>> ')
            if os.path.isdir(dir):
                break
            else:
                pass

        deactivate(dir)

def status():
    if os.path.isdir(default_dir):
        file_path = f'{default_dir}/rarreg.key'
        if os.path.isfile(file_path):
            print('������: �����������')
        else:
            print('������: �� �����������')
    else:
        print('WinRAR ���������� �� � ����������� �����')

def check_activate():
    if os.path.isdir(default_dir):
        activate(default_dir)
    else:
        while True:
            print('������� ���� �� ����� WinRAR')
            dir = input('>>> ')
            if os.path.isdir(dir):
                break
            else:
                pass

        activate(dir)

def main():
    while True:
        os.system('cls||clear')
        print(f'����� ���������� � AkiRAR Activator.\n��������� ���� �������������� �� ������ WinRAR 6.02 (64-���������)\n\n�������� ��������:\n1) ��������� ��������� (��������, ���� WinRAR � ��� ���������� � {default_dir})\n2) ������������ WinRAR\n3) �������������� WinRAR\n4) �����')
        vote = input('>>> ')
        if vote == '1':
            status()
            break
        elif vote == '2':
            check_activate()
            break
        elif vote == '3':
            check_deactivate()
            break
        elif vote == '4':
            break
        else:
            pass

    input('������� Enter ��� �������� ���������... ')

if __name__ == '__main__':
    if os.name == 'nt':
        main()
    else:
        print('������ OS �� ��������������')