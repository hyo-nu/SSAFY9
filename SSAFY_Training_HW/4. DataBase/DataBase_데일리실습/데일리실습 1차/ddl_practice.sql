CREATE TABLE users(
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  age INTEGER NOT NULL,
  country TEXT NOT NULL,
  phone TEXT NOT NULL,
  balance INTEGER NOT NULL
);

-- 데일리 실습 1-1
SELECT first_name, age, balance FROM users
ORDER BY age, balance DESC;

-- 데일리 실습 1-2
SELECT first_name, age FROM users
ORDER BY first_name, age DESC;

-- 데일리 실습 1-3
-- 1
SELECT first_name, country FROM users
WHERE first_name = '건우' AND country = '경기도';
-- 2
SELECT first_name, country, age FROM users
WHERE country NOT IN ('강원도','경기도') AND age BETWEEN 20 AND 30
ORDER BY age;

-- 데일리 실습 1-4
SELECT first_name, phone, country FROM users
WHERE phone LIKE '%-51__-%' AND country != '서울';

-- 데일리 실습 1-5
SELECT * FROM users 
ORDER BY age LIMIT 20 OFFSET 40;

