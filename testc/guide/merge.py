#!/usr/bin/env python

import sys

#assert sys.version >= '2' and sys.version_info.minor >= 7, "Python 2.7 or greater is supported"

import os
import re
import json
import errno

from optparse import OptionParser

from airspeed import *

from testc import guide

__test__ = False
__all__ = ["GuideMerge"]

class GuideMerge:
    # event that is a class, it will used the methods as they were static ones
    # based that is a proof of concept, this can be improved later

    def __init__(self, script, template, template_helper,  output, uri):
        self.__script = script
        self.__template = template
        self.__template_helper = template_helper
        self.__output_path = output
        self.__guide_uri = uri

    def __read_phrases(self, to_parse):
        phrases = []

        self.__assert_file(to_parse)

        with open(to_parse, 'r') as script:      
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

    def __generate_code(self, template_data, template_helper):
        template = Template(template_data)
        return template.merge(locals())
        
    def __generate_snippets(self, output_path, guide_script_name, phrases):
        counter = 0
        self.__mkdir("%s/%s" % (output_path, guide_script_name))
        for phrase in phrases:
            snippet = "%s/%s/casapy_%s_0%s_%s.py" % (output_path, guide_script_name, guide_script_name, counter, self.__normalize_phrase(phrase[0]))
            self.__write(snippet, phrase[1])
            counter += 1

    def __normalize_phrase(self, phrase):
        replaces = [ "-", "+", "_", " "]
        for replace in replaces:
            phrase = phrase.replace(replace, "_")
        return phrase.lower()

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

    def __get_base_path(self, file):
        pass

    def __get_guide_name(self, guide):
        """From the absolute path, return just only the
        extracted name dir, the guide_name is normalized
        """
        return guide.split("/")[-1:][0].split(".")[0]

    def __mkdir(self, path):
        try:
            os.makedirs(path)
        #this is for python > 2.5
        except OSError as e:
            if e.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else: raise e

    def merge(self):
        template = self.__read(self.__template)
        helper_template = self.__read(self.__template_helper)

        phrases = self.__read_phrases(self.__script)
        guide_script_name = self.__get_guide_name(self.__script) # name already normilized

        template_helper = {}
        template_helper["phrases"] = phrases
        template_helper["guide"] = guide_script_name
        template_helper["uri"] = self.__guide_uri

        merged_raw = self.__generate_code(template, template_helper)
        merged_beautified = self.__beautifier(merged_raw)
        self.__write("%s/regression_%s.py" % (self.__output_path, guide_script_name), merged_beautified)

        helper_merged_raw = self.__generate_code(helper_template, template_helper)
        helper_merged_beautified = self.__beautifier(helper_merged_raw)
        self.__write("%s/casapy_helper_%s.py" % (self.__output_path, guide_script_name), helper_merged_beautified)

if __name__ == '__main__':

    parser = OptionParser()
    parser.add_option('-c', "--config", dest="config", help="The configuration file to use", default="guides.conf")
    parser.add_option("-e", "--extracted", dest="extracted", help="Where the extracted scripts are", default="%s/ws/extracted" % os.getcwd())

    (options, args) = parser.parse_args()

    # iterate over the configuration
    with open(options.config) as json_data:
        json_obj = json.load(json_data)

        for element in json_obj["guides"]:
            if element["enable"]:
                guide_uri = element["uri"].strip()
                extracted_script = "%s/%s" % (options.extracted, element["guide"].strip()) # absolute
                template = element["template"].strip() # absolute
                template_helper = element["template_helper"].strip() # absolute
                output_path = "/".join(guide.__file__.split("/")[:-1]) # where this module is located

                print "- %s %s" % ( guide_uri, "-"*(77 - len(guide_uri)))
                print "script   : %s" % extracted_script
                print "template : %s" % template
                print "output   : %s" % output_path

                try:
                    merger = GuideMerge(extracted_script, template, template_helper, output_path, guide_uri)
                    merger.merge()
                except Exception, e:
                    print "Something went wrong with %s: \n %s" % (guide_uri, e)