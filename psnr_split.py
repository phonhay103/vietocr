import pandas as pd
import numpy as np

with open('datasets/labels/psnr_183_32_96.txt') as f:
    lines = f.read().splitlines()
    df = pd.DataFrame([line.split('\t') for line in lines], columns=['filename', 'psnr'])
    df = df.astype({'psnr': np.float32})

with open('datasets/labels/CGGANv2.2_47_no_filter.txt') as f:
    lines = f.read().splitlines()
    lines = [line.split('\t')[0] for line in lines]

with open('datasets/labels/psnr_47_32_96.txt', 'w') as f:
    df = df[df['filename'].isin(lines)]
    f.write('\n'.join([str(dt[0]) + '\t' + str(dt[1]) for dt in df.values]).rstrip())