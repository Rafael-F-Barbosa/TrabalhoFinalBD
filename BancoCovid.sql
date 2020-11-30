CREATE DATABASE IF NOT EXISTS BancoCovid;

USE BancoCovid;

-- A ordem aqui é importante
DROP TABLE IF EXISTS SintomasPacientes;
DROP TABLE IF EXISTS Sintomas;
DROP TABLE IF EXISTS MedicacoesPacientes;
DROP TABLE IF EXISTS Medicacoes;
DROP TABLE IF EXISTS TestesPacientes;
DROP TABLE IF EXISTS Testes;
DROP TABLE IF EXISTS Acoes;
DROP TABLE IF EXISTS SituacaoAtual;
DROP TABLE IF EXISTS ProfTabalhaHospital;
DROP TABLE IF EXISTS ProfAtendePaciente;
DROP TABLE IF EXISTS ProfissionaisSaude;
DROP TABLE IF EXISTS ParentePaciente;
DROP TABLE IF EXISTS Parentes;
DROP TABLE IF EXISTS Pacientes;
DROP TABLE IF EXISTS Hospitais;
DROP TABLE IF EXISTS RegiaoAdmin;


CREATE TABLE IF NOT EXISTS RegiaoAdmin(
	Codigo INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(65) NOT NULL,
    Populacao INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS SituacaoAtual(
	DataSituacao DATE NOT NULL,
    CasosLeves INT UNSIGNED NOT NULL,
    CasosGraves INT UNSIGNED NOT NULL,
    Mortes INT UNSIGNED NOT NULL,
    Recuperados INT UNSIGNED NOT NULL,
    CodRegiao INT UNSIGNED NOT NULL,
    FOREIGN KEY (CodRegiao) references RegiaoAdmin(Codigo),
    PRIMARY KEY (DataSituacao, CodRegiao)
);

CREATE TABLE IF NOT EXISTS Acoes(
	Codigo INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    Eficiencia INT UNSIGNED NOT NULL,
    Tipo VARCHAR(45) NOT NULL,
    CodRegiao INT UNSIGNED NOT NULL,
    FOREIGN KEY (CodRegiao) references RegiaoAdmin(Codigo)
);

CREATE TABLE IF NOT EXISTS Hospitais(
	Codigo INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	Cep VARCHAR(12) NOT NULL,
    Nome VARCHAR(65) NOT NULL,
    QtdLeitosDisponiveis INT UNSIGNED NOT NULL,
    QtdLeitosOcupados INT UNSIGNED NOT NULL,
    NumeroPessoasComCovid INT UNSIGNED NOT NULL,
    CodRegiao INT UNSIGNED,
    FOREIGN KEY(CodRegiao) references RegiaoAdmin(Codigo)
);


CREATE TABLE IF NOT EXISTS Pacientes(
	Cpf VARCHAR(11) PRIMARY KEY,
    Nome VARCHAR(65) NOT NULL,
    DataNascimento DATE NOT NULL,
    CodHospital INT UNSIGNED,
    FOREIGN KEY(CodHospital) references Hospitais(Codigo)
);

CREATE TABLE IF NOT EXISTS Testes(
	Codigo INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(65) NOT NULL
);

CREATE TABLE IF NOT EXISTS TestesPacientes(
	DataTeste DATE NOT NULL,
    Resultado BOOLEAN NOT NULL,
    CodTeste INT UNSIGNED NOT NULL,
    FOREIGN KEY(CodTeste) references Testes(Codigo),
    CpfPaciente VARCHAR(11) NOT NULL,
    FOREIGN KEY(CpfPaciente) references Pacientes(Cpf),
    PRIMARY KEY (CodTeste, CpfPaciente)
);

CREATE TABLE IF NOT EXISTS Sintomas(
	Codigo INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(65) NOT NULL,
    Tipo VARCHAR(65) NOT NULL
);

CREATE TABLE IF NOT EXISTS SintomasPacientes(
	DataSintoma DATE NOT NULL,
    CodSintoma INT UNSIGNED NOT NULL,
    FOREIGN KEY(CodSintoma) references Sintomas(Codigo),
    CpfPaciente VARCHAR(11) NOT NULL,
    FOREIGN KEY (CpfPaciente) references Pacientes(Cpf),
    PRIMARY KEY (CodSintoma, CpfPaciente)
);

CREATE TABLE IF NOT EXISTS Medicacoes(
	Codigo INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(65) NOT NULL
);

CREATE TABLE IF NOT EXISTS MedicacoesPacientes(
	DataMed DATE NOT NULL,
    Dosagem VARCHAR(45) NOT NULL,
    CodMedicacao INT UNSIGNED NOT NULL,
    FOREIGN KEY(CodMedicacao) references Medicacoes(Codigo),
    CpfPaciente VARCHAR(11) NOT NULL,
    FOREIGN KEY(CpfPaciente) references Pacientes(Cpf),
    PRIMARY KEY (CodMedicacao, CpfPaciente)
);

CREATE TABLE IF NOT EXISTS ProfissionaisSaude(
	CPF VARCHAR(11) PRIMARY KEY,
    Nome VARCHAR(65) NOT NULL,
    Profissao VARCHAR(45) NOT NULL,
    TeveCovid BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS ProfTabalhaHospital(
	CodHospital INT UNSIGNED NOT NULL,
    CpfProfissional VARCHAR(11) NOT NULL,
    FOREIGN KEY (CodHospital) references Hospitais(Codigo),
    FOREIGN KEY (CpfProfissional) references ProfissionaisSaude(Cpf),
    PRIMARY KEY (CodHospital, CpfProfissional)
);

CREATE TABLE IF NOT EXISTS ProfAtendePaciente(
	CpfPaciente VARCHAR(11) NOT NULL,
    CpfProfissional VARCHAR(11) NOT NULL,
    FOREIGN KEY (CpfPaciente) references Pacientes(Cpf),
    FOREIGN KEY (CpfProfissional) references ProfissionaisSaude(Cpf),
    PRIMARY KEY (CpfPaciente, CpfProfissional)
);

CREATE TABLE IF NOT EXISTS Parentes(
	Cpf VARCHAR(11) PRIMARY KEY,
    Nome VARCHAR(45) NOT NULL,
    DataNascimento DATE NOT NULL,
    TeveContato BOOLEAN NOT NULL -- Talvez isso aqui devesse estar
    -- na tabela de relacionamento, em
);

CREATE TABLE IF NOT EXISTS ParentePaciente(
	CpfPaciente VARCHAR(11) NOT NULL,
    CpfParente VARCHAR(11) NOT NULL,
    FOREIGN KEY (CpfPaciente) references Pacientes(Cpf),
    FOREIGN KEY (CpfParente) references Parentes(Cpf),
    PRIMARY KEY (CpfPaciente, CpfParente)
);


-- Stored Procedures

DROP PROCEDURE IF EXISTS RastreiaProfsPacientes;

CREATE PROCEDURE RastreiaProfsPacientes(CPF VARCHAR(11))
SELECT Nome, CPF
FROM ProfissionaisSaude
INNER JOIN ProfAtendePaciente ON ProfAtendePaciente.CpfProfissional = ProfissionaisSaude.CPF
WHERE ProfAtendePaciente.CpfPaciente = CPF;

DROP PROCEDURE IF EXISTS RastreiaParentesPacientes;

CREATE PROCEDURE RastreiaParentesPacientes(CPF VARCHAR(11))
SELECT Nome, Cpf
FROM Parentes
INNER JOIN ParentePaciente ON ParentePaciente.CpfParente = Parentes.Cpf
WHERE ParentePaciente.CpfPaciente = CPF;

DROP PROCEDURE IF EXISTS InformacoesDf;

CREATE PROCEDURE InformacoesDf(d DATE)
SELECT SUM(CasosLeves), SUM(CasosGraves), SUM(Mortes), SUM(Recuperados) FROM SituacaoAtual
WHERE DataSituacao = d;

DROP PROCEDURE IF EXISTS RastreiaMedicacoesPacientes;

CREATE PROCEDURE RastreiaMedicacoesPacientes(CPF VARCHAR(11))
SELECT Nome, Dosagem, DataMed
FROM Medicacoes, MedicacoesPacientes
WHERE MedicacoesPacientes.CpfPaciente = CPF AND Medicacoes.Codigo = MedicacoesPacientes.CodMedicacao;

DROP PROCEDURE IF EXISTS RastreiaTestesPacientes;

CREATE PROCEDURE RastreiaTestesPacientes(CPF VARCHAR(11))
SELECT Nome, DataTeste, Resultado
FROM Testes, TestesPacientes
WHERE TestesPacientes.CpfPaciente = CPF AND Testes.Codigo = TestesPacientes.CodTeste;

DROP PROCEDURE IF EXISTS RastreiaSintomasPacientes;

CREATE PROCEDURE RastreiaSintomasPacientes(CPF VARCHAR(11))
SELECT Nome, Tipo, DataSintoma
FROM Sintomas, SintomasPacientes
WHERE SintomasPacientes.CpfPaciente = CPF AND Sintomas.Codigo = SintomasPacientes.CodSintoma;



-- Views

DROP VIEW IF EXISTS vw_hospitais_cheios;


CREATE VIEW vw_hospitais_cheios
AS
SELECT Codigo, Nome, Cep FROM Hospitais
WHERE QtdLeitosDisponiveis = 0;
