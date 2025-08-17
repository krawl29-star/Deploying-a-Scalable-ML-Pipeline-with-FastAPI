# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
Created by: Katelynn Rawlings
Creation Date: 8/17/2025
Model: RandomForest Classifier
## Intended Use
The model is used to determine if a person is making over $50K a year based on:
* age
* workclass
* fnlwgt
* education
* education-num
* marital-status
* occupation
* relationship
* race
* sex

## Training Data
80% of the full census dataset was used in the training data

## Evaluation Data
20% of the full census dataset was used in the testing data

## Metrics
_Please include the metrics used and your model's performance on those metrics._
* Precision: 0.7419
* Recall: 0.6384
* F1: 0.6863

## Ethical Considerations

When considering salary, there are many factors that cannot be measured. This could include things like if the person were disabled, or otherwise incompacitated, the area that they live in, years that they've been working, etc. Our data includes a wide variety of factors to measure, but does not include all real world factors that could contribute to someones salary.

## Caveats and Recommendations

Our dataset is an extration from the 1994 Census database and is over 20 years old. 20 years ago, salaries where lower than they are today. Having more up to date data for evaluation would give us a better view if someone was making over 50K today.

When reviewing the data, the data did not have error that requrired a new cleaned data file as it was already in an optimal state.
