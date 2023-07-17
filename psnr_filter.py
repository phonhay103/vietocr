import pandas as pd
import numpy as np

with open('datasets/labels/psnr_47_32_96.txt') as f:
    lines = f.read().splitlines()
    df = pd.DataFrame([line.split('\t') for line in lines], columns=['filename', 'psnr'])
    df = df.astype({'psnr': np.float32})
    df = df[df['psnr'] >= df['psnr'].quantile(0.25)]
    filenames = df.filename.values.tolist()

with open('datasets/labels/CGGANv2.2_47_no_filter.txt') as f:
    lines = f.read().splitlines()
    lines = [line for line in lines if line.split('\t')[0] in filenames]

with open('datasets/labels/CGGANv2.2_47_PSNR_Q1.txt', 'w') as f:
    f.write('\n'.join(lines).rstrip())