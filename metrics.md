## Movie Genre Classification Model Scores

<details>
  <summary><strong>Model: Balanced Random Forest</strong></summary>

  ### Classification Report:
```
features    precision  recall  f1-score   support
```
```
action        0.16      0.13      0.14       263
adult         0.12      0.61      0.21       112
adventure     0.12      0.14      0.13       139
animation     0.08      0.34      0.14       104
biography     0.01      0.03      0.01        61
comedy        0.36      0.15      0.22      1443
crime         0.09      0.36      0.15       107
documentary   0.79      0.30      0.44      2659
drama         0.54      0.09      0.16      2697
family        0.05      0.08      0.06       150
fantasy       0.04      0.19      0.07        74
game-show     0.13      0.88      0.23        40
history       0.03      0.24      0.06        45
horror        0.38      0.36      0.37       431
music         0.21      0.69      0.32       144
musical       0.05      0.30      0.08        50
mystery       0.07      0.36      0.12        56
news          0.04      0.35      0.07        34
reality-tv    0.12      0.11      0.12       192
romance       0.06      0.38      0.11       151
sci-fi        0.15      0.41      0.22       143
short         0.29      0.12      0.17      1045
sport         0.21      0.69      0.32        93
talk-show     0.10      0.48      0.16        81
thriller      0.13      0.10      0.11       309
war           0.03      0.65      0.05        20
western       0.38      0.82      0.52       200

accuracy                           0.22     10843
macro avg      0.18      0.35      0.18     10843
weighted avg   0.45      0.22      0.25     10843
```

**Accuracy Score:** 0.2231
</details>

<details>
<summary><strong>Model: Logistic Regression</strong></summary>

### Classification Report:
```
features    precision  recall  f1-score   support
```
```
action        0.52      0.27      0.36      1314
adult         0.63      0.20      0.30       590
adventure     0.68      0.17      0.27       775
animation     0.53      0.04      0.08       498
biography     0.00      0.00      0.00       264
comedy        0.54      0.59      0.56      7446
crime         0.39      0.03      0.05       505
documentary   0.66      0.85      0.74     13096
drama         0.53      0.79      0.64     13612
family        0.50      0.07      0.12       783
fantasy       0.67      0.01      0.02       322
game-show     0.93      0.48      0.63       193
history       0.00      0.00      0.00       243
horror        0.66      0.58      0.62      2204
music         0.63      0.42      0.50       731
musical       0.00      0.00      0.00       276
mystery       0.20      0.00      0.01       318
news          0.75      0.03      0.06       181
reality-tv    0.50      0.15      0.23       883
romance       0.36      0.01      0.02       672
sci-fi        0.59      0.21      0.31       646
short         0.49      0.29      0.37      5072
sport         0.74      0.21      0.32       431
talk-show     0.60      0.13      0.22       391
thriller      0.36      0.11      0.17      1590
war           1.00      0.01      0.02       132
western       0.92      0.70      0.79      1032

accuracy                           0.58     54200
macro avg      0.53      0.24      0.27     54200
weighted avg   0.56      0.58      0.54     54200
```

**Accuracy Score:** 0.5811
</details>

<details>
<summary><strong>Model: SVM</strong></summary>

### Classification Report:
```
features    precision  recall  f1-score   support
```
```
action        0.55      0.21      0.30      1314
adult         0.68      0.18      0.29       590
adventure     0.72      0.16      0.26       775
animation     0.41      0.01      0.03       498
biography     0.00      0.00      0.00       264
comedy        0.54      0.56      0.55      7446
crime         0.45      0.01      0.02       505
documentary   0.64      0.86      0.74     13096
drama         0.50      0.82      0.62     13612
family        0.56      0.04      0.07       783
fantasy       1.00      0.00      0.01       322
game-show     0.90      0.54      0.68       193
history       0.00      0.00      0.00       243
horror        0.69      0.55      0.61      2204
music         0.72      0.32      0.45       731
musical       0.00      0.00      0.00       276
mystery       0.00      0.00      0.00       318
news          0.60      0.02      0.03       181
reality-tv    0.54      0.08      0.13       883
romance       0.00      0.00      0.00       672
sci-fi        0.58      0.17      0.26       646
short         0.60      0.24      0.35      5072
sport         0.90      0.14      0.25       431
talk-show     0.72      0.11      0.19       391
thriller      0.40      0.07      0.11      1590
war           1.00      0.02      0.04       132
western       0.92      0.69      0.79      1032

accuracy                           0.57     54200
macro avg      0.54      0.22      0.25     54200
weighted avg   0.57      0.57      0.52     54200
```

**Accuracy Score:** 0.5734
</details>
