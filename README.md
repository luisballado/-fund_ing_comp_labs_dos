# Fundamentos de Ingeniería Computacional

## Laboratorio 2

![grafica_resultados](https://raw.githubusercontent.com/luisballado/-fund_ing_comp_labs_dos/main/elgamal_graph.png "Grafica de resultados")

## Implementar un programa que realice lo siguiente: ##

1. Debe recibir como entrada un número primo p, de cualquier tamaño (por ejemplo los recomendados para aplicaciones criptográficas (1024,2048,.. bits)
2. Construir un Grupo multiplicativo $$Zp^{*}$$ (usando el conjunto {1,2,...p-1} y la operación * mod p
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


## Inicio

El proyecto está escrito en lenguaje python3.8 (el cual no es muy recomendable para aplicaciones donde se espera un mejor "performance") 
con ayuda de la libreria [pycryptodome](https://www.pycryptodome.org/ "pycryptodome")

### Prerequisitos

Tener la versión >= python3.

Instalar las dependencias marcadas bajo el comando 

```bash
pip install <nombre_paquete>
```

Dependencias

```
* cryptography = "^38.0.1"
* pycryptodome = "^3.15.0"
* pycryptodomex = "^3.15.0"
* matplotlib = "^3.6.0"
* tabulate = "^0.8.10"
```

### Versión replit

Se cuenta una versión funcional del laboratorio en la plataforma replit. (Se debe de contar con una cuenta)
Debido a que es una cuenta gratuita los resultados son limitados, pero funcionales.

https://replit.com/join/szodbvyxqb-luisballado


## Funcionamiento



## Código

Arreglo de bits usados

```python
bits = [1024,1128,1232,1336,1440,1544,1648,1752,1856,1960,2048]
```


```python

```

## Creación de gráfica 

Con uso de la libreria [matplotlib](https://matplotlib.org/ "matplotlib") a partir de los datos generados


```python
def graficar(x_datos,y_datos,result_arr):

  
  print(tabulate(result_arr))
  
  x1 = np.array(x_datos)
  y1 = np.array(y_datos)
  
  plt.plot(x1, y1, marker="o")
  
  plt.title("Lab2: ElGamal")
  plt.xlabel("Nivel de seguridad (bits)")
  plt.ylabel("Tiempo de ejecución (segundos)")
  plt.grid()
  plt.show()
```

#### Generación palabras random de longitud n
```python
def generar_palabras(longitud):
  letters = string.ascii_uppercase
  return ''.join(random.choice(letters) for i in range(longitud))
```

#### Inversa de una palabra

```python
def inv_palabra(palabra):
    return palabra[::-1]
```

#### Comparación de las palabras inversas

```python
if inv_palabra(msg) == inv_palabra(dmsg):
  print("Son iguales")
else:
  print("No iguales")
```

## Tabla de tiempos

Tomando en cuenta que la ejecución se realizó en replit con una máquina de baja caracteristicas, se puede observar que a medida que se incrementa la dificultad en la generación del número primo p en base a los bits, el tiempo de ejecución aumenta exponencialmente.

 Bits | Segundos
----- | --------
 1024 | 10.1963
 1128 | 10.914
 1232 | 10.7621
 1336 | 12.1107
 1440 | 14.1563
 1544 | 15.6374
 1648 | 17.0804
 1752 | 18.6815
 1856 | 20.8248
 1960 | 24.4412
 2048 | 27.9625