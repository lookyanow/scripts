#!/usr/bin/python	

import re

pattern = re.compile(" \d{3,3} ")
match = pattern.findall("100 44444 123 asdfsd 345 986987 asdasd")
print match

