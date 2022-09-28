# Laboratorio Dos
# Replicar el funcionamiento de ElGamal

import Crypto.Util.number  #libreria pycriptodome
import random
import time
import matplotlib.pyplot as plt
import numpy as np
import statistics
from tabulate import tabulate

bits = [1024, 1128, 1232, 1336, 1440, 1544, 1648, 1752, 1856, 1960, 2048]

# Modular exponentiation
def power(a, b, c):
    x = 1
    y = a
 
    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)
 
    return x % c

class ElGammal:
  def __init__(self, bits):
      self.bits = bits
      self.p = Crypto.Util.number.getPrime(
          self.bits, randfunc=Crypto.Random.get_random_bytes)
      self.g = Crypto.Util.number.getRandomRange(
          1, self.p - 1) % self.p

  def keygen(self):

      sk = Crypto.Util.number.getRandomRange(2, self.p - 1)  #public key
      self.pk = pow(self.g, sk, self.p)  #y = g^x * mod P

      return self.pk #regreso el public key

  def encrypt(self, pk, message):

      y = Crypto.Util.number.getRandomRange(2, self.p - 1)  #cipher text
      c1 = pow(self.g, y, self.p)
      c2 = (message * pow(pk, y, self.p)) % self.p
    
      return c1, c2

  def decrypt(self, c1, c2,secret_key):

      message = (c2 * power(c1, self.p-1-secret_key, self.p)) % self.p
         
      return message

class UsuarioA:
  def __init__():
    print("Usuario A")

  def _task_():
    return None

  def _get_message_():
    return None

  def _send_message_():
    return None

  def _compares_():
    return None

class UsuarioB:
  def __init__():
    print("Usuario B")

  def _task_():
    return None

  def _get_message_():
    return None

  def _send_message_():
    
  
def entidad_uno():
  '''
  1.- Genera una cadena de caracteres s
  tal que su longitud en bits es menor
  a la longitud de p
  2.- Cifra s, esto es, calcula c <- ElGamal.encrypt(s,X_B)
  3.- Envía c a B

  -Parte dos-
  Cuando recibe c', descifra para obtener s' y verifica inv(s) con s'
  '''
  return None


def entidad_dos():
  '''
  1.- Decifra c, calculando s <- ElGamal.decryt(c,x_B)
  2.- Calcula s' (inversa del arreglo)
  3.- Cifra s' esto es, calcula c' <- ElGamal.encrypt(s',X_A)
  4.- Envia c' a A
  '''
  return None

# Driver code
def main():
  msg = 'encryption'
  print("Original Message :", msg)


  elgamal = ElGammal(1024)
  
  key = elgamal.keygen() # Private key for receiver
  h = pow(elgamal.g, key, elgamal.p)
  print("g used : ", elgamal.g)
  print("g^a used : ", h)
  print("llave generada")
  print(key)
  print("Que es")
  print(elgamal.encrypt(key,msg))
  exit()
  dr_msg = elgamal.decrypt(en_msg, p, key, q)
  dmsg = ''.join(dr_msg)
  print("Decrypted Message :", dmsg)


if __name__ == '__main__':
    main()
