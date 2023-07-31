python train.py \
++project="vietocr_new" \
++name="Train new | augment | CGGAN 84 words FULL" \
++gpu_id=1 \
++dataset.data_root="/mnt/disk3/CGGANv2" \
++dataset.train_annotation="datasets/labels/train_new_cggan_84_no_filter.txt" \
++dataset.valid_annotation="datasets/labels/validV2.txt" \
++dataset.test_annotation="datasets/labels/testV2.txt" \
++dataset.train_lmdb="datasets/lmdb/train_new_cggan_84_no_filter" \
++dataset.valid_lmdb="datasets/lmdb/validV2" \
++dataset.test_lmdb="datasets/lmdb/testV2" \
++trainer.export="weights/train_new_cggan_84_no_filter.pth" \
++dataloader.num_workers=10 \
++aug.image_aug=true \
++force=false