#!/usr/bin/env python3

# This script removes duplicate events from an iCal file.
# To use it run:
# python3 icscleaner.py SOURCE_FILE.ics DESTINATION_FILE.ics

import sys

input_file = open(sys.argv[1])
output_file = open(sys.argv[2], 'w')

the_text = input_file.readlines() # all text from input file

the_dict = {}
temp, eventid, header = "", "", ""


for line in the_text:
    if 'BEGIN:VEVENT' in line:
        break
    else:
        header += line

for line in the_text:
    if 'BEGIN:VEVENT' in line:
        temp = ""
        temp = line
    elif 'END:VEVENT' in line:
        temp += line.rstrip()
        the_dict[eventid] = temp
    elif 'DTSTART' in line:
        temp += line
        eventid = line
    else:
        temp += line

output_file.write(header[:-1]) # -1 for remove new line

for line in the_dict.values():
    output_file.write(line)

output_file.write('END:VCALENDAR')
