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

```
from testc.regression.helper import RegressionRunner
RegressionRunner.execute("regression_3c129_tutorial")
```

### Writing your own classes

## Jenkins Integration

## About CASA

See [http://casa.nrao.edu/](casa.nrao.edu) for more info and licenses.