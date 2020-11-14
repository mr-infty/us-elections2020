# Benford's Law and the 2020 General Elections

## Goal

The goal of the following note is to determine whether and to what extent the (unofficial) election results of the 2020 general election satisfy (the strong version of) *Benford's Law*.

## Method

Unofficial election results are obtained from official sources for various states and counties, and are tested using the Kolmogorov-Smirnov test (with $\alpha = 0.01$) whether they satisfy strong version of Benford's Law.

## Background on Benford's Law and Fraud Detection

*Benford's law* is the counter-intuitive notion that the leading digits of "organic" numbers tend *not* to be uniformly distributed, but rather according to *Benford's distribution*:

$$P(d) = \log_{10}(d+1) - \log_{10}(d).$$

This distribution of digits follows immediately from the *strong* version of Benford's law, which states that the fractional part $\log_{10}(X) \mod 1$ of the logarithm of an "organic" random variable $X$ is uniformly distriuted.

What exactly "organic" should mean here is the non-trivial part of Benford's Law, which is yet to be made precise by someone. However, one should roughly think of things like electricity bills, street addresses, stock prices and the like.

The whole point of Benford's Law (from a practical viewpoint) is not which numbers satisfy but rather which numbers don't satisfy it. For instance, uniformly distributed (i.e. "random") numbers do not satisfy Benford's law, which means---given Benford's law---that most numbers aren't as random as you think they are.

Most importantly, the numbers people come up with when they have to produce some tend not to satisfy Benford's law, which makes it possible to *detect fraud* using statistical methods.

# Results
## Alabama
The test results for the state-wide election results (per county) of Alabama are as follows.

The election results for Biden **seem to satisfy** Benford's law up to an error of 1%:

- dmax: 0.076720
- dcrit: 0.165919
- N: 67

![Empirical distribution of fractional part of decimal logarithm of votes for Alabama (D) (black line) and uniform distribution (gray line)](graphics/Alabama_D.pdf)

The election results for Trump **seem to satisfy** Benford's law up to an error of 1%:

- dmax: 0.069288
- dcrit: 0.165919
- N: 67

![Empirical distribution of fractional part of decimal logarithm of votes for Alabama (R) (black line) and uniform distribution (gray line)](graphics/Alabama_R.pdf)

## Alaska
The test results for the state-wide election results (per precinct) of Alaska are as follows.

The election results for Biden **violate** Benford's law with 99% certainty:

- dmax: 0.129968
- dcrit: 0.064893
- N: 438

![Empirical distribution of fractional part of decimal logarithm of votes for Alaska (D) (black line) and uniform distribution (gray line)](graphics/Alaska_D.pdf)

The election results for Trump **violate** Benford's law with 99% certainty:

- dmax: 0.080107
- dcrit: 0.064819
- N: 439

![Empirical distribution of fractional part of decimal logarithm of votes for Alaska (R) (black line) and uniform distribution (gray line)](graphics/Alaska_R.pdf)

## Arizona
The test results for the state-wide election results (per county) of Arizona are as follows.

The election results for Biden **seem to satisfy** Benford's law up to an error of 1%:

- dmax: 0.171921
- dcrit: 0.338000
- N: 15

![Empirical distribution of fractional part of decimal logarithm of votes for Arizona (D) (black line) and uniform distribution (gray line)](graphics/Arizona_D.pdf)

The election results for Trump **seem to satisfy** Benford's law up to an error of 1%:

- dmax: 0.149234
- dcrit: 0.338000
- N: 15

![Empirical distribution of fractional part of decimal logarithm of votes for Arizona (R) (black line) and uniform distribution (gray line)](graphics/Arizona_R.pdf)

### Maricopa
The test results for the county-wide election results (per precinct) of Maricopa County, Arizona are as follows.

The election results for Biden **violate** Benford's law with 99% certainty:

- dmax: 0.228547
- dcrit: 0.049857
- N: 742

![Empirical distribution of fractional part of decimal logarithm of votes for Maricopa,Arizona (D) (black line) and uniform distribution (gray line)](graphics/Maricopa,Arizona_D.pdf)

The election results for Trump **violate** Benford's law with 99% certainty:

- dmax: 0.100022
- dcrit: 0.049857
- N: 742

![Empirical distribution of fractional part of decimal logarithm of votes for Maricopa,Arizona (R) (black line) and uniform distribution (gray line)](graphics/Maricopa,Arizona_R.pdf)

