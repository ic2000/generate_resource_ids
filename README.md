# generate_resource_ids
A simple script to generate a header file containing macro definitions for the IDs of a resource file.

## Usage

```
usage: generate_resource_ids.py [-h] inputfile outputfile

Generate a header file containing macro definitions for the IDs of a resource file.

positional arguments:
  inputfile   the path of the resource file
  outputfile  the path where the header file will be generated

optional arguments:
  -h, --help  show this help message and exit
```

Use the generated header file as the resource header file or `#include` it.

> **_NOTE:_** Resource names must follow the WinAPI/MFC ID naming convention by using the prefix `ID_` or `IDX_` (where X refers to a variable letter) to be recognised by the script. See the full list of ID prefixes [here]( https://docs.microsoft.com/en-us/cpp/mfc/tn020-id-naming-and-numbering-conventions?view=msvc-160.).
