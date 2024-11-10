INSERT INTO felhasználó (id, felhasználó_név, jelszó, jogosultság)
VALUES 
  (1, 'kovacs.peter', 'jelszo123', 'csapat'),
  (2, 'nagy.janos', 'jelszo456', 'szervező'),
  (3, 'kiss.anna', 'jelszo789', 'iskola');

INSERT INTO iskola (id, felhasználó_id, iskola_nev, iskola_cím, kapcsolattartó_neve, kapcsolattart_email)
VALUES 
  (1, 3, 'Budapesti Iskola', 'Budapest, Fő utca 1', 'Dr. Szabó Márta', 'szabo.marta@iskola.hu'),
  (2, 3, 'Pécsi Középiskola', 'Pécs, Kossuth tér 3', 'Dr. Farkas Ádám', 'farkas.adam@iskola.hu');

INSERT INTO Kategória (kategória)
VALUES 
  ('Robotika'),
  ('Alkalmazásfejlesztés'),
  ('Játékfejlesztés');

INSERT INTO Programnyelvek (program_nyelv)
VALUES 
  ('Python'),
  ('Java'),
  ('C#'),
  ('C++');

INSERT INTO Csapat (id, felhasználó_id, csapatneve, felkészítő_tanár, iskola_id, valasztott_kategória, valasztott_program_nyelv)
VALUES 
  (1, 1, 'Programozó Emberek', 'Nagy Katalin', 1, 'Robotika', 'Python'),
  (2, 1, 'Kreatív Fejek', 'Tóth Balázs', 1, 'Alkalmazásfejlesztés', 'Java'),
  (3, 2, 'GAMING Mesterek', 'Papp Éva', 2, 'Játékfejlesztés', 'C++');

INSERT INTO tag (id, nev, evfolyam, póttag, csapat_id)
VALUES 
  (1, 'Molnár Dániel', '10', FALSE, 1),
  (2, 'Horváth László', '11', FALSE, 1),
  (3, 'Kiss Virág', '9', TRUE, 1),
  (4, 'Szabó Zsófia', '10', FALSE, 2),
  (5, 'Varga Bence', '11', FALSE, 2),
  (6, 'Farkas Nóra', '10', TRUE, 3);