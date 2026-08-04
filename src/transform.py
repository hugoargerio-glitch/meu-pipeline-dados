import json
import os

def transform_users():
    """Lê o arquivo bruto de usuários, sanitiza e-mails e converte tipos."""
    raw_path = "data/raw/users_raw.json"
    
    if not os.path.exists(raw_path):
        raise FileNotFoundError(f"Arquivo {raw_path} não encontrado. Execute o extract.py primeiro.")
        
    with open(raw_path, "r", encoding="utf-8") as f:
        users = json.load(f)
        
    transformed_users = []
    for user in users:
        transformed_users.append({
            "user_id": int(user["id"]),
            "name": user["name"].strip().title(),
            "email": user["email"].lower().strip(),
            "created_at": user["created_at"]
        })
        
    print(f"Transformação concluída: {len(transformed_users)} registros limpos.")
    return transformed_users

if __name__ == "__main__":
    transform_users()