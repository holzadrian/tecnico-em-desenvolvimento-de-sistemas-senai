-- 1) Mostre o titulo_portugues e o ano_lancamento dos filmes lançados depois de 2000, em ordem crescente de ano.
SELECT titulo_portugues, ano_lancamento
FROM filme
WHERE ano_lancamento > 2000
ORDER BY ano_lancamento ASC;

-- 2) Liste o id, titulo_original e ano_lancamento dos filmes cujo título original contenha a palavra “Matrix”.
SELECT id, titulo_original, ano_lancamento
FROM filme
WHERE titulo_original LIKE '%Matrix%';

-- 3) Liste o titulo_original e o ano_lancamento dos filmes em que o título português seja igual ao inglês.
SELECT titulo_original, ano_lancamento
FROM filme
WHERE titulo_portugues = titulo_original;

-- 4) Liste os filmes que tenham titulo_original começando em "The" e/ou titulo_portugues começando com "O".
SELECT *
FROM filme
WHERE titulo_original LIKE 'The %'
   OR titulo_portugues LIKE 'O %';

-- 5) Mostre quais anos têm pelo menos um filme cadastrado na base.
SELECT DISTINCT ano_lancamento
FROM filme
ORDER BY ano_lancamento ASC;
