############################################################################
#This program converts an .srt file that uses commas for decimal points
#into a .vtt file.
#
#Author: Benjamin Niedzielski (bniedzie@ucla.edu)
#Last Modified: 8/12/2019
############################################################################
import re;
import sys;

readFile = 'test.txt';
writeFileBase = 'test/page';

fp = open(readFile, 'r');
fw = open('newtest.txt', 'w');
line = fp.readline();
while line:
    line = line.replace("<div class=\"PageNum\">", "\n<div class=\"PageNum\">\n");
    line = line.replace("<\div>", "\n<\div>\n");
    if line[-2:-1] == '-':
        line=line[:-2]+fp.readline();
    else:
        fw.write(line);
        line=fp.readline();
fp.close();
fw.close();

