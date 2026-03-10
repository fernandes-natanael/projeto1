from menus import main_menu 
from csv_handler import get_all_crops, insert_crop, delete_crop
from model.crop import Crop
crops: list[Crop] = []


#  print("\n--- FARMTCH SOLUTIONS - MENU ---")
#     print("1. Inserir Dados (Entrada)")
#     print("2. Listar Dados (Saída)")
#     print("3. Atualizar Dados")
#     print("4. Deletar Dados")
#     print("5. Sair e Gerar Arquivo para o R")
#     return input("Escolha uma opção: ").strip()

def list_crops():
    if not crops:
        print("\nNenhum dado cadastrado foi encontrado.")
        return

    print("\nLista de Dados:")
    for index, crop in enumerate(crops):
        print(f'== idx: {index},  Tipo: {crop.type}, Área: {crop.area}, Manejo de Insumos: {crop.input_management}')


def delete_crop():
    index = input('Qual o index do dado que você deseja remover?\n:').strip()
    if not index.isdigit():
        print(f'Index "{index}" não é um número')
        return
    index = int(index)
    if not (0 <= index < len(crops)):
        print('Index não encontrado no sistema')
        return
    crop = crops[index]
    delete_crop(crop.id)


def update_crop():
    index = input('Qual o index do dado que você deseja atualizar?\n:').strip()
    if not index.isdigit():
        print(f'Index "{index}" não é um número')
        return
    index = int(index)
    if not (0 <= index < len(crops)):
        print('Index não encontrado no sistema')
        return
    crop = crops[index]
    
    


if __name__ == "__main__":
    crops = get_all_crops()
    exit = False
    while not exit:
        option = main_menu()

        if option == '1':
            x = 1
        elif option == '2':
            list_crops()
        elif option == '3':
            x = 3
        elif option == '4':
            delete_crop()
        elif option == '5':
            print('Programa está finalizando')
            exit = True
        else:
            print(f'Input {option} não foi definido')


