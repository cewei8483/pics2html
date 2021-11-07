# pics2html
## Description
A python program that puts local image files into a single html (so that the pictures can be viewed in browser by scrolling)
- The program does the job recursively from cwd (current working directory)
- A html file is generated under each folder
- Each html file is named by the name of cwd

## Dependencies
Python 3.6 or above (for f-string)

## Execution
Simply run `pic2html.py` by Python (with images in the folder or subfolders of cwd)

e.g. `python.exe .\pic2html.py` in Windows

## Example
Say you have the following file structure:
```
project
│   pics2html.py   
│   file001.jpg
│
└───folder1
│   │   file011.jpg
│   │   file012.jpg
│   │
│   └───subfolder1
│       │   file111.jpg
│   
└───folder2
    │   file021.jpg
    │   file022.jpg
```

After the program is executed, the file sturcture will become:
```
project
│   pics2html.py   
│   file001.jpg
│   project.html (includes file001.jpg)
│
└───folder1
│   │   file011.jpg
│   │   file012.jpg
│   │   folder1.html (includes file011.jpg & file012.jpg)
│   │
│   └───subfolder1
│       │   file111.jpg
│       │   subfolder1.html (includes file111.jpg)
│   
└───folder2
    │   file021.jpg
    │   file022.jpg
    |   folder2.html (includes file021.jpg & file022.jpg)
```

## Options
### -writePic
Add the `-writePic` flag if you want to write the whole image into the html. The html file can then be read even outside the directory, however the file size will be large.

### Align multiple images horizontally
If you want to align multiple images horizontally in the html, there are (at least) two ways to do this:

1. Modify ```<img style="display:block; margin:auto;" ...>``` to  ```<img style="display:inline-block; margin:auto;" ...>``` for the images you want to align (but the alignment will be cancelled if images are too big to be placed in the same inline block)

2. Surround the image tags by a div with ```style="display: flex; justify-content: center;"```, then remove ```margin: auto``` for each image tag inside that div, for example:
```
<div style="display:flex; justify-content:center;">
  <img style="display:block;" src=".\file011.jpg">
  <img style="display:block;" src=".\file012.jpg">
</div>
```
