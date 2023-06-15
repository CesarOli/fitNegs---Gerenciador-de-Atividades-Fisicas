CREATE DATABASE Gerenciador_de_Atividades_Fisicas;

USE Gerenciador_de_Atividades_Fisicas

CREATE TABLE atividadesFisicas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    atividade_fisica VARCHAR(150),
    tempo_da_atividade TIME,
    distancia DECIMAL(8,2),
    calorias_queimadas INT,
    data_da_atividade DATE,
    hora_da_atividade TIME
);

