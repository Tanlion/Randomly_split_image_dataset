'''
Put this 'divide.py' under the same dir with Image dataset.
Please manually delete all "train", "val", "test" folders and all "train.txt", "val.txt", "test.txt" first.
The code will random divide all the images to train, val and test folders with the ratio of 7:2:1.
And creat txt file for images in train, val and test folders.
The ratio can be customized.
Notice: to run this code, manually delete the existent train, val, test folders first！
'''
import os
import random
import shutil
import PIL.Image as Image


#create new folder if it doesn't exist
def mkdir(path):
    import os
    path = path.strip() #delete space in head
    path = path.rstrip('\\') # delete \ in tail

    isExists = os.path.exists(path)

    if not isExists:
        os.makedirs(path)
        print(path)
        print('Successfully create a new folder as ' + path)
        return True
    else:
        print(path)
        print('The folder already exists')
        return False



#get all files paths and their names in a certain dir path
def each_file(dir_path):
    path_dir = sorted(os.listdir(dir_path)) #sorting all files under dir
    img_name = []    #list of all images' names
    all_img_path = []    #list of all images' paths
    for file_path in path_dir:
        child = os.path.join('%s%s' % (dir_path, file_path))
        img_name.append(file_path)
        all_img_path.append(child)
    return all_img_path, img_name
# print(each_file(img_path))        #['./Image/00001.jpg',  ['00001.jpg', '00002.jpg',



# #move images to train, val, test folders
def create_fold_txt (list, name, fname):
    for i in sorted(list):
        im = Image.open(i)
        im = im.convert("RGB")
        i = i.replace('Image', name)
        im.save(i)
        i_annot = i[-9 : -4]
        i_annot = annot_path + i_annot + '.png'
        imm = Image.open(i_annot)
        i_annot = i_annot.replace('Annotation', name +'annot')
        imm.save(i_annot)
        # name = 'f' + name
        fname.write(i + ' ' + i_annot + '\n')


if __name__ == '__main__':
    train_ratio = 0.7   # 300 * 0.7 == 210
    val_ratio = 0.2     #  300 * 0.2 == 60
    test_ratio = 0.1    # 300 * 0.1 == 30

    data_dir = './'
    img_path = os.path.join(data_dir, 'Image/')  # ./Image
    annot_path = os.path.join(data_dir, 'Annotation/')  # ./Annotation
    txt_path = os.path.join(data_dir)

    file_path, img_list = each_file(img_path)   #['./Image/00001.jpg',  ['00001.jpg', '00002.jpg',
    annotf_path, annot_list = each_file(annot_path)
    # make images in a random order and calculate the portion of train, val, test parts.
    random.shuffle(file_path)
    train_list = file_path[0: int(train_ratio * len(file_path))]
    val_list = file_path[int(train_ratio * len(file_path)): int((train_ratio + val_ratio) * len(file_path))]
    test_list = file_path[int((train_ratio + val_ratio) * len(file_path)):]

    #creat new folders
    mkdir('./train')
    mkdir('./val')
    mkdir('./test')
    mkdir('./trainannot')
    mkdir('./valannot')
    mkdir('./testannot')

    #write image path to txt, if txt dosen't exist, create a new one.
    ftrain = open('train.txt', 'w')
    ftest = open('test.txt', 'w')
    fval = open('val.txt', 'w')

    #move images and annotation images to folders and write names to txt
    create_fold_txt(train_list, 'train', ftrain)
    create_fold_txt(val_list, 'val', fval)
    create_fold_txt(test_list, 'test', ftest)

    ftrain.close()
    ftest.close()
    fval.close()