### Pima
The test results for the county-wide election results (per precinct) of Pima County, Arizona are as follows.

The election results for Biden **violate** Benford's law with 99% certainty:

- dmax: 0.112712
- dcrit: 0.061104
- N: 494

![Empirical distribution of fractional part of decimal logarithm of votes for Pima,Arizona (D) (black line) and uniform distribution (gray line)](graphics/Pima,Arizona_D.pdf)

The election results for Trump **seem to satisfy** Benford's law up to an error of 1%:

- dmax: 0.055297
- dcrit: 0.061166
- N: 493

![Empirical distribution of fractional part of decimal logarithm of votes for Pima,Arizona (R) (black line) and uniform distribution (gray line)](graphics/Pima,Arizona_R.pdf)

## Arkansas
The test results for the state-wide election results (per county) of Arkansas are as follows.

The election results for Biden **seem to satisfy** Benford's law up to an error of 1%:

- dmax: 0.049463
- dcrit: 0.088405
- N: 236

![Empirical distribution of fractional part of decimal logarithm of votes for Arkansas (D) (black line) and uniform distribution (gray line)](graphics/Arkansas_D.pdf)

The election results for Trump **violate** Benford's law with 99% certainty:

- dmax: 0.095244
- dcrit: 0.088218
- N: 237

![Empirical distribution of fractional part of decimal logarithm of votes for Arkansas (R) (black line) and uniform distribution (gray line)](graphics/Arkansas_R.pdf)

## California
The test results for the state-wide election results (per county) of California are as follows.

The election results for Biden **seem to satisfy** Benford's law up to an error of 1%:

- dmax: 0.115905
- dcrit: 0.178327
- N: 58

![Empirical distribution of fractional part of decimal logarithm of votes for California (D) (black line) and uniform distribution (gray line)](graphics/California_D.pdf)

The election results for Trump **seem to satisfy** Benford's law up to an error of 1%:

- dmax: 0.092923
- dcrit: 0.178327
- N: 58

![Empirical distribution of fractional part of decimal logarithm of votes for California (R) (black line) and uniform distribution (gray line)](graphics/California_R.pdf)

## Florida
The test results for the state-wide election results (per county) of Florida are as follows.

The election results for Biden **seem to satisfy** Benford's law up to an error of 1%:

- dmax: 0.064655
- dcrit: 0.165919
- N: 67

![Empirical distribution of fractional part of decimal logarithm of votes for Florida (D) (black line) and uniform distribution (gray line)](graphics/Florida_D.pdf)

The election results for Trump **seem to satisfy** Benford's law up to an error of 1%:

- dmax: 0.140142
- dcrit: 0.165919
- N: 67

![Empirical distribution of fractional part of decimal logarithm of votes for Florida (R) (black line) and uniform distribution (gray line)](graphics/Florida_R.pdf)

### Martin
The test results for the county-wide election results (per precinct) of Martin County, Florida are as follows.

The election results for Biden **seem to satisfy** Benford's law up to an error of 1%:

- dmax: 0.127541
- dcrit: 0.148181
- N: 84

![Empirical distribution of fractional part of decimal logarithm of votes for Martin,Florida (D) (black line) and uniform distribution (gray line)](graphics/Martin,Florida_D.pdf)

The election results for Trump **seem to satisfy** Benford's law up to an error of 1%:

- dmax: 0.093213
- dcrit: 0.148181
- N: 84

![Empirical distribution of fractional part of decimal logarithm of votes for Martin,Florida (R) (black line) and uniform distribution (gray line)](graphics/Martin,Florida_R.pdf)

### Miami-Dade
The test results for the county-wide election results (per precinct) of Miami-Dade County, Florida are as follows.

The election results for Biden **violate** Benford's law with 99% certainty:

- dmax: 0.070467
- dcrit: 0.047485
- N: 818

![Empirical distribution of fractional part of decimal logarithm of votes for Miami-Dade,Florida (D) (black line) and uniform distribution (gray line)](graphics/Miami-Dade,Florida_D.pdf)

The election results for Trump **violate** Benford's law with 99% certainty:

- dmax: 0.096724
- dcrit: 0.047514
- N: 817

![Empirical distribution of fractional part of decimal logarithm of votes for Miami-Dade,Florida (R) (black line) and uniform distribution (gray line)](graphics/Miami-Dade,Florida_R.pdf)

### Osceola
The test results for the county-wide election results (per precinct) of Osceola County, Florida are as follows.

