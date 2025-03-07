-- 코드를 작성해주세요
# parent의 genotype을 join
SELECT A.ID, A.GENOTYPE, B.GENOTYPE AS PARENT_GENOTYPE
FROM ECOLI_DATA AS A, 
(
SELECT ID, GENOTYPE
FROM ECOLI_DATA
) AS B
WHERE A.PARENT_ID = B.ID AND BIN(A.GENOTYPE & B.GENOTYPE) = BIN(B.GENOTYPE)
ORDER BY ID;