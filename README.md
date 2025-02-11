# python-cli

## Idea behind project

1) Build easy to use library that could be included in all of the other python projects without the need to write it from scratch every time.

2) Get an idea how python packages are written, structured, built and distributed

3) Have a coding project in free time to better my python skills

## Purpose

Make the command line or textual output more readable. 
Use different colors to improve information extraction from a sea of letters.
Gradually increase difficulty of programming requests/tasks.

# How to use

1. clone this repository (pypi distribution is planned down the road)
2. `cd` into the repository and from the command line run `pip install -r requirements.txt`
3. Run command `pip install .`

> [!NOTE]
> Pay attention to the `.` (dot) in above command
   
> [!TIP]
> Run with flag `-e` if you want to change code - for more information: [pip documentation](https://pip.pypa.io/en/stable/topics/local-project-installs/#editable-installs)

4. To test, go into your python script and run:

```py
from colored_utils.main import ColoredUtils
cu = ColoredUtils()

print(cu.success)
```

This should successfully install and import module for your use. 

> [!WARNING]
> Project structure will change.
