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

Few things are needed:

   * The class, there's a pre-stablished name convention, all regression classes should be prefixed with ```regresion_<id-of-the-test>```
      * import the needed helper classes
      * in your tests class, add ```__all__ = ["<name-of-your-class>"]``` for your class be visible for the testing framework (if you want)
      * define your methods, ```test_<name=of-the-method>``` is a must for python xunit
   * The script to be executed by/within CASA, using the prefix ```casapy_<id-of-the-test-case>```, which contains only the code to be executed within CASA

The inherited method ```execute``` is a helper to execute or import the ```casapy_``` module within CASA, is defined by:

```
def execute(self, casapy_script, test_assert = False, import_module = False)
```

   * casapy_script: the ```casapy_``` module to use.
   * test_assert: a future feature to assert outputs of a regression tests.
   * import_module: if True, it will import the module rather than execute it (```execfile```), useful for dummy non casa tests.

Within the testing context, it is possible to define:

   * Several test classes within a module (```regresion_<id-of-the-test>```)
   * Several method / test cases per tests classes
   * Several ```casapy_<id-of-the-test-case>``` executing per method.

Things sare much simpler by using an already implemented class as an example, see the [regression_3c129_tutorial.py](https://github.com/atejeda/casa-testing/blob/master/testc/regression/regression_3c129_tutorial.py).

The Python xunit implementation provides several methods to deal with the test setup per class and per method, refer to the ```Python xunit hints``` section.

### Python xunit hints

Ignoring, works in a method nor class level, just append the decorator, e.g.:

```
@unittest.skip("reason")
```test_<name-of-the-method>```(self): ...
```

Class level helpers, ```setUpClass```  and ```tearDownClass```, are executed just before and after a test class is executed, the ```@classmethod
``` decorator is mandatory.

```
@classmethod
def setUpClass(class_instance): ...
```

```
@classmethod
def tearDownClass(class_instance): ....
````

In both methods, the ```class_instance``` argument is an instance of your testing class object.

The first line of the pydoc added to the ```test_<name-of-the-method>``` will be printed instead of the test name when it is executed.

## Jenkins Integration

## About CASA

See [http://casa.nrao.edu/](casa.nrao.edu) for more info and licenses.