def main():
    vicePresList = createListFromFile("VPres.txt")
    presList = createListFromFile("USPres.txt")
    createNewFile(vicePresList, presList, "Both.txt")

def createListFromFile(fileName):
    infile = open(fileName, 'r')
    desiredList = [line.rstrip() for line in infile]
    # desiredList = [line for line in infile]
    infile.close()
    return desiredList

def createNewFile(list_vice, list_pres, fileName):
    outfile = open(fileName, 'w')
    # set_vice = set(list_vice)
    # set_pres = set(list_pres)

    # set_both = set_vice.intersection(set_pres)

    # outfile.writelines(set_both)
    # outfile.close()

    for person in list_vice:
        if person in list_pres:
            outfile.write(person + '\n')
    outfile.close()

main()