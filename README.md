# ACM-Research-Coding-Challenge-Fall-2022-Solution
Created for ACM Research Coding Challenge

*To DO*

_Project Questions_
1. Create algorithm for giving car models a certain ranking based on average review score and # of reviews.
-> Assess ranking based on ratings and # of reviews for both buyer and seller categories. Use formula 1 + 4 (1/ 1 + (k)^-ax) to calculate rating reliability, then calculate rating based on average rating + (rating reliability - 50) / 50 separately for buyer and for seller ratings.
-> Compare Buyer rankings to Sellers rankings to better estimate rankings at low # of Buyer reviews.
-> Note that we are not given a number of cars sold, which makes it difficult to accurately consider the usefulness of # of reviews.
2. Compare buyer average rankings to sellers rankings.

_Data Set Challenges_

1. Remove the symbols from the 'price' variable and convert it into an integer. Also remove any rows that have a value 'not priced' OR you can try to impute an appropriate price value based on the make and model of the car.

2. Average buyer ratings and seller ratings, and tally total number of buyer reviews and total number of seller reviews across each of the cars based on their makes, models, and years {year, make, model, used/new}.
