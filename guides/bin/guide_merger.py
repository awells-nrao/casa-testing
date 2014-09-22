#!/usr/bin/env python

import os
import sys
import re
import json

from optparse import OptionParser
from airspeed import *
from casa.test.guides.merge import GuideMerge

if __name__ == '__main__':

    # defaults
    default_config = ("%s/%s") % (os.getenv("CGUIDES_CONFIG"), "cguides.json")
    default_regression_dir = os.getenv("CGUIDES_REGRESSION")
    default_cspec_dir = os.getenv("CGUIDES_CSPECS")
    default_extracted_dir = os.getenv("CGUIDES_EXTRACTED")

    # options
    parser = OptionParser()
    parser.add_option('-c', "--config", dest="config", help="Get the guides specified in a json file", default=default_config)
    parser.add_option("-o", "--output", dest="output", help="Where the file will be generated", default=default_regression_dir)
    parser.add_option("-s", "--script", dest="script", help="Where the extracted scripts are", default=default_extracted_dir)
    parser.add_option("-t", "--cspec", dest="cspec", help="Where the cspecs are", default=default_cspec_dir)

    (options, args) = parser.parse_args()

    # iterate over the configuration
    with open(options.config) as json_data:
        json_obj = json.load(json_data)

        for element in json_obj["guides"]:
            if element["enable"]:
                guide = element["guide"].replace(":","").replace("_","")

                script = ("%s/%s.py") % (options.script, guide)
                template = ("%s/%s.cspec") % (options.cspec, guide)
                output = ("%s/%s.py") % (options.output, guide)

                #try:
                merger = GuideMerge(script, template, output)
                merger.merge()
                #except Exception, e:
                #    print "Something has gone wrong with %s: \n %s" % (script, e)
