---
title: Processing Excel XLSX files with Python
date: 2017-10-09
tags: [splunk, code]
published: true
layout: default
---
# Processing Excel XLSX files with Python

Using Python's [ElementTree](http://effbot.org/zone/element-index.htm) XML
Parser, its possible to quickly parse data within a Microsoft Excel .XLSX file.

An .XLSX file consists of a large number of XML files that are compressed into
a single .ZIP file.  Some Spreadsheets make large use of sharedStrings, where
are strings that are stored in a separate XML file (`sharedStrings.xml`) which
then acts as the source of a lookup for the worksheets. Cells that have a `s`
value in the `t` attribute for a cell contain a sharedString, whose contents
actually exist in another xml fie in the .XLSX. The following script should
form the basis of an .XLSX to .CSV convertor.


```python
#!/usr/bin/env python

import xml.etree.ElementTree as ET
import codecs
import sys
import datetime

def excel_date_to_str(d):
  # excel stores a date as days since 01/01/1900
  # by adding 6933594 to the excel value, we can use python's date module to format it correctly
  ret = None
  try:
    ret = datetime.date.fromordinal(int(d) + 693594).strftime("%A, %d %B %Y")
  finally:
    return ret

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

x = ET.parse(open("xl/sharedStrings.xml"))
sharedStrings = x.getroot()

last_v = None
last_type = None
for event, elem in ET.iterparse("xl/worksheets/sheet1.xml", events=('start', 'end')):
  uri, tag = elem.tag.split("}")

  if event == "start" and tag == "c": # start c tag
      last_v = None
      if "t" in elem.attrib:
        last_type = elem.attrib["t"]
      else:
        last_type = None

  elif event == "end" and tag == "c":   # end c tag
    if "r" in elem.attrib:
      rc = elem.attrib["r"]
      if last_v != None:
        print "RC is ", rc, " = ", last_v

  elif event == "start" and tag == "v": # start v tag

    value = "".join(elem.itertext())
    if last_type == "s":
      last_v = "".join(sharedStrings[int(value)].itertext())
    else:
      last_v = value, "type is ", last_type, excel_date_to_str(value)
```

## References
* [ELementTree Overview](http://effbot.org/zone/element-index.htm)
* [MS's Office XML Specifications](https://msdn.microsoft.com/en-us/library/aa338205(v=office.12).aspx)
