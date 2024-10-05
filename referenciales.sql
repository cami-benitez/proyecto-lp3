CREATE TABLE 
    pais(
        id serial PRIMARY KEY 
        , descripcion varchar(60) UNIQUE
    );

CREATE TABLE
	personas(
		id serial PRIMARY KEY,
		descripcion varchar(60) UNIQUE,
		apellido varchar(50),
		numero_cedula TEXT NOT NULL 
	);
CREATE TABLE 
    dia(
        id serial PRIMARY KEY 
        , descripcion varchar(60) UNIQUE
    );
    
    CREATE TABLE 
    turno(
        id serial PRIMARY KEY 
        , descripcion varchar(60) UNIQUE
    );

    CREATE TABLE 
    Sexo(
        id serial PRIMARY KEY 
        , descripcion varchar(60) UNIQUE
    );
    
    
    CREATE TABLE 
    Diagnostico(
        id serial PRIMARY KEY 
        , descripcion varchar(60) UNIQUE
    );
    
CREATE TABLE 
    estadocivil(
        id serial PRIMARY KEY 
        , descripcion varchar(60) UNIQUE
    );
    