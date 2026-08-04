import json
import os

def extract_raw_users():
    """Simula a extração de dados brutos de usuários."""
    print("Iniciando extração de dados brutos...")
    
    raw_data = [
        {"id": "1", "name": "Ana Silva", "email": "ANA@EMAIL.COM", "created_at": "2026-01-10 10:00:00"},
        {"id": "2", "name": "Bruno Souza", "email": "bruno@email.com", "created_at": "2026-01-11 11:30:00"},
        {"id": "3", "name": "Carla Dias", "email": "CARLA@EMAIL.COM", "created_at": "2026-01-12 14:15:00"}
    ]
    
    # Garante que a pasta data/raw existe
    os.makedirs("data/raw", exist_ok=True)
    
    output_path = "data/raw/users_raw.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(raw_data, f, indent=4)
        
    print(f"Extração concluída com sucesso. Dados salvos em: {output_path}")

if __name__ == "__main__":
    extract_raw_users()