window_size = 2 # Length of subsequences

seqs = set()
min_length = 9999999999999999999

# Learn all subsequences of length window_size from training file
with open('data/hdfs_train') as f:
    for line in f:
        parts = tuple(['-1'] + line.strip('\n').strip(' ').split(' ') + ['-1'])
        for i in range(len(parts) - window_size + 1):
            seqs.add(parts[i:(i+window_size)])
        min_length = min(min_length, len(parts))

#print('Learned sequences:')
#print(seqs)

def detect_anomalies(line, seqs, min_length):
    # Returns True if anomaly is detected and False otherwise
    # Generate anomaly for sequence if any subsequence of length window_size is not present in seqs
    parts = tuple(['-1'] + line.strip('\n').strip(' ').split(' ') + ['-1'])
    detected = False
    for i in range(len(parts) - window_size + 1):
        seq = parts[i:(i+window_size)]
        if seq not in seqs:
            detected = True
            break
    # Also generate anomaly for sequence if length is smaller than minimum length from training file
    if detected is True or len(parts) < min_length:
        return True
    else:
        return False

# Initialize metrics
tp = 0
fn = 0
tn = 0
fp = 0

# Run detection on abnormal data
with open('data/hdfs_test_abnormal') as f:
    for line in f:
        if detect_anomalies(line, seqs, min_length) is True:
            tp += 1
        else:
            fn += 1

# Run detection on normal data
with open('data/hdfs_test_normal') as f:
    for line in f:
        if detect_anomalies(line, seqs, min_length) is True:
            fp += 1
        else:
            tn += 1 

# Print results
print('Window-size=' + str(window_size))
print('Min-length=' + str(min_length))
print('TP=' + str(tp))
print('FP=' + str(fp))
print('TN=' + str(tn))
print('FN=' + str(fn))
print('TPR=R=' + str(tp / (tp + fn)))
print('FPR=' + str(fp / (fp + tn)))
print('P=' + str(tp / (tp + fp)))
print('F1=' + str(tp / (tp + 0.5 * (fp + fn))))
print('ACC=' + str((tp + tn) / (tp + tn + fp + fn)))
