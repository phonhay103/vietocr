python train.py \
++project="vietocr_new" \
++name="Train old" \
++gpu_id=1 \
++dataset.data_root="/mnt/disk3/CGGANv2" \
++dataset.train_annotation="datasets/labels/train.txt" \
++dataset.valid_annotation="datasets/labels/valid.txt" \
++dataset.test_annotation="datasets/labels/test.txt" \
++dataset.train_lmdb="datasets/lmdb/train" \
++dataset.valid_lmdb="datasets/lmdb/valid" \
++dataset.test_lmdb="datasets/lmdb/test" \
++trainer.export="weights/train_old.pth" \
++trainer.log="logs/train_old.log" \
++dataloader.num_workers=20