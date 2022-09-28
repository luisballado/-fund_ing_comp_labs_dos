# Laboratorio Dos
# Replicar el funcionamiento de ElGamal

import Crypto.Util.number  #libreria pycriptodome
import time
import statistics
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
import string
import random

class ElGammal:

    def __init__(self, bits):
        self.bits = bits
        self.p = Crypto.Util.number.getPrime(
            self.bits, randfunc=Crypto.Random.get_random_bytes)
        self.g = Crypto.Util.number.getRandomRange(1, self.p - 1) % self.p

    def keygen(self):

        sk = Crypto.Util.number.getRandomRange(2, self.p - 1)  #public key
        self.pk = pow(self.g, sk, self.p)  #y = g^x * mod P

        return self.pk  #regreso el public key

    def encrypt(self, pk, message):

        y = Crypto.Util.number.getRandomRange(2, self.p - 1)  #cipher text
        c1 = pow(self.g, y, self.p)
        c2 = (message * pow(pk, y, self.p)) % self.p

        return c1, c2

    def decrypt(self, c1, c2, secret_key):

        message = (c2 * pow(c1, self.p - 1 - secret_key, self.p)) % self.p

        return message


def keygen(q):

    #generacion secret key
    key = Crypto.Util.number.getRandomRange(2, q - 1)

    return key


# Encriptacion Asimetrica
def encrypt(msg, q, h, g):

    en_msg = []

    #USUARIOB selects an element k from cyclic group F
    k = keygen(q)  # Private key for sender

    #then she computes p=g^k and s=h^k = g^(ak)
    s = pow(h, k, q)
    p = pow(g, k, q)

    #copiar el arreglo en otro arreglo
    for i in range(0, len(msg)):
        en_msg.append(msg[i])

    print("g^k used : ", p)
    print("g^ak used : ", s)

    #encriptar caracter por caracter para encriptarlo
    for i in range(0, len(en_msg)):
        en_msg[i] = s * ord(en_msg[i])

    return en_msg, p  #then she sends (p,M*s) = (g^k,M*s)


def decrypt(en_msg, p, key, q):

    dr_msg = []
    #calcular s' = p^a = g^ak
    h = pow(p, key, q)
    for i in range(0, len(en_msg)):
        #dividir M*s por s' para obtener M como s=s'
        dr_msg.append(chr(int(en_msg[i] / h)))

    return dr_msg

def generar_palabras(longitud):
  letters = string.ascii_uppercase
  return ''.join(random.choice(letters) for i in range(longitud))

def inv_palabra(palabra):
    return palabra[::-1]

def graficar(x_datos, y_datos, result_arr):

    print(tabulate(result_arr))

    x1 = np.array(x_datos)
    y1 = np.array(y_datos)

    plt.plot(x1, y1, marker="o")

    plt.title("Lab2: ElGamal")
    plt.xlabel("Nivel de seguridad (bits)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.grid()
    plt.show()



def main():

    _bits_ = [1024, 1128, 1232, 1336, 1440, 1544, 1648, 1752, 1856, 1960, 2048]
    time_cicle = []
    time_mean = []
    _result_arr_ = []

    for bits in _bits_:

        _bits_arr_ = []
        _bits_arr_.append("Bits")
        _bits_arr_.append(bits)
        start_time_cicle = time.time()

        for i in range(31):
            msg = generar_palabras(10)
            print("Original Message :", msg)

            # USUARIOA
            q = Crypto.Util.number.getPrime(
                bits, randfunc=Crypto.Random.get_random_bytes)
            g = Crypto.Util.number.getRandomRange(1, q - 1) % q

            key = keygen(q)  #Llave privada para el receptor
            h = pow(g, key, q)  #despues calcula h=g^a
            print("g used : ", g)  #g
            print("g^a used : ", h)  #g^a

            #USUARIOB encripta informacion usando la llave publica de USUARIOA
            en_msg, p = encrypt(msg, q, h, g)
            print("Cadena encriptada")
            print(en_msg)

            #USUARIOA desencripta el mensaje
            dr_msg = decrypt(en_msg, p, key, q)
            dmsg = ''.join(dr_msg)

            print("Decrypted Message :", inv_palabra(dmsg))
          
            if inv_palabra(msg) == inv_palabra(dmsg):
                print("Son iguales")
            else:
                print("No iguales")

            time_cicle.append(time.time() - start_time_cicle)

        mean = statistics.mean(time_cicle)

        _bits_arr_.append(mean)
        time_mean.append(mean)
        _result_arr_.append(_bits_arr_)

    # create data
    graficar(_bits_, time_mean, _result_arr_)


if __name__ == '__main__':
    main()
