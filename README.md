# CASA testing framework

The main purpose of this approach is provide a standar way and sort of framework to test CASA regression and guides tests by using python xunit framework implementation, nose + plugins and jenkins + plugins.

## Scope

Python, that's it (to be done).

## Architecture, design and implementation

### Architecture

<div align="center">
    <img src="http://s18.postimg.org/kezwcw4l5/architecture.png" />
</div>

### Design

### Implementation

Everything is packaged in a ```testc``` python package.

## How to use

A static method is provided to execute the regression test class, which is located at ```testc/regression```:

```
from testc.regression.helper import RegressionRunner
RegressionRunner.execute("regression_3c129_tutorial")
```

### Writing your own classes

Two things are needed:

   * The class, there's a pre-stablished name convention, all regression classes should be prefixed with ```regresion_<id-of-the-test>```.
   * The script to be executed by/within CASA, using the prefix ```casapy_<id-of-the-test-case>```, which contains only the code to be executed within CASA.


The inherited method ```execute``` is a helper to execute or import the ```casapy_``` module within CASA, is defined by:

```
def execute(self, casapy_script, test_assert = False, import_module = False)
```

   * casapy_script: the ```casapy_``` module to use.
   * test_assert: a future feature to assert outputs of a regression tests.
   * import_module: if True, it will import the module rather than execute it (```execfile```), useful for dummy non casa tests.

The Python xunit implementation provides several methods to deal with data setup and data cleaning, refer to the ```Python xunit hints``` section.

### Python xunit hints

## Jenkins Integration

## About CASA

See [http://casa.nrao.edu/](casa.nrao.edu) for more info and licenses.