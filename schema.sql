-- Creación tabla de usuarios
CREATE TABLE IF NOT EXISTS users (
  iUser_cod INTEGER PRIMARY KEY AUTOINCREMENT,
  tName TEXT UNIQUE NOT NULL,
  tPass TEXT NOT NULL,
  dCreated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  dModified TIMESTAMP
);

-- Creación registro de entrenameintos
CREATE TABLE IF NOT EXISTS activity (
  iActivity_id INTEGER PRIMARY KEY AUTOINCREMENT,
  tName TEXT NOT_NULL UNIQUE,
  tDescription TEXT,
  dCreated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  dModified TIMESTAMP
);

-- Creación registro de entrenameintos
CREATE TABLE IF NOT EXISTS training (
  iTraining_cod INTEGER PRIMARY KEY AUTOINCREMENT,
  iUser_cod INTEGER,
  iActivity INTEGER,
  iDistance REAL,
  iDuration TEXT,
  dCreated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  dModified TIMESTAMP,
  FOREIGN KEY (iUser_cod) REFERENCES usuarios(iUser_cod) ON DELETE CASCADE,
  FOREIGN KEY (iActivity) REFERENCES activity(iTraining_cod) ON DELETE CASCADE
);


/* DIVISION DE LOS ENTRENAMIENTOS EN DOS PARTES, EN CASO DE AGRUPAR ACTIVIDADES
DIFERENTES EN UNA MISMA SESION */

/* CREATE TABLE IF NOT EXISTS training_head (
  iTraining_cod INTEGER PRIMARY KEY AUTOINCREMENT,
  iUser_cod INTEGER,
  dCreated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  dModified TIMESTAMP,
  FOREIGN KEY (iUser_cod) REFERENCES usuarios(iUser_cod)
);

CREATE TABLE IF NOT EXISTS training_det (
  iLine INTEGER,
  iTraining INTEGER,
  iActivity INTEGER,
  iDuration INTEGER,
  iDistance REAL,
  PRIMARY KEY(iLine, iTraining)
  FOREIGN KEY (iTraining) REFERENCES training_head(iTraining_cod),
  FOREIGN KEY (iActivity) REFERENCES activity(iTraining_cod)
); */