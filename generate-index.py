#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2020 Anaconda, Inc
import os
from os.path import dirname, join
import sys

from jinja2 import Template

_TEMPLATE = """\
<html>
<head>
  <title>Conda Schemas</title>
  <style type="text/css">
    a, a:active {
      text-decoration: none; color: blue;
    }
    a:visited {
      color: #48468F;
    }
    a:hover, a:focus {
      text-decoration: underline; color: red;
    }
    body {
      background-color: #F5F5F5;
    }
    h2 {
      margin-bottom: 12px;
    }
    th, td {
      font: 100% monospace; text-align: left;
    }
    th {
      font-weight: bold; padding-right: 14px; padding-bottom: 3px;
    }
    th.tight {
        padding-right: 6px;
    }
    td {
      padding-right: 14px;
    }
    td.tight {
        padding-right: 8px;
    }
    td.s, th.s {
      text-align: right;
    }
    td.summary {
      white-space: nowrap;
      overflow: hidden;
    }
    td.packagename {
      white-space: nowrap;
      text-overflow: ellipsis;
      overflow: hidden;
      max-width: 180px;
      padding-right: 8px;
    }
    td.version {
      //white-space: nowrap;
      overflow: hidden;
      max-width: 90px;
      padding-right: 8px;
    }
    table {
      background-color: white;
      border-top: 1px solid #646464;
      border-bottom: 1px solid #646464;
      padding-top: 10px;
      padding-bottom: 14px;
    }
    address {
      color: #787878;
      padding-top: 10px;
    }
  </style>
</head>
<body>
  <h2>Conda Schemas</h2>
  {% for subdir in subdirs %}<a href="{{ subdir }}">{{ subdir }}</a>&nbsp;&nbsp;&nbsp;{% endfor %}
  <table>
    <tr>
      <th>File</th>
    </tr>
{% for fn in files %}
    <tr>
      <td><a href="{{ fn }}">{{ fn }}</a></td>
    </tr>
{%- endfor %}
  </table>
</body>
</html>

"""

files=sorted(p for p in os.listdir(".") if p.endswith(".schema.json"))
rendered = Template(_TEMPLATE).render(files=files)

print(rendered, file=sys.stderr)

with open(join(dirname(__file__), "index.html"), "w") as fh:
    fh.write(rendered)