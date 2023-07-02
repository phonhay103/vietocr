python test.py \
++gpu_id=3 \
++trainer.export="weights/train_new_CGGANv2_183_6222.pth" \
++train_lmdb="datasets/lmdb/trainV2_CGGANv2.2" \
++valid_lmdb="datasets/lmdb/validV2" \
++test_lmdb="datasets/lmdb/testV2" \
++dataloader.num_workers=10