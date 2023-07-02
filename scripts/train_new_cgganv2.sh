python train.py \
++project="vietocr_new" \
++name="Train new CGGANv2 - 183 words - 6222 samples" \
++gpu_id=2 \
++dataset.data_root="/mnt/disk3/CGGANv2" \
++dataset.train_annotation="datasets/labels/trainV2_CGGANv2.2.txt" \
++dataset.valid_annotation="datasets/labels/validV2.txt" \
++dataset.test_annotation="datasets/labels/testV2.txt" \
++dataset.train_lmdb="datasets/lmdb/trainV2_CGGANv2.2" \
++dataset.valid_lmdb="datasets/lmdb/validV2" \
++dataset.test_lmdb="datasets/lmdb/testV2" \
++trainer.export="weights/trainV2_CGGANv2.2.pth" \
++trainer.log="logs/train_new_CGGANv2_183_6222.log" \
++dataloader.num_workers=20