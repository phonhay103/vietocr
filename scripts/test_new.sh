python test.py \
++gpu_id=2 \
++trainer.export="weights/train_new.pth" \
++train_lmdb="datasets/lmdb/trainV2" \
++valid_lmdb="datasets/lmdb/validV2" \
++test_lmdb="datasets/lmdb/testV2" \
++dataloader.num_workers=20