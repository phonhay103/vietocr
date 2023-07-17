python test.py \
++gpu_id=3 \
++trainer.export="weights/train_new.pth" \
++dataset.valid_lmdb="datasets/lmdb/validV2" \
++dataset.test_lmdb="datasets/lmdb/testV2" \
++dataloader.num_workers=20