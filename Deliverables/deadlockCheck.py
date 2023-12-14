import csv
import sys

def read_data_from_csv(filename):
    data = []
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if row[0]=="#":
                continue
            elif len(row) == 2:
                try:
                    x, y = float(row[0]), float(row[1])
                    data.append((x, y))
                except ValueError:
                    pass
    return data


def is_periodic1(data):
    if data[0][1]==0:
        check_up = 1
        check_down = 0
    else:
        check_up = 0
        check_down = 1
    for i in range(1, len(data)-2,2):
        if (check_up == 1 and (data[i][1] != 0 or data[i+1][1] != 1)):
            print("false up",data[i][0],data[i][1],data[i+1][1])
            return False
        if (check_down == 1 and (data[i][1] != 1 or data[i+1][1] != 0)):
            print("false down",data[i][0],data[i][1],data[i+1][1])
            return False
        if (check_up == 1):
            check_up = 0
            check_down = 1
        else: 
            check_up = 1
            check_down = 0
    return True


if __name__ == "__main__":
    # Check if exactly one command-line argument is provided
    if len(sys.argv) != 2:
        print("Wrong arguments")
        print("Usage: python deadlockCheck.py fileName.csv")
        sys.exit()

    # Access the single command-line argument
    filename = sys.argv[1]
    data = read_data_from_csv(filename)

    if is_periodic1(data):
        print("The data in the file "+filename+" represents a periodic function.")
    else:
        print("The data in the file "+filename+" does not represent a periodic function.")
