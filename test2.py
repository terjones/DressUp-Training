############################################################################
#This program converts an .srt file that uses commas for decimal points
#into a .vtt file.
#
#Author: Benjamin Niedzielski (bniedzie@ucla.edu)
#Last Modified: 8/12/2019
############################################################################
import re;
import sys;

readFile = 'newtest.txt';
writeFileBase = 'test/page';
writeFile = writeFileBase;
count = 1;

fp = open(readFile, 'r');
fw = None;
line = fp.readline();
while line:
    if line == "<div class=\"PageNum\">\n":
        line = "";
        if (fw != None):
            fw.close();
        fw = open((writeFile + str(count) + '.txt'), 'w');
        count = count + 1;
    line=fp.readline();
    regex = re.compile(".*?<(.*?)>")
    if line != "<div class=\"PageNum\">\n":
        line = re.sub(regex, '', line)
        if fw != None:
            fw.write(line);
fp.close();
if fw != None:
    fw.close();