The election results for Biden **seem to satisfy** Benford's law up to an error of 1%:

- dmax: 0.072245
- dcrit: 0.089942
- N: 228

![Empirical distribution of fractional part of decimal logarithm of votes for Osceola,Florida (D) (black line) and uniform distribution (gray line)](graphics/Osceola,Florida_D.pdf)

The election results for Trump **seem to satisfy** Benford's law up to an error of 1%:

- dmax: 0.061158
- dcrit: 0.088405
- N: 236

![Empirical distribution of fractional part of decimal logarithm of votes for Osceola,Florida (R) (black line) and uniform distribution (gray line)](graphics/Osceola,Florida_R.pdf)

## Georgia
The test results for the state-wide election results (per county) of Georgia are as follows.

The election results for Biden **seem to satisfy** Benford's law up to an error of 1%:

- dmax: 0.050332
- dcrit: 0.056392
- N: 580

![Empirical distribution of fractional part of decimal logarithm of votes for Georgia (D) (black line) and uniform distribution (gray line)](graphics/Georgia_D.pdf)

The election results for Trump **seem to satisfy** Benford's law up to an error of 1%:

- dmax: 0.035176
- dcrit: 0.055583
- N: 597

![Empirical distribution of fractional part of decimal logarithm of votes for Georgia (R) (black line) and uniform distribution (gray line)](graphics/Georgia_R.pdf)

### Cobb
The test results for the county-wide election results (per precinct) of Cobb County, Georgia are as follows.

The election results for Biden **violate** Benford's law with 99% certainty:

- dmax: 0.281565
- dcrit: 0.112784
- N: 145

![Empirical distribution of fractional part of decimal logarithm of votes for Cobb,Georgia (D) (black line) and uniform distribution (gray line)](graphics/Cobb,Georgia_D.pdf)

The election results for Trump **violate** Benford's law with 99% certainty:

- dmax: 0.253272
- dcrit: 0.112784
- N: 145

![Empirical distribution of fractional part of decimal logarithm of votes for Cobb,Georgia (R) (black line) and uniform distribution (gray line)](graphics/Cobb,Georgia_R.pdf)

### DeKalb
The test results for the county-wide election results (per precinct) of DeKalb County, Georgia are as follows.

The election results for Biden **violate** Benford's law with 99% certainty:

- dmax: 0.409322
- dcrit: 0.098269
- N: 191

![Empirical distribution of fractional part of decimal logarithm of votes for DeKalb,Georgia (D) (black line) and uniform distribution (gray line)](graphics/DeKalb,Georgia_D.pdf)

The election results for Trump **violate** Benford's law with 99% certainty:

- dmax: 0.141574
- dcrit: 0.098269
- N: 191

![Empirical distribution of fractional part of decimal logarithm of votes for DeKalb,Georgia (R) (black line) and uniform distribution (gray line)](graphics/DeKalb,Georgia_R.pdf)

### Fulton
The test results for the county-wide election results (per precinct) of Fulton County, Georgia are as follows.

The election results for Biden **violate** Benford's law with 99% certainty:

- dmax: 0.108344
- dcrit: 0.069669
- N: 380

![Empirical distribution of fractional part of decimal logarithm of votes for Fulton,Georgia (D) (black line) and uniform distribution (gray line)](graphics/Fulton,Georgia_D.pdf)

The election results for Trump **seem to satisfy** Benford's law up to an error of 1%:

- dmax: 0.043403
- dcrit: 0.069946
- N: 377

![Empirical distribution of fractional part of decimal logarithm of votes for Fulton,Georgia (R) (black line) and uniform distribution (gray line)](graphics/Fulton,Georgia_R.pdf)

### Gwinnett
The test results for the county-wide election results (per precinct) of Gwinnett County, Georgia are as follows.

The election results for Biden **violate** Benford's law with 99% certainty:

- dmax: 0.323849
- dcrit: 0.108735
- N: 156

![Empirical distribution of fractional part of decimal logarithm of votes for Gwinnett,Georgia (D) (black line) and uniform distribution (gray line)](graphics/Gwinnett,Georgia_D.pdf)

The election results for Trump **violate** Benford's law with 99% certainty:

- dmax: 0.146186
- dcrit: 0.108735
- N: 156

![Empirical distribution of fractional part of decimal logarithm of votes for Gwinnett,Georgia (R) (black line) and uniform distribution (gray line)](graphics/Gwinnett,Georgia_R.pdf)

