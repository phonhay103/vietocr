python test.py \
++gpu_id=3 \
++trainer.export="weights/train_new_CGGANv2_183_6222.pth" \
++dataset.valid_lmdb="datasets/lmdb/validV2" \
++dataset.test_lmdb="datasets/lmdb/testV2" \
++dataloader.num_workers=20