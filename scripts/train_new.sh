python train.py \
++project="vietocr_naver" \
++name="Train original" \
++gpu_id=0 \
++dataset.data_root="/mnt/disk3/CG-GAN/training_data/new_train" \
++dataset.train_annotation="/mnt/disk3/CG-GAN/VN_train_2.txt" \
++dataset.valid_annotation="/mnt/disk3/CG-GAN/VN_val_2.txt" \
++dataset.test_annotation="/mnt/disk3/CG-GAN/VN_val_2.txt" \
++dataset.train_lmdb="datasets/lmdb/trainV2" \
++dataset.valid_lmdb="datasets/lmdb/validV2" \
++dataset.test_lmdb="datasets/lmdb/testV2" \
++trainer.export="weights/train_new.pth" \
++dataloader.num_workers=20 \
++aug.image_aug=false \
++force=false