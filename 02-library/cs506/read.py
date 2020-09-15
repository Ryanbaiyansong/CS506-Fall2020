def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    res = [] #matrix to store the result
    with open(csv_file_path) as csvDataFile:
        rows = csvDataFile.readlines()

    for row in rows:
        data = row.strip().split(",") # split by comma
        res.append([eval(val) for val in data])
            
    return res
