import winreg
# Ref: https://stackoverflow.com/questions/53132434/list-of-installed-programs/54825112


def foo(hive, flag):
    aReg = winreg.ConnectRegistry(None, hive)
    aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall", 0, winreg.KEY_READ | flag)

    count_subkey = winreg.QueryInfoKey(aKey)[0]

    software_list = []

    for i in range(count_subkey):
        software = {}
        try:
            asubkey_name = winreg.EnumKey(aKey, i)
            asubkey = winreg.OpenKey(aKey, asubkey_name)
            software['name'] = winreg.QueryValueEx(asubkey, "DisplayName")[0]

            if winreg.QueryValueEx(asubkey, "InstallLocation")[0]:
                software['install_location'] = winreg.QueryValueEx(asubkey, "InstallLocation")[0]
            else:
                software['install_location'] = 'undefined'
            software_list.append(software)
        except EnvironmentError:
            continue

    return software_list


if __name__ == '__main__':
    software_list = foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY) + foo(winreg.HKEY_LOCAL_MACHINE,
                                                                                 winreg.KEY_WOW64_64KEY) + foo(
        winreg.HKEY_CURRENT_USER, 0)

    count = 0
    for software in software_list:
        if software['install_location'] != 'undefined':
            print(software['name'], ' ', software['install_location'])
            count += 1
    print('Number of installed apps with clear path: %s' % count)