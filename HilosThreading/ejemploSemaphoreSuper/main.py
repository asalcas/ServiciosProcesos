from Supermercado import Supermercado

if __name__ == '__main__':
    for i in range(1,16):
        super = Supermercado(str(i))
        super.start()