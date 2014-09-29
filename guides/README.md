# Guides

## Configuration file

The guides to use must be specified in the [guides.conf](https://github.com/atejeda/casa-testing/blob/master/guides/guides.conf) configuration file.

```
{
    "base_uri": "http://casaguides.nrao.edu/index.php?title=",

    "guides": [
        { "enable": 1, "uri": "EVLA_3-bit_Tutorial_G192", "guide": "EVLA3BitTutorialG192.py", "template": "guides.template" }
    ]
}
```

By using a configuration file, allows more flexibility to manage or group the tests.

### Fields

   * enable: ```1``` for enable and ```0``` for disable the extraction and code parse/generation for the guide.
   * guide: Is the guide identifier, the extracted guide and the generated code will use this identifier.
   * template: Which template to use.

## Template and code parsing/generation

```Airspeed``` is used for the template and code generation, currently [guides.template](https://github.com/atejeda/casa-testing/blob/master/guides/guides.template) is used to generate ```RegressionBase > unittest.TestCase``` pyunit test classes, in which each ```keyword-phrase``` and his python code within the guide is a test case method of the generated class.

An example of a generated class:

```
#!/usr/bin/env python

# This is a generated module
# all modified changes will be lost in the next code generation

# Defined keyword-phrases 
# keyword-phrase: "initial data split" 
# keyword-phrase: "initial listobs run" 
# keyword-phrase: "creating a plot of the already flagged data" 

import sys

assert sys.version >= '2' and sys.version_info.minor >= 7, "Python 2.7 or greater is supported"

import os
import unittest

from testc.regression.helper import RegressionHelper
from testc.regression.helper import RegressionBase

__all__ = ["Test_EVLA3BitTutorialG192"]

class Test_EVLA3BitTutorialG192(RegressionBase):
  """ Testing guides from EVLA_3-bit_Tutorial_G192
  """

  @classmethod
  def setUpClass(class_instance):
    pass

  def setUp(self):
    pass

  def tearDown(self):
    pass

  @classmethod
  def tearDown(class_instance):
    pass

  def test_EVLA3BitTutorialG192_00_initial_data_split(self):
    """Test EVLA_3-bit_Tutorial_G192 (EVLA3BitTutorialG192) "initial data split" 
    """
    self.execute("casapy_EVLA3BitTutorialG192_00_initial_data_split")

  def test_EVLA3BitTutorialG192_01_initial_listobs_run(self):
    """Test EVLA_3-bit_Tutorial_G192 (EVLA3BitTutorialG192) "initial listobs run" 
    """
    self.execute("casapy_EVLA3BitTutorialG192_01_initial_listobs_run")

  def test_EVLA3BitTutorialG192_02_creating_a_plot_of_the_already_flagged_data(self):
    """Test EVLA_3-bit_Tutorial_G192 (EVLA3BitTutorialG192) "creating a plot of the already flagged data"
    """
    self.execute("casapy_EVLA3BitTutorialG192_02_creating_a_plot_of_the_already_flagged_data")
```

As one can see, the method is generated as ```test_<guide>_<auto-incremental-id>_<keyword-phrase>``` and executes the ```casapy_<guide>_<auto-incremental-id>_<keyword-phrase>.py``` is script by using inherited ```RegressionBase``` helper methods. 

The CASA guide keyword-phrase code is located in a code snippet named as ```casapy_<guide>_<auto-incremental-id>_<keyword-phrase>.py```, it only contains the code to be executed by casa, this script is generated in the same directory where the test class was generated.

Using the same example, in summary, will be generated (according to the configuration file:

   * A test class for the casa guide, each test case method is a keyword-phrase.
   * A python script with the keyword-phrase content to be executed within in a CASA environment.

```
guide/
|-- regression_EVLA3BitTutorialG192.py
|-- casapy_EVLA3BitTutorialG192_00_initial_data_split.py
|-- casapy_EVLA3BitTutorialG192_01_initial_listobs_run.py
|-- casapy_EVLA3BitTutorialG192_02_creating_a_plot_of_the_already_flagged_data.py
|-- extract.py
|-- merge.py
|-- __init__.py
```

## keywords-phrases

TBD

## How to

### Extraction

TBD

### Merge

The merge script needs to know the configuration file to use and where the extracted scripts are, by default it will look for it the current working directory.

```
parser.add_option('-c', "--config", dest="config", help="The configuration file to use", default="guides.conf")
parser.add_option("-e", "--extracted", dest="extracted", help="Where the extracted scripts are", default="%s/ws/extracted" % os.getcwd())
```

A verbose example of a ```merge``` execution:

```
- EVLA_3-bit_Tutorial_G192 -----------------------------------------------------
script   : /a/dir/guides/ws/extracted/EVLA3BitTutorialG192.py
template : guides.template
output   : /a/dir/testc/guide
```

By default, for ```convention over configuration``` purposes, the code generated will be located in the same directory where the ```merge``` module is: ```testc/guide```, this approach allows to separate the regression test from the guide tests (which also are regression tests).

### Execute

You have to be sure that the testc is installed in the lib directory in your CASA installation. The following code snippet can be executed within a CASA
environment:

```
from testc.regression.helper import RegressionRunner
RegressionRunner.execute("regression_EVLA3BitTutorialG192", guide = True)
```

An example verbose:

```
Test EVLA_3-bit_Tutorial_G192 (EVLA3BitTutorialG192) "initial data split" ... ok
Test EVLA_3-bit_Tutorial_G192 (EVLA3BitTutorialG192) "initial listobs run" ... ok
Test EVLA_3-bit_Tutorial_G192 (EVLA3BitTutorialG192) "creating a plot of the already flagged data" ... ok

----------------------------------------------------------------------
XML: test_evla3bittutorialg192.xml
----------------------------------------------------------------------
Ran 3 tests in 0.019s

OK
True
```

The only difference with the regression tests, from a execution point of view, is that the ```guide = True``` should be specified for the ```RegressionRunner.execute``` in order to find the regression test class in the guide package, an automated way can be easily implemented to locate the module, but was done in this way in order to avoid collisions with the module file name.

In order to know how to use ```RegressionRunner``` and ```RegressionBase``` helper metods, refer to the regression documentation.

