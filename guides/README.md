# Guides

## Setup

Source the profile to set the workspace:

```
. guides.profile
```

If your planning to execute this in a non CASA environment, add the libraries to the path, e.g.:

```
export PYTHONPATH=$PYTHONPATH:$PWD/..
```

Airspeed is needed for the template system and code generation, use ```easy_install``` to install the library:

```
easy_install airspeed
```

## Configuration

### Profile

### Directory structure

### Guides and mapping

Under ```config/``` directory, a ```guide.json``` file contains the guides to be extracted and tested, also maps the guide to his template:

```
{
    "base_uri": "http://casaguides.nrao.edu/index.php?title=",
    "guides": [
        { "enable": 1, "guide": "EVLA_3-bit_Tutorial_G192", "template": "EVLA3-bitTutorialG192.template" }
    ]
}
```

## The templates

```Airspeed``` is used for the template and code generation, refer to this page for the airspeed syntax usage.

   * ```#foreach ($entry in $map)```: is the keyword-phrase
   * ```#foreach ($section in $map[$entry])```: the content of each instance of the keyword-phrase, due the keyword-phrase can be specified ```>= 1```.

The ```$section``` is the content of the keyword-phrase ```initial data split```.

```
#if($entry == "initial data split")
$section
#end
```

## Extract

```
Usage: guide_extract.py [options]

Options:
  -h, --help            show this help message and exit
  -b, --benchmark       produce benchmark test script
  -n, --noninteractive  make script non-interactive (non-benchmark mode only)
  -p, --plotmsoff       turn off all plotms commands
  -c CONFIG, --config=CONFIG
                        Get the guides specified in a json file
  -o OUTPUT, --output=OUTPUT
                        output dir for files
```

## Merge

```[
$ guide_merger.py --help

Usage: guide_merger.py [options]

Options:
  -h, --help            show this help message and exit
  -c CONFIG, --config=CONFIG
                        Get the guides specified in a json file
  -o OUTPUT, --output=OUTPUT
                        Where the file will be generated
  -s SCRIPT, --script=SCRIPT
                        Where the extracted scripts are
  -t CSPEC, --cspec=CSPEC
                        Where the cspecs are
```

## Example

Setup the environment described above, create a symlink from workspace/example/EVLA3-bitTutorialG192.py to workspace/extracted/EVLA3-bitTutorialG192.py and execute:

```
guide_merger.py
```

By default it will:

   * read the default guides.json file, this is specified in the profile
   * read the extracted script from workspace/extracted
   * parse the extracted script and by using the template generate the code into workspace/regression

Currently, these keywords are still not added to the guides. An example is already extracted with some keywords

## Keyword-phrase convention/standard


## Data
/home/casa/casaGuideData