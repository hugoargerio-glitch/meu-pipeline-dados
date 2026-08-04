-- sql/schema.sql
-- Tabela de destino para o pipeline de dados de usuários

CREATE TABLE IF NOT EXISTS users (
    user_id BIGINT PRIMARY KEY, -- Alterado para BIGINT (64 bits) para suportar escala
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);