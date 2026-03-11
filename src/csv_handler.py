import os
import uuid
import pandas as pd
from model.crop import Crop
from dataclasses import dataclass, asdict, fields

CSV_FILE = 'farm_tech_solutions.csv'
COLUMNS = [field.name for field in fields(Crop)]

def create_csv_file() -> None:
    if not os.path.exists(CSV_FILE):
        empty_df = pd.DataFrame(columns=COLUMNS)
        empty_df.to_csv(CSV_FILE, index=False)
        print(f"[System] Created new database file: {CSV_FILE}")

def get_all_crops() -> list[Crop]:
    create_csv_file()
    df = pd.read_csv(CSV_FILE)
    crops: list[Crop] = []
    for _, row in df.iterrows():
            crop = Crop(
                id=uuid.UUID(str(row['id'])),
                type=str(row['type']),
                area=float(row['area']),
                input_management=float(row['input_management'])
            )
            crops.append(crop)
            
    return crops

def insert_crop(crop: Crop) -> None:
    df = pd.read_csv(CSV_FILE)
    crop_dict = asdict(crop)
    crop_dict['id'] = str(crop_dict['id'])

    new_row_df = pd.DataFrame([crop_dict])
    df = pd.concat([df, new_row_df], ignore_index=True)
        
    df.to_csv(CSV_FILE, index=False)
    print(f"[Inserted] Crop: {crop.type} | Area: {crop.area}")

def update_crop(updated_crop: Crop) -> bool:
    df = pd.read_csv(CSV_FILE)
    target_id = str(updated_crop.id)
    
    if target_id not in df['id'].values:
        print(f"[Warning] Cultura com ID {target_id} não encontrada para atualização.")
        return False
        
    crop_dict = asdict(updated_crop)
    crop_dict['id'] = target_id
    
    index_to_update = df[df['id'] == target_id].index[0]
    
    for key, value in crop_dict.items():
        df.loc[index_to_update, key] = value
        
    df.to_csv(CSV_FILE, index=False)
    print(f"[Updated] Cultura atualizada com sucesso: {updated_crop.type} | Nova Área: {updated_crop.area}")
    return True

def delete_crop(crop_id: uuid.UUID) -> bool : 
    df = pd.read_csv(CSV_FILE)
    initial_count = len(df)
    df_filtered = df[df['id'] != str(crop_id)]

    if len(df_filtered) == initial_count:
        print(f"[Warning] Cultura não foi encontrada para deleção no csv.")
        return False        
    
    df_filtered.to_csv(CSV_FILE, index=False)
    print(f"[Deleted] Cultura deletada com sucesso.")
    return True

