-- 코드를 작성해주세요
SELECT A.id AS ITEM_ID, A.ITEM_NAME AS ITEM_NAME, A.RARITY as RARITY
FROM ( 
    SELECT ITEM_INFO.ITEM_ID as id, ITEM_NAME, RARITY, PARENT_ITEM_ID
    FROM ITEM_INFO JOIN ITEM_TREE USING(ITEM_ID) 
) as A, 
ITEM_INFO
WHERE A.PARENT_ITEM_ID = ITEM_INFO.ITEM_ID AND ITEM_INFO.RARITY ='RARE'
ORDER BY A.id DESC;
