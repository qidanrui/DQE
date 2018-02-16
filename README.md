# DQE
This code is for paper "Outliers Revisited: A Data  ality Explanation"
## File Structure
* src: source code of algorithms and experiments code
* dataset: Dataset source files used in experiments

## Datasets
* Letter dataset: http://sci2s.ugr.es/keel/dataset.php?cod=198
* MAGIC dataset: https://archive.ics.uci.edu/ml/datasets/magic+gamma+telescope
* Restaurant dataset: http://www.cs.utexas.edu/users/ml/riddle/data.html
* GPS dataset: collected by carrying smartphones and walking around campus

## Experiments
### Experiment 4.1
#### 4.1.1
* Run Fig. 4
```
python src/exp/exp_epsilon_wisconsin.py
```

* Run Fig. 5
```
python src/exp/exp_k_wisconsin.py
```
#### 4.1.2
* Run Fig. 6

For different epsilon:
```
python src/exp/exp_classify_epsilon_letter.py
```

For different neighbor k:
```
python src/exp/exp_classify_k_letter.py
```
#### 4.1.3
* Run Fig. 7

For different epsilon:
```
python src/exp/exp_subspace_epsilon.py
```

For different neighbor k:
```
python src/exp/exp_subspace_eta.py
```

#### 4.1.4

* Run Fig. 8

```
python src/exp/exp_size_wisconsin.py
```

* Run Fig. 9

```
python src/exp/exp_attr_wisconsin.py
```

### Experiment 4.2
* Run Fig. 10

```
python src/exp/exp_epsilon_gps.py
```

* Run Fig. 11

```
python src/exp/exp_k_gps.py
```

### Experiment 4.3
#### 4.3.1
* Run Fig. 12

For different epsilon:
```
python src/exp/exp_classify_epsilon_magic.py
```

For different neighbor k:
```
python src/exp/exp_classify_neighbor_k_magic.py
```

* Run Fig. 13

For different epsilon:
```
python src/exp/exp_subspace_avg_attr_epsilon.py
```

For different neighbor k:
```
python src/exp/exp_subspace_avg_attr_k.py
```

#### 4.3.2
* Run Fig. 14

For different epsilon:
```
python src/exp/exp_matching_epsilon.py
```

For different neighbor k:
```
python src/exp/exp_matching_k.py
```


