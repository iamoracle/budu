import sys, os

# check if the number of arguments supplied is 3 or more

if len(sys.argv) < 3:

    print('expecting exactly two arguments: username and password')

    print("usage: python execute.py username password")

    exit()

# the code to be exported

code = r"""
import sys, os, ctypes

def is_admin():

    try:

        return ctypes.windll.shell32.IsUserAnAdmin()

    except:

        return False


if is_admin():

    os.system("net User %s %s")

else:

    ctypes.windll.shell32.ShellExecuteW(
        None, u"runas", sys.executable, __file__, None, 1)
"""

# format the code with arguments

code = code % (sys.argv[1], sys.argv[2])

# directory of the output file

directory = os.path.dirname(os.path.realpath(__file__))

output_file = os.path.join(directory, 'code.py')

# write code to file

with open(output_file, 'w') as file:

    file.write(code)
