--1 problem
CREATE TABLE zoo(
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT,
  height INT,
  age INT
);

--2 problem
INSERT INTO zoo 
VALUES
 ('gorilla','omnivore',215,180,5),
 ('rabbit','herbivore',3,150,NULL),
 ('tiger','carnivore',220,115,3),
 ('elephant','herbivore',3800,280,10),
 ('dog','omnivore',8,20,1),
 ('eagle','carnivore',8,75,NULL),
 ('dolphin','carnivore',21,NULL,3),
 ('alligator','carnivore',25,50,NULL),
 ('panda','herbivore',80,90,2),
 ('pig','omnivore',70,45,5);

--3 problem
SELECT name, height FROM zoo;

--4 problem
UPDATE zoo
SET height = 15
WHERE name = 'rabbit';

SELECT name, height FROM zoo
WHERE name = 'rabbit';

--5 problem
DELETE FROM zoo
WHERE eat = 'omnivore';

SELECT * FROM zoo;