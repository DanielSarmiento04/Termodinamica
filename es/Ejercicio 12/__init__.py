from colorama import init, Fore, Back, Style
import pyromat as pyro

aire = pyro.get('ig.air')


def get_T_2_from_T_1(T_1, relacion_presion, k):
    """
        Esta función calcula la temperatura final de un gas ideal a partir de la inicial,
        se debe tener en cuenta que la relación de presión  y la constante de los gases ideales
    """
    T_2 = T_1 * pow(relacion_presion, (k-1)/k)
    return T_2


def get_T_2s_by_T_1(T_1, relacion_presion):
    """
        Descripción
        -----------
        Esta función calcula la temperatura final de un gas ideal a partir de la inicial, 
        iterando el valor con el fin de converger a la temperatura final, usando el suposición
        de gas ideal.

        Base
        ----
        pv = nRT

        p * v ^ k  = constante

        p1 * v1 ^ k = p2 * v2 ^ k

        v2 = v1 * (p1 / p2) ^ (1/k)

        T2 = T1 * (p1 / p2) ^ ((k-1)/k)
    """

    cp_1 = aire.cp(T=T_1)[0]
    cv_1 = aire.cv(T=T_1)[0]
    k_prom_1_2 = k_1 = cp_1 / cv_1
    print("cp_1 = ", cp_1, "kJ/kg*K", "cv_1 = ", cv_1, "KJ/kg*K", "k_1 = ", k_1, "\n")
    for i in range(4):
        T_2s = get_T_2_from_T_1(T_1, relacion_presion, k_prom_1_2)
        cp_2s = aire.cp(T=T_2s)[0]
        cv_2s = aire.cv(T=T_2s)[0]
        k_2s = cp_2s / cv_2s
        k_prom_1_2 = (k_1 + k_2s) / 2
        print("cp_2s = ", cp_2s, "kJ/kg*K", "cv_2s = ", cv_2s, "KJ/kg*K", "k_2s = ", k_2s)
        print("k_prom = ", k_prom_1_2)
        print(Fore.LIGHTMAGENTA_EX,"T_2s = ", T_2s, "K", Style.RESET_ALL, "\n")

    return T_2s