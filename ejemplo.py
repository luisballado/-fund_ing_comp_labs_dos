#BASURA
def main():

  bits = [1024, 1128, 1232, 1336, 1440, 1544, 1648, 1752, 1856, 1960, 2048]
  
  _bits_ = 1024
  msg = 'soy un secreto'
  print("Original Message :", msg)
  
  # USUARIOA
  q = Crypto.Util.number.getPrime(_bits_, randfunc=Crypto.Random.get_random_bytes)
  g = Crypto.Util.number.getRandomRange(
          1, q - 1) % q
  
  key = keygen(q) #Llave privada para el receptor
  h = pow(g, key, q) #despues calcula h=g^a
  print("g used : ", g) #g
  print("g^a used : ", h) #g^a
  
  #USUARIOB encripta informacion usando la llave publica de USUARIOA
  en_msg, p = encrypt(msg, q, h, g)
  print("Cadena encriptada")
  print(en_msg)
  
  #USUARIOA desencripta el mensaje
  dr_msg = decrypt(en_msg, p, key, q)
  dmsg = ''.join(dr_msg)
  print("Decrypted Message :", inv_palabra(dmsg));


def keygen(q):

  #generacion secret key
	key = Crypto.Util.number.getRandomRange(2, q - 1)

	return key

# Encriptacion Asimetrica
def encrypt(msg, q, h, g):

	en_msg = []

  #USUARIOB selects an element k from cyclic group F
	k = keygen(q)# Private key for sender

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

	return en_msg, p #then she sends (p,M*s) = (g^k,M*s)

def decrypt(en_msg, p, key, q):

	dr_msg = []
  #calcular s' = p^a = g^ak
	h = pow(p, key, q)
	for i in range(0, len(en_msg)):
    #dividir M*s por s' para obtener M como s=s'
		dr_msg.append(chr(int(en_msg[i]/h)))
		
	return dr_msg