SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
FROM FOOD_FACTORY
WHERE LEFT(TLNO, 3)='033'
ORDER BY FACTORY_ID