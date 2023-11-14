# Pneumonia Drug Prediction using Logistic Regression
For CS123a Project (Introduction to Bioinformatics) at San Jose State University

Technologies used: Python, PyTorch...

## What is the goal?
The goal of this project is to train a Logistic Regression to identify potential drug molecules that can be used to treat pneumonia. 

### What can this do for us?
Usage of machine learning such as Logistic Regression can help us save time and money in the drug development process.

## Why Logistic Regression?
Logistic Regression is a type of machine learning that is used to predict the probability of a categorical dependent variable (in this case, the potential drug molecule). We are trying to predict the probability of a drug molecule being used to treat pneumonia so as a result, Logistic Regression is perfectly suited for this task. 

### Issues with Logistic Regression...
Potential problems with Logistic Regression is that it is prone to overfitting. This means that the model will be too specific to the training data and will not be able to generalize well to new data. Given that we are using a relatively small dataset, this may be a problem.

## Dataset and other information...
The dataset that will be used in this project was created from the team's aggregation of both drugs proven to work against pneuomonia and drugs that cannot work against pneuomonia (resistant or antiviral drugs). 

We obtain the SMILES information from the ChemSpider database found here: https://www.chemspider.com/

## Process
The dataset is split into 3 parts: training, validation, and testing. As the names entail: the training dataset will be used to train the model, the validation dataset will be used to validate the model, and the testing dataset will be used to test the model.

## Running program
pip install -r requirements.txt
