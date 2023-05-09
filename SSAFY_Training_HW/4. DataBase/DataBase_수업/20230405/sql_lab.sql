-- 주석입니다.


CREATE TABLE users(
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL 
);


CREATE TABLE contacts(
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  email TEXT NOT NULL
);

-- 테이블 이름 변경
ALTER TABLE contacts RENAME TO infos;

-- 필드 이름 변경 
ALTER TABLE infos RENAME COLUMN ddmail TO dmail;

-- 필드 추가
ALTER TABLE infos ADD COLUMN phone TEXT NOT NULL;

--  필드 추가 에러 발생하는경우
ALTER TABLE infos ADD COLUMN phone TEXT NOT NULL DEFAULT'no phone';

-- 필드 삭제
ALTER TABLE infos DROP COLUMN phone;

-- 테이블 삭제
DROP TABLE infos;

-- SELECT
SELECT * FROM users;
SELECT first_name, age FROM users;
SELECT rowid, first_name, age FROM users;

--정렬(ORDER BY)
SELECT first_name, age FROM users
ORDER BY age DESC, first_name;

SELECT DISTINCT first_name, country FROM users;

-- 실습 (5/10)
SELECT DISTINCT country FROM users ORDER BY country;

-- 실습 (8/10)
SELECT DISTINCT first_name, country FROM users;

-- WHERE 실습(1/4)
--
SELECT first_name, age, balance FROM users
WHERE age >= 30 ORDER BY balance DESC; 

-- WHERE 실습(3/4)
-- 나이가 30살 이상이고 계좌 잔고가 50만원 초과인 사람들의 이름,나이,계좌 잔고 조회

-- like 실습(1/10)
-- 이름에 호가 들어가는 사람 조회
SELECT last_name, first_name FROM users
WHERE first_name LIKE '%호%';

