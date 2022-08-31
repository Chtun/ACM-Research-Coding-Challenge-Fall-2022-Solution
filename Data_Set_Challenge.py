# Create 2D array 'cars_price' to store price of vehicles across different models and different stores
def FormatCarPrice(cars, index):

    for i in range(1, len(cars)):
        # Determine whether value under 'Price' column for cars are digits
        if (cars[i][index][2:len(cars[i][index])].isdigit()):
            cars[i][index] = int(cars[i][index][2:len(cars[i][index])]) * 1000 + int(cars[i][index + 1][0:len(cars[i][index]) - 1])
            del cars[i][index + 1]
        else:
            cars[i][index] = 'Not Priced'

    # Create 'cars_price' and set values
    cars_price = [['Year','Make', 'Model', 'Used/New', 'Price']]

    for i in range(1, len(cars)):
        if (cars[i][4] != 'Not Priced'):
            cars_price.append([cars[i][0], cars[i][1], cars[i][2], cars[i][3], cars[i][4]])



    return cars_price

    

# Create 2D array 'cars_info' to store buyer and seller average rating, and total # of buyer and seller reviews for each car with a different make, model, and year
def FormatCarsInfo(cars):
    
    cars_info = [['Year','Make', 'Model', 'average buyer rating', '# of buyers', 'average seller rating', '# of sellers', '', '', 'adjusted buyer ranking', 'adjusted sellers ranking', '', 'buyer rating reliability', 'seller rating reliability', '', 'final ranking']]

    indices_remove = []
   
    # Iterate through cars  in 'cars' array to calculate average buyer and seller ratings, adding up any additional raitings found later on and storing the additional cars' indices to be removed later.
    for i in range(1, len(cars)):

        cars_info.append([cars[i][0], cars[i][1], cars[i][2]])
        
        
        avr_buyer_rating = float(cars[i][5]) * int(cars[i][6])
        avr_sellers_rating = float(cars[i][9]) * int(cars[i][10])
        num_buyers = int(cars[i][6])
        
        num_sellers = int(cars[i][10])


        for j in range (i + 1, len(cars)):
            if cars[j][0] == cars_info[i][0] and cars[j][1] == cars_info[i][1] and cars[j][2] == cars_info[i][2]:
                num_buyers += int(cars[j][6])
                num_sellers += int(cars[j][10])
                avr_buyer_rating += float(cars[j][5]) * int(cars[j][6])
                avr_sellers_rating += float(cars[j][9]) * int(cars[j][10])
                indices_remove.append(j)

        avr_buyer_rating = avr_buyer_rating / num_buyers
        
        avr_sellers_rating = avr_sellers_rating / num_sellers


        # Round average ratings to 2 decimal places
        avr_buyer_rating = float("{0:.2f}".format(avr_buyer_rating))
        avr_sellers_rating = float("{0:.2f}".format(avr_sellers_rating))


        # Calculate adjusted buyer rating, taking into account number of buyer reviews based on function 100 * (1/ 1 + (k)^-ax)
        buyer_rating_reliability = 100 * (1 / (1 + pow(1.12 , -(num_buyers - 50))))
        adjusted_buyer_ranking =  avr_buyer_rating  + (buyer_rating_reliability - 100) / 100
        
        # Calculate adjusted seller rating, taking into account number of seller reviews based on function 100 * (1/ 1 + (k)^-ax)
        seller_rating_reliability = 100 * (1 / (1 + pow(1.25 , -(num_sellers - 25))))
        adjusted_seller_ranking = avr_sellers_rating + (seller_rating_reliability - 100) / 100

        # Calculate overall ranking based on both buyer and seller ratings, taking into account rating reliability for each
        final_ranking = (adjusted_buyer_ranking * (buyer_rating_reliability) / (buyer_rating_reliability + seller_rating_reliability)) + (adjusted_seller_ranking * (seller_rating_reliability) / (buyer_rating_reliability + seller_rating_reliability))

        # Round rankings and rating reliability to 2 decimal places
        adjusted_buyer_ranking = float("{0:.2f}".format(adjusted_buyer_ranking))
        adjusted_seller_ranking = float("{0:.2f}".format(adjusted_seller_ranking))
        buyer_rating_reliability = float("{0:.2f}".format(buyer_rating_reliability))
        seller_rating_reliability = float("{0:.2f}".format(seller_rating_reliability))
        seller_rating_reliability = float("{0:.2f}".format(seller_rating_reliability))
        final_ranking = float("{0:.2f}".format(final_ranking))

        cars_info[i].extend((avr_buyer_rating, num_buyers, avr_sellers_rating, num_sellers, '', '', adjusted_buyer_ranking, adjusted_seller_ranking, '', buyer_rating_reliability, seller_rating_reliability, '', final_ranking))
        
    # Remove duplicate cars that have the same makes, models, and years
    indices = [*set(indices_remove)]
    for k in reversed(indices):
            del cars_info[k]
    
    return cars_info

