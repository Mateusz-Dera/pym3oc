# pym3oc
# Copyright © 2022 Mateusz Dera

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import os
from sys import argv
from pydub import AudioSegment

version = "2022.11.13"

help_string = """
Short   Long        Description
-v      --version   Show version
-h      --help      Show help
-b      --bitrate   Bitrate
-i      --input     Input file
-o      --output    Output file
"""

error_input_not_exist = """
Input file not found
"""

error_input_value = """
Missing input value
"""

error_input_mp3 = """
Input is not .mp3 file
"""

error_input_duplicate = """
Duplicated input value
"""

error_bitrate_value = """
Missing bitrate value
"""

error_bitrate_int = """
Bitrate value is not integer
"""

error_bitrate_max = """
Maximum bitrate is %i
"""

error_bitrate_min = """
Minimum bitrate is %i
"""

error_bitrate_duplicate = """
Duplicated bitrate value
"""

error_input_value = """
Missing output value
"""

error_output_ogg = """
Output is not .ogg file
"""

error_output_duplicate = """
Duplicated output value
"""

error_output_not_exist = """
Output path not found
"""

version_string = """
Version: %s
"""

input = ""
output = ""
bitrate_value = 128

is_input = False
is_output = False
is_bitrate = False

max_b = 500
min_b = 45

def version():
    print(version_string% version)
    exit()
    pass

def help():
    print(help_string)
    exit()
    pass

def input(f):
    global input
    global is_input
    if os.path.exists(os.path.expanduser(f)):
        if f[-4:] == ".mp3":
            input = f
            is_input = True
        else:
            print(error_input_mp3)
            exit()
    else:
        print(error_input_not_exist)
        exit()
    pass

def bitrate(b):
    global bitrate_value
    global is_bitrate
    
    is_int = True
    b_int = 0
    
    try:
        b_int = int(b)
    except:
        is_int = False

    if is_int:
        if b_int < 45:
            print(error_bitrate_min% min_b)
            exit()
        elif b_int > 500:
            print(error_bitrate_max% max_b)
            exit()
        else:
            is_bitrate = True
            bitrate_value = b_int
    else:
        print(error_bitrate_int)
        exit()

def output(o):
    global output
    global is_output
    if os.path.exists(os.path.expanduser(os.path.split(o)[0])):
        if o[-4:] == ".ogg":
            output = o
            is_output = True
        else:
            print(error_output_ogg)
            exit()
    else:
        print(error_output_not_exist)
        exit()   
    pass

for i in range(0,len(argv)):

    if argv[i] == "-h" or argv[i] == "--help":
        help()

    elif argv[i] == "-i" or argv[i] == "--input":
        if is_input:
            print(error_input_duplicate)
            exit()
        else:
            if i+1 <= len(argv):
                i+=1
                input(argv[i])
            else:
                print(error_input_value)
                exit()

    elif argv[i] == "-b" or argv[i] == "--bitrate":
        if is_bitrate:
            print(error_bitrate_duplicate)
            exit()
        else:
            if i+1 <= len(argv):
                i+=1
                bitrate(argv[i])
            else:
                print(error_bitrate_value)
                exit()
    
    elif argv[i] == "-o" or argv[i] == "--output":
        if is_output:
            print(error_output_duplicate)
            exit()
        else:
            if i+1 <= len(argv):
                i+=1
                output(argv[i])
            else:
                print(error_output_value)
                exit()


sound = AudioSegment.from_file(os.path.expanduser(input))
sound.export(os.path.expanduser(output), format="ogg", bitrate=str(bitrate_value)+"k")