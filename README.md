# Fundamentos de Ingeniería Computacional

## Laboratorio 2

## Implementar un programa que realice lo siguiente: ##

1. Debe recibir como entrada un número primo p, de cualquier tamaño (por ejemplo los recomendados para aplicaciones criptográficas (1024,2048,.. bits)
2. Construir un Grupo multiplicativo Zp* (usando el conjunto {1,2,...p-1} y la operación * mod p
3. Usar como generador algún elemento aleatorio de Zp*
4. Usando ElGamal, se deberán generar dos parejas de llaves con el algoritmo ElGamal.keyGen()
5. Realizar lo siguiente:
    * Generar una cadena de caracteres s = [c1,c2,c3...cn] tal que su longitud en bits es menor a la longitud de p
    * Cifra s, esto es: calcula x <-- ElGamal.encrypts(s,X_B)
    *  Envia c a B   
6. Cuando B recibe c, realiza lo siguiente
    * Descifra c, calculando s <-- ElGamal.decrypt(c,X_B)
    * Calcula s' = [cn...c3,c2,c1]
    * Cifra s', esto es, calcula c' <-- ElGamal.encrypt(s',X_A)
    * Envia c' a A
7. Cuando A recibe c', descifra para obtener s', y verifica que si s' = [cn...c3,c2,c1]
8. Se deberán ejecutar los pasos 4-7 en al menos 10 casos de prueba, usando un valor de p diferente para cada caso, siendo que p puede ser de entre 1024 y 2048 bits.
9. Reportar en una tabla de tiempos la ejecución para cada caso de prueba.
    * Eje X: Nivel de seguridad (tamaño en bits de p)
    * Eje Y: tiempo de ejecución de los pasos 4-7


### Prerequisites

The things you need before installing the software.

* You need this
* And you need this
* Oh, and don't forget this

### Installation

A step by step guide that will tell you how to get the development environment up and running.

```
$ First step
$ Another step
$ Final step
```

## Usage

A few examples of useful commands and/or tasks.

```
$ First example
$ Second example
$ And keep this in mind
```

## Deployment

Additional notes on how to deploy this on a live or release system. Explaining the most important branches, what pipelines they trigger and how to update the database (if anything special).

### Server

* Live:
* Release:
* Development:

### Branches

* Master:
* Feature:
* Bugfix:
* etc...

## Additional Documentation and Acknowledgments

* Project folder on server:
* Confluence link:
* Asana board:
* etc...
