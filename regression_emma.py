'''
This is a program that charts the average of the Southern California population
growth from the years 2010-2018, made by Emma Ruccio. The population is presented
in thousands, while the years are presented as just the last two numbers (i.e.
10 instead of 2010).
Source: https://wolfstreet.com/2019/04/19/los-angeles-population-falls-san-francisco-bay-area-rises-least-since-2010-as-california-population-growth-turns-to-crawl/.
02/24/20
'''

import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
   #number of observations
    n = np.size(x);

    #finding the mean of x and y vector
    mean_x, mean_y = np.mean(x), np.mean(y)

    #calculating the least squares
    SS_xy = np.sum(y*x) - n * mean_y * mean_x
    SS_xx = np.sum(x*x) - n * mean_x * mean_x

    #regression coefficents
    slope = SS_xy/SS_xx
    yintercept = mean_y - slope * mean_x

    #return m and b
    return(slope, yintercept)

def plot_regression_line(x, y, b):
    #plotting the actual points as a scatter plot
    plt.scatter(x, y, color = "m", marker = "o", s = 30)

    #predicted response vector
    y_pred = b[0] + b[1] + x

    #plotting the regression plot_regression_line
    plt.plot(x, y_pred, color = "g")

    #putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    #function to show plotting
    plt.show()

def main():
    #observations
    x = np.array([10, 11, 12, 13, 14, 15, 16, 17, 18])
    y = np.array([39, 182, 179, 167, 170, 160, 122, 80, 62])

    # estimated coefficients
    b = estimate_coef(x, y)
    print("Estimated coefficients: \n b = {} \ \n m = {}".format(b[0], b[1]))

    #plotting regression line
    plot_regression_line(x, y, b)

#make script importable and executables
if __name__ == "__main__":
    main()
