# Homework 3: Z-Score Python Script (Group Homework)

#################
#  SAMPLE DATA  #
#################
# First data set: a list of positive integers (not a normal distribution)
population1 = [14, 28, 96, 97, 21, 29, 29, 4, 58, 
               42, 25, 97, 49, 33, 75, 53, 14, 53, 
               45, 87, 75, 66, 62, 55, 57, 44, 44, 
               94, 19, 96, 12, 59, 86, 88, 61, 68, 
               37, 64, 19, 46, 68, 98, 19, 54, 65, 
               30, 1, 82, 76, 3]

# Second data set: a list of negative and positive integers (normal distribution)
population2 = [-16, 10, -15, -6, -5, -20, -11, 9, -9,
               -7, 5, -14, 6, -10, -22, -19, 21, 11, 
               -18, -13, -24, -21, 14, 19, 20, 13, 16, 
               8, 4, 3, 18, 22, 17, 7, -12, -3, 
               23, -8, 2, -2, -4, 1, 12, -25, -1,
               15, 0, -23, -17, 24]

# Third data set: a list of positive integers (normal distribution)
population3 = [125, 475, 275, 550, 350, 325, 575, 
               25, 225, 150, 425, 75, 175, 650, 
               600, 625, 675, 250, 100, 0, 375, 
               500, 400, 450, 300, 525, 50, 200]

#################
#  FUNCTIONS    #
#################

def mean(data_set):
    return sum(data_set) / len(data_set)

def stdev(data_set, avg):
    variance = sum([(integer - avg) ** 2 for integer in data_set]) / len(data_set)
    return variance ** 0.5
	
def least(data_set):
    return min(data_set)
	
def greatest(data_set):
    return max(data_set)

def test_z_score_function():
    pop1_avg = mean(population1)
    pop1_sd = stdev(population1, pop1_avg)
    
    mean_z_score_p1 = z_score(pop1_avg, pop1_avg, pop1_sd)
    
    pop2_greatest = greatest(population2)
    pop2_avg = mean(population2)
    pop2_sd = stdev(population2, pop2_avg)
    
    greatest_z_score_p2 = z_score(pop2_greatest, pop2_avg, pop2_sd)
    
    print("The z-score of the mean of population1 is", mean_z_score_p1)
    print("The z-score of the greatest value of population2 is", greatest_z_score_p2)

#######################################################

def z_score(x, mu, sigma):
    # Participating group member names: [Johnathan Rast, Armani Pittman, Jennifer Niga]
    return (x - mu) / sigma

#########################
#  TESTING YOUR CODE    #
#########################

def run_automated_tests():
    # List of test cases in the form (x, mu, sigma, expected_result)
    test_cases = [
        (14, mean(population1), stdev(population1, mean(population1)), (14 - mean(population1)) / stdev(population1, mean(population1))),
        (10, mean(population2), stdev(population2, mean(population2)), (10 - mean(population2)) / stdev(population2, mean(population2))),
        (475, mean(population3), stdev(population3, mean(population3)), (475 - mean(population3)) / stdev(population3, mean(population3))),
        (mean(population1), mean(population1), stdev(population1, mean(population1)), 0),  # Testing the mean value which should have z-score of 0
        (greatest(population2), mean(population2), stdev(population2, mean(population2)), z_score(greatest(population2), mean(population2), stdev(population2, mean(population2))))
    ]

    all_passed = True
    for i, (x, mu, sigma, expected) in enumerate(test_cases):
        result = z_score(x, mu, sigma)
        if abs(result - expected) > 1e-6:  # Allowing small floating-point tolerance
            print(f"Test case {i + 1} failed: Expected {expected}, but got {result}")
            all_passed = False
        else:
            print(f"Test case {i + 1} passed.")

    if all_passed:
        print("All automated tests passed!")
    else:
        print("Some tests failed. Please check the details above.")

#Test function
test_z_score_function()

#Automated tests
run_automated_tests()