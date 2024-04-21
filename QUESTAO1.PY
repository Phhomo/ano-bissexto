def eh_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True, "por ser divisível por 400"
            else:
                return False, "por ser divisível por 100 mas não por 400"
        else:
            return True, "por ser divisível por 4 e não por 100"
    else:
        return False, "por não ser divisível por 4"

def main():
    ano = int(input("Digite o ano que deseja verificar: "))
    bissexto, explicacao = eh_bissexto(ano)

    if bissexto:
        print("\nO ano", ano, "é bissexto,", explicacao)
        print("Portanto, possui 366 dias.")
    else:
        print("\nO ano", ano, "não é bissexto,", explicacao)
        print("Portanto, possui 365 dias.")

if __name__ == "__main__":
    main()
