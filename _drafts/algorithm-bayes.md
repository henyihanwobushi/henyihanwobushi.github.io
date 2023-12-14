---
layout: post
title: "[Algorithm] Bayes"
---

Bayes is a probabilistic algorithm that uses Bayes' theorem to solve the problem of determining the likelihood of an event occurring based on prior knowledge of conditions that might be related to the event.

Bayes' theorem is stated as:

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

where:

- $P(A|B)$ is the probability of event A given event B.
- $P(B|A)$ is the probability of event B given event A.
- $P(A)$ is the probability of event A.
- $P(B)$ is the probability of event B.

The hello world example is to find out if a e-mail is spam or not. The email is spam if it contains the word "free" and the word "money" in the body of the email. The word "free" is more likely to appear in spam emails than non-spam emails. The word "money" is more likely to appear in spam emails than non-spam emails.

The probability of an email being spam is calculated as follows:

$$
P(spam|free, money) = \frac{P(free, money|spam)P(spam)}{P(free, money)}
$$

## Step 1: Calculate the Prior Probability

The prior probability of an email being spam is calculated as follows:

$$
P(spam) = \frac{1}{1000}
$$

This means that the probability of an email being spam is 0.001.

## Step 2: Calculate the Probability of the Word "Free" Appearing in a Spam Email

The probability of the word "free" appearing in a spam email is calculated as follows:

$$
P(free|spam) = \frac{3}{5}
$$

This means that the probability of the word "free" appearing in a spam email is 0.6.

## Step 3: Calculate the Probability of the Word "Money" Appearing in a Spam Email

The probability of the word "money" appearing in a spam email is calculated as follows:

$$
P(money|spam) = \frac{2}{5}
$$

This means that the probability of the word "money" appearing in a spam email is 0.4.

## Step 4: Calculate the Likelihood of the Email being Spam

The likelihood of the email being spam is calculated as follows:

$$
P(free, money|spam) = \frac{3}{5} \times \frac{2}{5} \times \frac{1}{1000} = 0.00003
$$

This means that the likelihood of the email being spam is 0.00003.

## Step 5: Calculate the Posterior Probability

The posterior probability of an email being spam is calculated as follows:

$$
P(spam|free, money) = \frac{P(free, money|spam)P(spam)}{P(free, money)} = \frac{0.00003 \times 0.001}{0.00003 \times 0.001 + 0.00003 \times 0.999} = 0.00003
$$

This means that the posterior probability of an email being spam is 0.00003.

This is a very simple example of how Bayes' theorem can be used to solve a problem. In practice, you would use more complex models and data to calculate the posterior probability.

# Bayes Classification with Continuous Variables

Bayes classification is a type of classification where the class variable is continuous. It is a probabilistic approach to classify data into different categories.

Bayes' theorem can be used to calculate the posterior probability of a continuous variable.

The Bayes classification algorithm is as follows:

1. Define the prior probability distribution of the class variable.
2. Define the likelihood function of the class variable given the input variables.
3. Define the prior probability distribution of the input variables.
4. Calculate the posterior probability distribution of the class variable given the input variables.
5. Classify the input variables into the category with the highest posterior probability.

## Step 1: Define the Prior Probability Distribution of the Class Variable

The prior probability distribution of the class variable is defined as follows:

$$
P(c) = \frac{1}{K}
$$

where $K$ is the number of classes.

## Step 2: Define the Likelihood Function of the Class Variable Given the Input Variables

The likelihood function of the class variable given the input variables is defined as follows:

$$
P(c|x) = \frac{P(x|c)P(c)}{P(x)}
$$

where $P(x|c)$ is the likelihood of the input variables given the class variable, $P(c)$ is the prior probability of the class variable, and $P(x)$ is the marginal probability of the input variables.

## Step 3: Define the Prior Probability Distribution of the Input Variables

The prior probability distribution of the input variables is defined as follows:

$$
P(x) = \frac{1}{N}
$$

where $N$ is the number of input variables.

## Step 4: Calculate the Posterior Probability Distribution of the Class Variable Given the Input Variables

The posterior probability distribution of the class variable given the input variables is calculated as follows:

$$
P(c|x) = \frac{P(x|c)P(c)}{P(x|c)P(c) + P(x|\bar{c})P(\bar{c})}
$$

where $P(x|\bar{c})$ is the prior probability of the class variable not equal to the class variable, and $P(\bar{c})$ is the marginal probability of the class variable not equal to the class variable.

## Step 5: Classify the Input Variables into the Category with the Highest Posterior Probability

The category with the highest posterior probability is selected as follows:

$$
c_{max} = \arg\max_{c} P(c|x)
$$

This means that the category with the highest posterior probability is the class variable with the highest posterior probability.