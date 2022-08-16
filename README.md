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

The following plot shows an overview of the test data (training data is exluded). The minimal sequence length known from the training data is indicated with a dashed line and shows that it is suitable to separate around 37% of the anomalous samples correctly just based on their lengths (note that many points overlap in the plot). Moreover, detecting new event types (Seq=1) allows to detect around 47% of the anomalies and sequences (Seq=2) allows to detect around 11% of the remaining anomalies. Around 5% of the anomalies are not detected.

<p align="center"><img src="https://github.com/ait-aecid/stide/blob/main/scatter.png" width=100% height=100%></p>

[1] [Forrest, Stephanie, et al. "A sense of self for unix processes." Proceedings 1996 IEEE Symposium on Security and Privacy. IEEE, 1996](https://ieeexplore.ieee.org/abstract/document/502675)

[2] HDFS log data set taken without changes from the [DeepLog implementation by wuyifan18](https://github.com/wuyifan18/DeepLog)
