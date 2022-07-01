# stide

The algorithm in this repository evaluates the STIDE [1] algorithm on the HDFS log data set [2]. The STIDE algorithm learns a set of subsequences of a given length from a sequence of event types during the training phase. In the detection phase, each new subsequence that is not known from the training phase is reported as an anomaly. The idea is that abnormal event sequences in the HDFS log data set involve new event types or different combinations of co-occurring events, which can be used for detection. In addition, we also learn the shortest length of any sequence in the training phase and also generate anomalies for new sequences that are shorter than the minimum. The reason for this is that many abnormal event sequences in the HDFS log data set are very short.

Run the STIDE algorithm with the following command to obtain the evaluation results:

```
ubuntu@user-1:~/stide$ python3 stide.py
Window-size=2
Min-length=15
TP=15997
FP=795
TN=552571
FN=841
TPR=R=0.9500534505285664
FPR=0.0014366621729560544
TNR=0.998563337827044
P=0.9526560266793711
F1=0.9513529586678561
ACC=0.9971308514145815
```

The algorithm achieves an accuracy of 99.7% for a sequence length (=window-size) of 2. Feel free to edit the `stide.py` file and try out different settings for the window-size which is defined in the first line. Even a window-size of 1 yields an accuracy of 99.5% as most of the anomalous sequences can be identified by new event types and their short lengths.

[1] [Forrest, Stephanie, et al. "A sense of self for unix processes." Proceedings 1996 IEEE Symposium on Security and Privacy. IEEE, 1996](https://ieeexplore.ieee.org/abstract/document/502675)

[2] HDFS log data set taken without changes from the [DeepLog implementation by wuyifan18](https://github.com/wuyifan18/DeepLog)
