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
		numero_cedula decimal(8) UNIQUE
	);