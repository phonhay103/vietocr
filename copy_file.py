import shutil
import os
from tqdm import tqdm


label_path = 'datasets/labels/CGGANv2.2_6478_no_filter.txt'
source_dir = "/mnt/disk3/CGGANv2"
destination_dir = "/mnt/disk3/GAN/GAN_6478_NF"


with open(label_path) as f:
    lines = [line.split('\t')[0] for line in f]
    for file in tqdm(lines):
        shutil.copy2(os.path.join(source_dir, file), os.path.join(destination_dir, file))