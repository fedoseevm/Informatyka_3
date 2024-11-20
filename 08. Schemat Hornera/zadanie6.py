def HornerBinToDec(bin):
    dec = int(binary[0])
    n = len(binary)
    for i in range(1, n):
        dec = 2 * dec + int(binary[i])
    return dec

def HornerBinToDecV2(bin):
    dec = 0
    for cyfra in bin:
        dec = 2 * dec + int(cyfra)
    return dec


binary = input("Podaj liczbę binarną: ")
print(HornerBinToDec(binary))
print(HornerBinToDecV2(binary))
