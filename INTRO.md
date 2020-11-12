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

