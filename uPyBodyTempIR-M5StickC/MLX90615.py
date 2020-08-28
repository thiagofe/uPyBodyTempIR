from urandom import getrandbits

n_reads_MLX90615 = 0
def Read_MLX90615_Temperatures():
    global n_reads_MLX90615
    n_reads_MLX90615 += 1
    
    if (n_reads_MLX90615 % 34) < 17:    # 17 medidas com temperatura ambiente, 17 com temperature de pessoa
        tObject = 3710 + getrandbits(20) % 10  # valores inteiros aleatório de 3710 à 3720
        tAmbient = 2500 + getrandbits(20) % 10 # valores inteiros aleatório de 2500 à 2510
        return (tObject, tAmbient)
    else:
        return (2500, 2500)   # Tobject = 25.00 C, Tambient = 25.00 C
