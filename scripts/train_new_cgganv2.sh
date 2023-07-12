python train.py \
++project="vietocr_new" \
++name="Train new + CGGANv2 | 84 - filter" \
++gpu_id=1 \
++dataset.data_root="/mnt/disk3/CGGANv2" \
++dataset.train_annotation="datasets/labels/trainV2_CGGANv2.2.txt" \
++dataset.valid_annotation="datasets/labels/validV2.txt" \
++dataset.test_annotation="datasets/labels/testV2.txt" \
++dataset.train_lmdb="datasets/lmdb/trainV2_CGGANv2.2" \
++dataset.valid_lmdb="datasets/lmdb/validV2" \
++dataset.test_lmdb="datasets/lmdb/testV2" \
++trainer.export="weights/trainV2_CGGANv2.2.pth" \
++dataloader.num_workers=20