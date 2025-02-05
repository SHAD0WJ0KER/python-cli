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

For now, clone this repository (pypi distribution is planned down the road). 
From the command line run `pip install -r requirements.txt`. Then, run command `pip install .` (if you intend to change the code add option `-e`, so you won't need to reinstall module with every code change). Afterwards, go into your python script and run:

```py
from colored_utils.main import Colored_utils
cu = Colored_utils()

cu.success()
```

This should successfully install and import module for your use. 

> [!NOTE]
> Due