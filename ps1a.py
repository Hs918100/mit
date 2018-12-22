###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:


#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
import csv
import ps1_partition
import time
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    with open(filename) as file:
        cows = dict(csv.reader(file))
      # the key is the used to use a element wise orde
    return cows
# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here

    train = []
    # get tuples from dictionary key ordered by value high to low
    CowTupleList = sorted(cows.items(), key=lambda x: x[1], reverse=True)
    while (CowTupleList):
        #copy = CowTupleList[:]#[copy]
        temp_limit = limit
        temp = []
        cart =[]
        for name,weight in CowTupleList:#
            if int(weight)<=temp_limit:
                cart.append(name)
                temp_limit-=int(weight)
            else:
                temp.append((name,weight))
        train.append(cart)
        CowTupleList = temp
    end_time = time.time()
    return train

# i Hava to sort the dict
# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    real_list = []
    for Combination in ps1_partition.get_partitions(cows): #creating total combination and iterating on the total
        temp_limit = limit
        valid_list = []
        for i in range(len(Combination)):#using the length to find out elements in the combination
            val = 0
            cart =[]
            temp_limit = limit
            # iterating over the sublist
            for element in Combination[i]:
                val+=int(cows[element])
                if val>temp_limit:
                    break
                elif val==temp_limit or val<temp_limit:
                    cart.append(element)
            valid_list.append(cart) #adding the sublist to form a list
        if valid_list==Combination:#rejecting the combination which does not fit the criteria i.e if the Combinations is exceeding the limit
            real_list.append(Combination)#appending all the solutin in a list


    # finding the smallest listed solution because it is the optimal solution
    min_length = min(map(len,real_list))
    for element in real_list:
        if len(element)== min_length:
            return element










    #
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    start_time = time.time()
    solution_1 = greedy_cow_transport(load_cows('ps1_cow_data.txt'),limit=10)
    end_time = time.time()
    print('Time taken is greedy algorithm is',end_time-start_time)
    start_time = time.time()
    solution_2 = brute_force_cow_transport(load_cows('ps1_cow_data.txt'), limit=10)
    end_time = time.time()
    print('Time taken is Brute force algorithm is', end_time - start_time)

def main():
    # #greedy_solution=greedy_cow_transport(load_cows('ps1_cow_data.txt'),limit=10)
    # solutin = brute_force_cow_transport(load_cows('ps1_cow_data_2.txt'),limit=10)
    # #solutin = brute_force_cow_transport(load_cows('dict3.txt'), limit=100)
    # print(solutin)
    compare_cow_transport_algorithms()
if __name__=="__main__":
    main()

