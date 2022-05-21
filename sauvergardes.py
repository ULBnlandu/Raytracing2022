def save(tableau):
    with open('heatMapAvion.txt', 'a') as file:
        file.truncate(0)
        for element in tableau:
            file.write(str(element)+'\n')
        file.close()
def retrieveArray():
    with open('heatMapAvion.txt', 'r') as file:
        for line in file:
            print(line)
        file.close

tableau = [0, 48, 48, 29, 2687, 2829, 2992, 27828]
save(tableau)
retrieveArray()