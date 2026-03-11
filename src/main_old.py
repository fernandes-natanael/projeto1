import csv
nomes_culturas = []
areas_calculadas = []
insumos_totais = []

def menu():
    while True:
        print("\n--- FARMTCH SOLUTIONS - MENU ---")
        print("1. Inserir Dados (Entrada)")
        print("2. Listar Dados (Saída)")
        print("3. Atualizar Dados")
        print("4. Deletar Dados")
        print("5. Sair e Gerar Arquivo para o R")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cultura = input("Tipo de cultura (Manga/Cana): ").capitalize()
            if cultura == "Manga":

                l = float(input("Largura do terreno (m): "))
                c = float(input("Comprimento do terreno (m): "))
                area = l * c

                ruas = int(input("Quantidade de ruas: "))
                litros_por_metro = float(input("Quantidade de litros por metro quadrados (m): "))
                total_insumo = ruas * c * litros_por_metro

            else:

                B = float(input("Base maior (m): "))
                b = float(input("Base menor (m): "))
                h = float(input("Altura (m): "))
                area = ((B + b) * h) / 2
                ruas = int(input("Quantidade de ruas: "))
                total_insumo = ruas * h * 0.8

            nomes_culturas.append(cultura)
            areas_calculadas.append(area)
            insumos_totais.append(total_insumo)

        elif opcao == '2':
            for i in range(len(nomes_culturas)):
                print(f"[{i}] {nomes_culturas[i]} | Área: {areas_calculadas[i]}m² | Insumo: {insumos_totais[i]}L")

        elif opcao == '3':

            if not insumos_totais:
                print("Erro: A lista está vazia. Adicione um insumo primeiro (Opção 1 ou 2).")
            else:
                try:

                    print(f"Lista atual: {insumos_totais}")
                    print(f"Escolha um índice que sejá maior do que 0:  {len(insumos_totais) - 1}")

                    idx_input = input("Índice para atualizar: ")


                    idx = int(idx_input)


                    novo_valor = float(input('Novo valor de insumo: '))
                    insumos_totais[idx] = novo_valor

                    print(f"Sucesso! O índice {idx} agora vale {novo_valor}")

                except ValueError:
                    print("Erro: Digite apenas números!")
                except IndexError:
                    print("Erro: Esse índice não existe na lista. Tente um dos números mostrados acima.")



        elif opcao == '4':
            idx = int(input("Índice para deletar: "))
            nomes_culturas.pop(idx)
            areas_calculadas.pop(idx)
            insumos_totais.pop(idx)

        elif opcao == '5':

            with open('dados_fazenda.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Cultura", "Area", "Insumo"])
                for i in range(len(nomes_culturas)):
                    writer.writerow([nomes_culturas[i], areas_calculadas[i], insumos_totais[i]])
            print("Dados salvos! Saindo...")
            break


menu()