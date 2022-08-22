# ACM-Research-Coding-Challenge-Fall-2022-Solution
Created for ACM Research Coding Challenge

*To DO*
_Project Questions_
1. Create algorithm for giving car models a certain ranking based on average review score and # of reviews.
-> Split data between Used and New.
-> Compare Buyer rankings to Sellers rankings to better estimate rankings at low # of Buyer reviews.
-> Note that we are not given a number of cars sold, which makes it difficult to accurately consider the usefulness of # of reviews.
2. Compare buyer average rankings to sellers rankings.

_Data Set Challenges_

1. Remove the symbols from the 'price' variable and convert it into an integer. Also remove any rows that have a value 'not priced' OR you can try to impute an appropriate price value based on the make and model of the car.

2. In the 'New/Used' column there are many different types of 'certified' values. Change all these to be displayed as 'Certified'. (Aggregate all the different make-specific certified values into one certified category)

3. Remove rows from the data where the value for 'drivetrain' is '-' . These were most likely cases where the seller did not input the drivetrain information. (You can also impute this data if you feel comfortable doing so).

4. Create dummy variables for the appropriate categorical variables so that they can be used for predictive modeling

5. Create a regression model that predicts a car's price OR a classification model that predicts a car's drivetrain
