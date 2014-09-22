#!/usr/bin/env python

import os
import sys
import json

from optparse import OptionParser

from casa.test.guides import extract

if __name__ == "__main__":

    # defined by the profile
    default_config = ("%s/%s") % (os.getenv("CGUIDES_CONFIG"), "cguides.json") 
    default_extracted_dir = os.getenv("CGUIDES_EXTRACTED")

    default_config = os.getenv("CGUIDES_CONFIG") + "/cguides.json"
    default_ws_pass1 = os.getenv("CGUIDES_PASS1")

    # options
    parser = OptionParser()
    parser.add_option('-b', '--benchmark', action="store_true", default=False, help="produce benchmark test script" )
    parser.add_option('-n', '--noninteractive', action="store_true", default=False, help="make script non-interactive (non-benchmark mode only)")
    parser.add_option('-p', '--plotmsoff', action="store_true", help="turn off all plotms commands")
    parser.add_option('-c', '--config', help="Get the guides specified in a json file", default=default_config)
    parser.add_option('-o', '--output', help='output dir for files', default=default_extracted_dir)
    
    (options, args) = parser.parse_args()

    # iterate over the configuration file
    with open(options.config) as json_data:
        json_obj = json.load(json_data)
        base_uri = json_obj["base_uri"]

        for element in json_obj["guides"]:
            if element["enable"]:
                uri = base_uri + element["guide"]
                try:
                    extract.main(uri, options)
                except Exception, e:
			    	print "Something has gone wrong with %s: \n %s" % (script, e)
    json_data.
