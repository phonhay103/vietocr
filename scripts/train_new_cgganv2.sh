python train.py \
++project="vietocr_new" \
++name="Train new | CGGAN 84 words SSIM Q2" \
++gpu_id=3 \
++dataset.data_root="/mnt/disk3/CGGANv2" \
++dataset.train_annotation="datasets/labels/trainV2_CGGANv2.2.txt" \
++dataset.valid_annotation="datasets/labels/validV2.txt" \
++dataset.test_annotation="datasets/labels/testV2.txt" \
++dataset.train_lmdb="datasets/lmdb/trainV2_CGGANv2.2" \
++dataset.valid_lmdb="datasets/lmdb/validV2" \
++dataset.test_lmdb="datasets/lmdb/testV2" \
++trainer.export="weights/train_new.pth" \
++dataloader.num_workers=10 \
++aug.image_aug=false \
++force=false