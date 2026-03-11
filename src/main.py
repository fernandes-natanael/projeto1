from menus import main_menu 
from csv_handler import get_all_crops, update_all_crops_in_csv
from model.crop import Crop

crops: list[Crop] = []

def list_crops():
    if not crops:
        print("\nNenhum dado cadastrado foi encontrado.")
        return

    print("\nLista de Dados:")
    for index, crop in enumerate(crops):
        print(f'== idx: {crop.id},  Tipo: {crop.type}, Área: {crop.area}, Manejo de Insumos: {crop.input_management}')

def delete_crop():
    id_input = input('Qual o ID do dado que você deseja remover?\n:').strip()    
    if not id_input.isdigit():
        print(f'[Error] ID "{id_input}" não é um número válido.')
        return
        
    target_id = int(id_input)
    
    for i, crop in enumerate(crops):
        if crop.id == target_id:
            del crops[i]
            print(f"[System] Cultura com ID {target_id} deletada com sucesso.")
            return
    print(f'[Error] Cultura com ID {target_id} não foi encontrada no sistema.')

def update_crop():
    index = input('Qual o index do dado que você deseja atualizar?\n:').strip()
    if not index.isdigit():
        print(f'[Error] ID "{index}" não é um número válido.')
        return
    target_id = int(index)

    crop = next((c for c in crops if c.id == target_id), None)
    
    if not crop:
        print(f'[Error] Cultura com ID {target_id} não encontrada no sistema.')
        return

    while True:
        cultura = input("Tipo de cultura (Manga/Cana) ou X para voltar: ").strip().capitalize()
        
        if cultura in ["Manga", "Cana", "X"]:
            break 
        else:
            print("[Erro] Cultura inválida. Por favor, digite 'Manga' ou 'Cana'.\n")
    
    if cultura == "X":
        print(f"[System] retornando para menu principal.")
        return
    if cultura == "Manga":
        width = float(input("Largura do terreno (m): "))
        length = float(input("Comprimento do terreno (m): "))
        street = int(input("Quantidade de ruas: "))
        liters_per_meter = float(input("Quantidade de litros por metro quadrado (l/m^2): "))

        area = length * width
        input_management = street * length * liters_per_meter
    else: 
        B = float(input("Base maior (m): "))
        b = float(input("Base menor (m): "))
        height = float(input("Altura (m): "))
        street = int(input("Quantidade de ruas: "))
        
        area = ((B + b) * height) / 2
        input_management = street * height * 0.8
    
    crop.area = area
    crop.type = cultura
    crop.area = area
    crop.input_management = input_management
    

def insert_crop():
    while True:
        cultura = input("Tipo de cultura (Manga/Cana) ou X para voltar: ").strip().capitalize()
        
        if cultura in ["Manga", "Cana", "X"]:
            break 
        else:
            print("[Erro] Cultura inválida. Por favor, digite 'Manga' ou 'Cana'.\n")

    # Lógica de cálculo baseada na cultura escolhida
    if cultura == "X":
        print(f"[System] retornando para menu principal.")
        return
    if cultura == "Manga":
        width = float(input("Largura do terreno (m): "))
        length = float(input("Comprimento do terreno (m): "))
        street = int(input("Quantidade de ruas: "))
        liters_per_meter = float(input("Quantidade de litros por metro quadrado (l/m^2): "))

        area = length * width
        input_management = street * length * liters_per_meter
    else: 
        B = float(input("Base maior (m): "))
        b = float(input("Base menor (m): "))
        height = float(input("Altura (m): "))
        street = int(input("Quantidade de ruas: "))
        
        area = ((B + b) * height) / 2
        input_management = street * height * 0.8

    nova_cultura = Crop(
        id=len(crops),
        type=cultura,
        area=area,
        input_management=input_management
    )

    # Adiciona o objeto na lista
    crops.append(nova_cultura)

    print(f"\n[Sucesso] {cultura} registrada com ID: {nova_cultura.id}")
    
if __name__ == "__main__":
    crops = get_all_crops()
    exit = False
    while not exit:
        option = main_menu()
        if option == '1':
            insert_crop()
        elif option == '2':
            list_crops()
        elif option == '3':
            update_crop()
        elif option == '4':
            delete_crop()
        elif option == '5':
            update_all_crops_in_csv(crops)
        elif option == '6':
            update_csv = input("Deseja atualizar csv com dados atuais s/n\n:").strip().lower()
            if update_csv == 's':
                update_all_crops_in_csv(crops)
            print('Programa está finalizando')
            exit = True
        else:
            print(f'Input {option} não foi definido')


