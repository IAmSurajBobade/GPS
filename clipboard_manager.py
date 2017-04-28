# -*- coding: utf-8 -*-

import win32clipboard as w
from datetime import datetime

from pyparsing import line

w.OpenClipboard()
d = w.GetClipboardData(w.CF_TEXT)
w.CloseClipboard()

str_file_path = "C:\Users\Suraj.Bobade\Desktop"
str_file_name = datetime.date()

print str_file_name
