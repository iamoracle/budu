
import sys, os, ctypes

def is_admin():

    try:

        return ctypes.windll.shell32.IsUserAnAdmin()

    except:

        return False


if is_admin():

    os.system("net User username password")

else:

    ctypes.windll.shell32.ShellExecuteW(
        None, u"runas", sys.executable, __file__, None, 1)
