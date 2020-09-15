def euclidean_dist(x, y):
    """
    Calculate the euclidean distance between x and y
    """   
    return (sum([(a - b) ** 2 for a, b in zip(x, y)]))**(1/2)

def manhattan_dist(x, y):
    """
    Calculate the manhattan distance between x and y
    """ 
    return sum(abs(a-b) for a,b in zip(x,y))

def jaccard_dist(x, y):
    """
    Calculate the jaccard distance between x and y
    """
    if len(x) == 0 or len(y) == 0:
        raise ValueError("lengths must not be zero")
    x_set = set(x)
    y_set = set(y)
    intersection = len(x_set.intersection(y_set))
    union = len(x_set.union(y_set))
    return 1 - intersection/union

def cosine_sim(x, y):
    """
    Calculate the cosine similarity between x and y
    """
    if len(x) == 0 or len(y) == 0:
        raise ValueError("lengths must not be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")
    dot_res = 0
    magnitude_of_x = 0
    magnitude_of_y = 0
    for i in range(len(x)):
        dot_res += x[i] * y[i]
        magnitude_of_x += x[i]**2
        magnitude_of_y += y[i]**2
    magnitude_of_x = magnitude_of_x**(1/2)
    magnitude_of_y = magnitude_of_y**(1/2)
    return dot_res / (magnitude_of_x * magnitude_of_y)

# Feel free to add more
