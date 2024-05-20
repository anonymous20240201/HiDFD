import cv2
import os
from PIL import Image

path = '/opt/data/common/Data_set/ILSVRC2012/imagenet/train'
save_path = './data/I64/train'
size = 32
count = 0
for i in os.listdir(path):
    print(count)
    count = count + 1
    subdir = os.path.join(path, i)
    subdir_save = os.path.join(save_path, i)
    if i == 'valprep.sh':
        continue
    if not os.path.exists(subdir_save):
        os.makedirs(subdir_save)
    img_list = os.listdir(subdir)
    # img_list = img_list[:50]
    for j in img_list:
        img_dir = os.path.join(subdir, j)
        img_save_dir = os.path.join(subdir_save, j)
        img = cv2.imread(img_dir)
        img = cv2.resize(img, (size, size))
        cv2.imwrite(img_save_dir, img)

        # img = Image.open(img_dir)
        # # print(im)
        # # Convert grayscale images into 3 channels
        # if img.mode != "RGB":
        #     img = img.convert(mode="RGB")
        #
        # im_resized = img.resize((size, size))
        # # Get rid of extension (.jpg or other)
        # im_resized.save(os.path.join(img_save_dir))
