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
		cedula TEXT NOT NULL 
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
    
    CREATE TABLE 
    enfermedad(
        id serial PRIMARY KEY 
        , descripcion varchar(60) UNIQUE
    );
    
    CREATE TABLE 
    ocupacion(
        id serial PRIMARY KEY 
        , descripcion varchar(60) UNIQUE
    );

    CREATE TABLE 
    cita(
        id serial PRIMARY KEY 
        , descripcion varchar(60) UNIQUE
    );

    CREATE TABLE 
    pago(
        id serial PRIMARY KEY 
        , descripcion varchar(60) UNIQUE
    );

    CREATE TABLE 
    horario(
        id serial PRIMARY KEY 
        , descripcion varchar(60) UNIQUE
    );

CREATE TABLE 
    Servicio(
        id serial PRIMARY KEY 
        , descripcion varchar(60) UNIQUE
    );
    
    