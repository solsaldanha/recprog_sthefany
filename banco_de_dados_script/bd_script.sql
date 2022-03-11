CREATE DATABASE diretores
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Portuguese_Brazil.1252'
    LC_CTYPE = 'Portuguese_Brazil.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;



create table Diretor(
	pid serial,
	nome text,
	email text,
	num_alunos int,
	idade int,
	primary key(pid)
);