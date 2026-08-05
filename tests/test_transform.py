import json
import os
import sys
import unittest

# Permite que o teste encontre o seu script transform.py dentro da pasta src/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.transform import transform_users


class TestUsersTransform(unittest.TestCase):

    def setUp(self):
        """Executado antes de cada teste: cria um arquivo JSON bruto de teste."""
        os.makedirs("data/raw", exist_ok=True)
        self.test_raw_path = "data/raw/users_raw.json"

        # Dados "sujos" de exemplo para testar a limpeza
        self.sample_raw_data = [{
            "id": "10",
            "name": "  maria da silva ",
            "email": "MARIA.SILVA@EMAIL.COM ",
            "created_at": "2026-02-01 08:30:00",
        }]

        with open(self.test_raw_path, "w", encoding="utf-8") as f:
            json.dump(self.sample_raw_data, f)

    def test_transform_users_rules(self):
        """Testa se as regras de limpeza foram aplicadas corretamente."""
        transformed = transform_users()
        record = transformed[0]  # Pega o registro transformado

        # 1. Valida se o ID virou número inteiro (10 em vez de "10")
        self.assertIsInstance(record["user_id"], int)
        self.assertEqual(record["user_id"], 10)

        # 2. Valida remoção de espaços e letras iniciais maiúsculas
        self.assertEqual(record["name"], "Maria Da Silva")

        # 3. Valida e-mail em minúsculas e sem espaços extras
        self.assertEqual(record["email"], "maria.silva@email.com")


if __name__ == "__main__":
    unittest.main()