
Check that Detectron tests pass (e.g. for SpatialNarrowAsOp test):

ERROR: test_large_forward (__main__.SpatialNarrowAsOpTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/kaidipei/research/Detectron/detectron/tests/test_spatial_narrow_as_op.py", line 68, in test_large_forward
    self._run_test(A, B)
  File "/home/kaidipei/research/Detectron/detectron/tests/test_spatial_narrow_as_op.py", line 37, in _run_test
    workspace.FeedBlob('A', A)
  File "/home/kaidipei/anaconda2/lib/python2.7/site-packages/caffe2/python/workspace.py", line 315, in FeedBlob
    return C.feed_blob(name, arr, StringifyProto(device_option))
RuntimeError: [enforce fail at common_cudnn.h:108] version_match || backwards_compatible_7 || patch_compatible. 
cuDNN compiled (7102) and runtime (7005) versions mismatch 

This is due to pre-built caffe2 has different cuDNN version.
