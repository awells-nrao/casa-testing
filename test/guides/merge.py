#!/usr/bin/env python

import sys

assert sys.version >= '2' and sys.version_info.minor >= 7, "Python 2.7 or greater is supported"

import os
import re
import json

from optparse import OptionParser
from airspeed import *

__all__ = ["GuideMerge"]

class GuideMerge:

    def __init__(self, script, template, output):
        self.__script_path = script
        self.__template_path = template
        self.__output_path = output

    def __read_phrases(self):
        phrases = []

        with open(self.__script_path, 'r') as script:      
            phrase = None
            base_re = "(((# In CASA)+(:?)){1})+"
            append_line = False

            for line in script:
                is_incasa = re.search("%s.*" % base_re, line)
                is_phrase = re.search("%s.(\w)+" % base_re, line)

                if is_incasa:
                    phrase = None

                if phrase and len(line) and not is_incasa:
                    phrases[-1:][0][1] += line

                if is_incasa and is_phrase:
                    phrase = re.split(base_re, line)[-1:][0].strip()
                    phrases.append([phrase, ""])

        return phrases

    def __merge(self, template_data, template_helper):
        template = Template(template_data)
        return template.merge(locals())
        
    def __generate_snippets(self):

        guide = self.__script_path.split("/")[-1:][0].split(".")[0]
        snippet_dir = "/".join(self.__output_path.split("/")[:-1])
        for entry in self._map:
            counter = 0
            for content in self._map[entry]:
                 entry_script = "%s/cexec_%s_%s_%s.py" % (snippet_dir, guide, entry.replace(" ", "_").lower(), counter)
                 self.__write(entry_script, content)

    def __beautifier(self, body):
        lines = body.splitlines()
        size = len(lines)
        beautified = ""

        for i in range(0, size):
            if len(lines[i].strip()) and not len(lines[i - 1].strip()) and i:
                beautified += ("\n%s\n") % lines[i]
            elif len(lines[i].strip()):
                beautified += ("%s\n") % lines[i]
                
        return beautified

    def __read(self, file):
        self.__assert_file(file)
        content = None
        with open(file, 'r') as template:
            content = template.read()
        return content

    def __write(self, file, data):
        with open(file, 'w') as output:
            output.write(data)

    def __assert_file(self, file):
        assert os.access(file, os.F_OK), "%s not exists" % file

    def merge(self):
        phrases = self.__read_phrases()
        template = self.__read(self.__template_path)

        template_helper = {}
        template_helper["phrases"] = phrases
        template_helper["guide"] = self.__script_path.split("/")[-1:][0].split(".")[0]

        merged_raw = self.__merge(template, template_helper) 
        merged_beautified = self.__beautifier(merged_raw)
        self.__write(self.__output_path, merged_beautified)

        #self.__generate_snippets()
