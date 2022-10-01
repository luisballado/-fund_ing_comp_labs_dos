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

#Clase para englobar las funciones de ElGamal
class ElGammal:

    def __init__(self, bits):
        self.bits = bits
        self.p = Crypto.Util.number.getPrime(
            self.bits, randfunc=Crypto.Random.get_random_bytes)
        self.g = Crypto.Util.number.getRandomRange(1, self.p - 1) % self.p

    def keygen(self):

        self.sk = Crypto.Util.number.getRandomRange(2, self.p - 1)  #public key
        self.pk = pow(self.g, self.sk, self.p)  #y = g^x * mod P

        return self.sk, self.pk  #regreso el public key

    def encrypt(self, pk, message):

        encrypt_msg = []

        y = Crypto.Util.number.getRandomRange(2, self.p - 1)  #cipher text
        c1 = pow(self.g, y, self.p)
        Z = pow(pk, y, self.p)
        #copiar el arreglo en otro arreglo
        for i in range(0, len(message)):
            encrypt_msg.append(message[i])

        for i in range(0, len(encrypt_msg)):
            encrypt_msg[i] = ord(encrypt_msg[i]) * Z

        return c1, encrypt_msg

    def decrypt(self, sk, c, p):

        dr_msg = []
        h = pow(c[0], sk, p)
        mensaje = c[1]
        for i in range(0, len(mensaje)):
            dr_msg.append(chr(int(mensaje[i] / h)))

        return dr_msg


#funcion generar palabras random
def generar_palabra(longitud):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(longitud))


#funcion invertir una cadena de caracteres
def inv_palabra(palabra):
    return palabra[::-1]


#funcion graficar resultados y mostrar tabla
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
            msg = generar_palabra(10)

            print("Mensaje Original :", msg)

            elgamal = ElGammal(bits)

            # USUARIOA
            # Generar llave
            k_private_A, k_public_A = elgamal.keygen()

            #USUARIOB
            # Generar llave
            k_private_B, k_public_B = elgamal.keygen()

            #USUARIOA encripta usando llave pub de USUARIOB
            c = elgamal.encrypt(k_public_B, msg)

            #USUARIOB recibe el mensaje encriptado y lo des-encripta
            dr_msg = elgamal.decrypt(k_private_B, c, elgamal.p)
            dmsg = ''.join(dr_msg)

            #USUARIOB invierte el mensaje
            msg_inv = inv_palabra(dmsg)

            #USUARIOB encripta el mensjae
            c_dos = elgamal.encrypt(k_public_A, msg_inv)

            #USUARIOA recibe el mensaje encriptado
            #y lo des-encripta
            dr_msg_dos = elgamal.decrypt(k_private_A, c_dos, elgamal.p)
            dmsg_dos = ''.join(dr_msg_dos)
            print(dmsg_dos)

            #compara con el mensaje original invertido
            if inv_palabra(msg) == dmsg_dos:
                print("Son iguales")
            else:
                print("No son iguales")

            time_cicle.append(time.time() - start_time_cicle)

        mean = statistics.mean(time_cicle)

        _bits_arr_.append(mean)
        time_mean.append(mean)
        _result_arr_.append(_bits_arr_)

    # create data
    graficar(_bits_, time_mean, _result_arr_)


if __name__ == '__main__':
    main()
