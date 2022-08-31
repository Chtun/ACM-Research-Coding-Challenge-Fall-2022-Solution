# ACM-Research-Coding-Challenge-Fall-2022-Solution
Created for ACM Research Coding Challenge

In this project, I sought to calculate a ranking score (from 0 to 5) for each car by their make, model, and year that accounts for both the average review scores and the number of reviews. This is done by subtracting up to a single point from the average review scores depending on how low the rating reliability was (more than 100 ratings were classified as 100% reliable, and values between 1 and 100 reviews were classified as values between 0 and 100% reliable based on a sigmoid function). Then, I used those ranking scores to determine which of the car brands had the highest and most reliable reviews, which is stored in the 'best_rankings.csv' file. Finally, I used those ranking scores to determine which of the dealers sell the best cars.

Upon completion of this project, I was required to work through several data set and coding challenges, which are listed below.


_Project Questions_
1. Create algorithm for giving car models a certain ranking based on average review score and # of reviews.

-> Assess ranking based on ratings and # of reviews for both buyer and seller categories. Use formula 100 * (1/ 1 + (k)^-ax) (sigmoid function) to calculate rating reliability, then calculate rating based on average rating + (rating reliability - 100) / 100 separately for buyer and for seller ratings.

-> Compare Buyer rankings to Sellers rankings to better estimate rankings at low # of Buyer reviews.

-> Note that we are not given a number of cars sold, which makes it more difficult to accurately consider the usefulness of # of reviews.

2. Compare buyer average rankings to sellers rankings.

3. Use final rankings of each car to find which dealers sell the best cars.




_Data Set and Coding Challenges_

1. Remove the symbols from the 'price' variable and convert it into an integer. Also remove any rows that have a value 'not priced' OR you can try to impute an appropriate price value based on the make and model of the car.

2. Average buyer ratings and seller ratings, and tally total number of buyer reviews and total number of seller reviews across each of the cars based on their makes, models, and years {year, make, model, used/new}.



_Files_

Outside of the code, I slightly modified the 'cars_raw.csv' file because I needed to get rid of commas that appeared in the 'dealer name' column, which I replaced with semicolons. The rest of the csv files were generated from the python script.

cars_price.csv: CSV file of the average price of cars by year, make, model, and new/used

cars_info.csv: CSV file of the average buyer rating, number of buyer reviews, average seller rating, number of seller reviews, adjusted buyer ranking, adjusted sellers ranking, buyer rating reliability, seller rating reliability, and final ranking score of each car by year, make, and model.

best_rankings.csv: CSV file of ranking of best car brands by average final ranking across all their car models and years.

dealer_rankings.csv: CSV file of ranking of best dealerships by average final ranking across all their sales of car by make, model, and year.
