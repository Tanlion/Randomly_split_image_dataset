# Randomly_split_image_dataset
This code is for spliting a whole image dataset with its annotation data into 'train', 'val', 'test' and corresponding annotation folders randomly. The ratio selected in this file is 7:2:1.

The original data folder dir is like below:

└── folder
    ├── Image
    │   └── 00001.jpg
    │   └── 00002.jpg
    │   └── 00003.jpg
    │   └── ......
    └── Annotation
    │   └── 00001.png
    │   └── 00002.png
    │   └── 00003.png
    │   └── ......
    
    
The target dir would be like this:

└── folder
    ├── train
    │   └── 00011.jpg
    │   └── 00032.jpg
    │   └── 00053.jpg
    │   └── ......
    └── trainannot
    │   └── 00011.png
    │   └── 00032.png
    │   └── 00053.png
    │   └── ......
    ├── val
    │   └── 00021.jpg
    │   └── 00062.jpg
    │   └── 00083.jpg
    │   └── ......
    └── valannot
    │   └── 00021.png
    │   └── 00032.png
    │   └── 00083.png
    │   └── ......
    ├── test
    │   └── 00001.jpg
    │   └── 00092.jpg
    │   └── 00103.jpg
    │   └── ......
    └── testannot
    │   └── 00001.png
    │   └── 00092.png
    │   └── 00103.png
    │   └── ......
    ├── train.txt
    ├── val.txt
    ├── test.txt
    
    
