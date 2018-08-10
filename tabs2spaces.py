#!/usr/bin/env python3

####################################
#                                  #
# Author: silentcat                #
# Date: 2018-08-09                 #
# Description: A program that can  #
# convert tabs to spaces. For some #
# reason, some text editors have   #
# poorly implemented this feature. #
#                                  #
####################################

import sys

###############################################################
# METHODS:                                                    #
###############################################################
# read_file(path_to_file): Reads a file at path_to_file.      #
###############################################################
# replace_line(line): Replaces all spaces in line with tabs.  #
###############################################################
# write_file(path_to_file, data): Overwrites a file at        #
# path_to_file with data replacing it with its space-indented #
# version.                                                    #
###############################################################

def read_file(path_to_file):
    data = None
    with open(path_to_file) as f:
        data = f.read()
    return data

def replace_line(line):
    new_line = ''
    for i in range(0, len(line)):
        if line[i] == '\t':
            new_line += '    '
        else:
            new_line += line[i]
    return new_line

def write_file(path_to_file, data):
    with open(path_to_file, 'w') as f:
        f.write('')
        f.write(data)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: ./tabs2spaces.py [filename] [filename2] [...]')
        exit(1)
    for arg in sys.argv:
        filename = arg
        data = read_file(filename)
        lines = data.split('\n')
        buffer = ''
        for line in lines:
            line = replace_line(line)
            buffer += line + '\n'
        write_file(filename, buffer)


