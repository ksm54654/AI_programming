import pickle

infile = open('UNDict.dat', 'rb')
countries = pickle.load(infile)
infile.close()

# def main():
#     nations = getDictionary("UNdict.dat")

    # print("Enter the name of a continent", end='')
    # continent = input("other than Antarctica : ")
    # contientDict = constructContinentNations(nations, continent)