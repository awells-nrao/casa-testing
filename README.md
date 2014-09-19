# CASA testing

Is a bunch of python scritps to execute the tests wrapped in a pyunit, later to be execute by nose.

## Usage

Copy the ```test``` directory into the python directory of your casa installation and within CASA, 

```
from test.regression.helper import RegressionRunner
RegressionRunner.execute("regression_3c129_tutorial")
```

### Naming convention

   * ```regression_{test}.py```: Is a ```test.helper.RegressionBase``` > ```unit.TestCase``` class, which execute the CASA executable script if is needed.
   * ```cexec_{test}.py```: Is a CASA executable script, intended to be executing within the CASA environment.

## Define a new regression test

The easy way to do it, is by modifying the provided templates, take a look to the pyunit hints.

### Pyunit hints

## About CASA

See [http://casa.nrao.edu/](casa.nrao.edu) for more info and licenses.