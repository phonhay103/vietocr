import shutil
import os
from tqdm import tqdm


label_path = 'datasets/labels/testV2.txt'
source_dir = "/mnt/disk3/CGGANv2"
destination_dir = "/mnt/disk3/TEST"


with open(label_path) as f:
    lines = [line.split('\t')[0] for line in f]
    for file in lines:
        shutil.copy2(os.path.join(source_dir, file), os.path.join(destination_dir, file))