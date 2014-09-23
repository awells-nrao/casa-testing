#!/usr/bin/env python

import sys

assert sys.version >= '2', "Python 2.0 or greater is supported"

import os
import re
import json

from optparse import OptionParser
from airspeed import *

__all__ = ["GuideMerge"]

class GuideMerge:

    def __init__(self, script, template, output):
        self._script = script
        self._template = template
        self._output = output
        self._map = {}
        self._template_str = ""

    # this should be improved > TODO
    def __mapPhrases(self):
    	"""Construct the map/dict  
    	"""
        with open(self._script, 'r') as script:
            phrase = None
            base_re = "(((# In CASA)+(:?)){1})+"
	    appendLine = False

            for line in script:
                isInCASA = re.search("%s.*" % base_re, line)
                isPhrase = re.search("%s.(\w)+" % base_re, line)

                if isInCASA and isPhrase:
                    phrase = re.split(base_re, line)[-1:][0].strip()
		    if not phrase in self._map:
			self._map[phrase] = []
		    self._map[phrase].append("")
		    appendLine = True
		
		if isInCASA and not isPhrase:
		    appendLine = False
                
                if not isInCASA and not isPhrase and phrase and appendLine:
                    self._map[phrase][len(self._map[phrase]) - 1] += line

    def __readTemplate(self):
        with open(self._template, 'r') as template:
            self._template_str = template.read()

    def __merge(self):
    	"""Is using the populated map/dict
    	in order to be expanded in the template
    	"""
        template = Template(self._template_str)

        # local helpers... inefficient but isn't to many string data
        # to hold in memory
        map = self._map
        guide = self._script.split("/")[-1:][0].split(".")[0]

        beautified = self.__beautifier(template.merge(locals()))
        self.__write(self._output, beautified)

    def __generate_snippets(self):
        """ generate the executable snippets in the same workspace
        were regression module is generated
        """
        guide = self._script.split("/")[-1:][0].split(".")[0]
        snippet_dir = "/".join(self._output.split("/")[:-1])
        for entry in self._map:
            counter = 0
            for content in self._map[entry]:
                 entry_script = "%s/cexec_%s_%s_%s.py" % (snippet_dir, guide, entry.replace(" ", "_").lower(), counter)
                 self.__write(entry_script, content)

    def __beautifier(self, body):
    	"""Remove the excesive amount of blank lines
    	in the parsed code
    	"""
        lines = body.splitlines()
        size = len(lines)
        beautified = ""

        for i in range(0, size):
            if len(lines[i].strip()) and not len(lines[i - 1].strip()) and i:
                beautified += ("\n%s\n") % lines[i]
            elif len(lines[i].strip()):
                beautified += ("%s\n") % lines[i]
        return beautified

    def __write(self, file, data):
        with open(file, 'w') as output:
            output.write(data)

    def merge(self):
        self.__mapPhrases()
        self.__readTemplate()
        self.__merge()
        self.__generate_snippets()
