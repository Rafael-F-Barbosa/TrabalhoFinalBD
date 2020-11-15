CREATE DATABASE IF NOT EXISTS BancoCovid;


USE BancoCovid;


-- Assim posso rodar tudo de uma vez
-- A ordem aqui é importante
DROP TABLE IF EXISTS SintomasPacientes;
DROP TABLE IF EXISTS Sintomas;
DROP TABLE IF EXISTS MedicacoesPacientes;
DROP TABLE IF EXISTS Medicacoes;
DROP TABLE IF EXISTS TestesPacientes;
DROP TABLE IF EXISTS Testes;
DROP TABLE IF EXISTS Pacientes;
DROP TABLE IF EXISTS Hospitais;
DROP TABLE IF EXISTS RegiaoAdmin;

-- Comecei criando pelo centro da tabela
-- Usei EssePadrao de case pro nome das tabelas
-- Coloquei as tabelas no plural 
CREATE TABLE IF NOT EXISTS RegioesAdmin(
	Codigo INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(65) NOT NULL,
    Populacao INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Hospitais(
	Endereco INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(65) NOT NULL,
    QtdLeitosDisponiveis INT NOT NULL,
    QtdLeitosOcupados INT NOT NULL,
    NumeroPessoasComCovid INT NOT NULL,
    CodRegiao INTEGER UNSIGNED,
    FOREIGN KEY(CodRegiao) references RegiaoAdmin(Codigo)
);


CREATE TABLE IF NOT EXISTS Pacientes(
	Cpf INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(65) NOT NULL,
    DataNascimento DATE NOT NULL,
    Endereco INTEGER UNSIGNED,
    FOREIGN KEY(Endereco) references Hospitais(Endereco)
);

CREATE TABLE IF NOT EXISTS Testes(
	Codigo INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(65) NOT NULL
);

CREATE TABLE IF NOT EXISTS TestesPacientes(
	DataTeste DATE NOT NULL,
    Resultado BOOLEAN NOT NULL,
    Codigo INTEGER UNSIGNED,
    FOREIGN KEY(Codigo) references Testes(Codigo),
    CpfPaciente INTEGER UNSIGNED,
    FOREIGN KEY(CpfPaciente) references Pacientes(Cpf)
);

CREATE TABLE IF NOT EXISTS Sintomas(
	Codigo INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(65) NOT NULL,
    Tipo VARCHAR(65) NOT NULL
);

CREATE TABLE IF NOT EXISTS SintomasPacientes(
	DataSintoma DATE NOT NULL,
    Codigo INTEGER UNSIGNED,
    FOREIGN KEY(Codigo) references Sintomas(Codigo),
    CpfPaciente INTEGER UNSIGNED,
    FOREIGN KEY(CpfPaciente) references Pacientes(Cpf)
);

CREATE TABLE IF NOT EXISTS Medicacoes(
	Codigo INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(65) NOT NULL
);

CREATE TABLE IF NOT EXISTS MedicacoesPacientes(
	DataMed DATE NOT NULL,
    DOSAGEM INTEGER NOT NULL,
    Codigo INTEGER UNSIGNED,
    FOREIGN KEY(Codigo) references Medicacao(Codigo),
    CpfPaciente INTEGER UNSIGNED,
    FOREIGN KEY(CpfPaciente) references Pacientes(Cpf)
);




