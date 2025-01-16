from Parking import Parking

if __name__ == '__main__':
    for i in range(1,11):
        aparcar = Parking(str(i))
        aparcar.start()