def OutputCSV(CSV_Table, name):
    with open(name + '.csv', 'w', newline='') as csvfile:
        cars_table = csv.writer(csvfile, delimiter=',',
                                quoting=csv.QUOTE_NONE, escapechar='\\')
        for i in range(len(CSV_Table)):
            cars_table.writerow(CSV_Table[i])

# Find the best ranked cars by brand and the top 10 cars to buy based on final rankings
def FindBestRankings(cars_info):
    
    car_brand = [['Brand', 'Calculate Score', 'Info']]
    best_rankings = np.array([['Brand', 'Average Final Rankings', 'Number of Cars rated']])
    
    # Iterate through cars_info and add new car brands found to car brand. Then, add number of reviews and add up total review scores for all cars in a brand
    for i in range(1, len(cars_info)):
        isInCarBrand = False
        for j in range(1, len(car_brand)):
            if cars_info[i][1] == car_brand[j][0]:
                isInCarBrand = True
            
        if isInCarBrand == False:
            car_brand.append([cars_info[i][1], 0, 0])
            index = (FindIndexIn2D(car_brand, cars_info[i][1]))[0]
            car_brand[index][1] = (cars_info[i][15]) * (cars_info[i][4] + cars_info[i][6])
            car_brand[index][2] = cars_info[i][4] + cars_info[i][6]
        else:
            index = (FindIndexIn2D(car_brand, cars_info[i][1]))[0]
            car_brand[index][1] += cars_info[i][15] * (cars_info[i][4] + cars_info[i][6])
            car_brand[index][2] += cars_info[i][4] + cars_info[i][6]

    # Calculate average final ranking based on -> summation of total review scores / number of reviews
    for i in range(1, len(car_brand)):
        car_brand[i][1] = car_brand[i][1] / car_brand[i][2]
        car_brand[i][1] = float("{0:.2f}".format(car_brand[i][1]))
        best_rankings = np.vstack([best_rankings, [car_brand[i][0], car_brand[i][1], car_brand[i][2]]])
    
    # Sort 'best_rankings' array by top car brand values
    best_rankings = best_rankings[best_rankings[:, 1].argsort()[::-1][:len(best_rankings)]]

    return best_rankings

# Find index of element in v
def FindIndexIn2D(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return [i, x.index(v)]


def main():

    cars = []

    # Create 2D array 'cars' from data table in 'cars_raw.csv' file
    with open('cars_raw.csv', newline='') as csvfile:
        
        
        cars_table = csv.reader(csvfile, delimiter=',', quotechar='|')
        
        for row in cars_table:
            cars.append(row)

    # Find index with 'Price', create cars_price, format cars_price
    index = cars[0].index('Price')
    cars_price = FormatCarPrice(cars, index)
    print("Car price formatted.")

    # Create cars_info and format cars_info
    cars_info = FormatCarsInfo(cars)
    print("Cars info formatted.")

    # Find best rankings of cars by brand, the top 20 cars, and taking into account both average rating and rating reliability
    best_rankings = FindBestRankings(cars_info)
    print("Best rankings formatted.")

    # Create output .csv file for 'cars_price'
    OutputCSV(cars_price, "cars_price")    
    OutputCSV(cars_info, "cars_info")
    OutputCSV(best_rankings, "best_rankings")
    



if __name__ == '__main__':
    import csv
    import numpy as np
    main()