--TEST FOR THE VARIABLE PL/SQL
--VARIABLE v_bind := VARCHAR2(10);  -- Bind variables 
--EXEC :v_bind := 'TEST'


SET SERVEROUT ON;
DECLARE
    --test_constant CONSTANT NUMBER(7,6) := 7.45689;   -- Contsant need to initialize in here
    --test_constant CONSTANT NUMBER(7,6) NOT NULL DEFAULT 7.45689;
    --my_name     VARCHAR2(10); -- Declare the variable
    my_name EMP.ENAME%TYPE;  -- Anchored data type
BEGIN
    my_name := 'Malitha'; -- Initialize the variable. This can be done any place in the program
    SELECT ENAME INTO my_name FROM EMP WHERE EMPNO = 7839;  -- Fetch from select query
    DBMS_OUTPUT.PUT_LINE('My name is' || my_name);
END;
/

--PL/SQL conditional statement -------------------------------------------------
--IF THEN
SET SERVEROUTPUT ON;
DECLARE
    v_num NUMBER := &number;
BEGIN
    IF v_num <= 10 THEN
        DBMS_OUTPUT.PUT_LINE('Less than or equal 10');
    ELSIF v_num > 10 AND v_num <=20 THEN
       DBMS_OUTPUT.PUT_LINE('Less than or equal 20 and greater than 10');
    ELSE 
        DBMS_OUTPUT.PUT_LINE('greater than 20 or less than 0');
    END IF;
END;
/

--PL/SQL LOOPS -----------------------------------------------------------------
SET SERVEROUTPUT ON;
DECLARE
    v_count NUMBER := 0;
    v_result NUMBER;
BEGIN
    LOOP
        v_count := v_count + 1;
        v_result := 10 * v_count;
        DBMS_OUTPUT.PUT_LINE( '10 x ' || v_count || ' = ' || v_result );
        EXIT WHEN v_count > 10;
    END LOOP;
END;
/
-- Simple loops ==> LOOP - END LOOP
-- While loops ==> WHILE <BOOLEAN CONDITION> LOOP - END LOOP
-- For loops ==> Ex,

SET SERVEROUTPUT ON;
BEGIN
    FOR v_count IN REVERSE 1 .. 10 LOOP
        DBMS_OUTPUT.PUT_LINE( '10 x ' || v_count || ' = ' || v_count * 10 );
    END LOOP;
END;
/

--PL/SQL Triggers --------------------------------------------------------------
SELECT USER FROM DUAL;
SET SERVEROUTPUT ON;

CREATE OR REPLACE TRIGGER MY_TRIGGER
BEFORE INSERT OR DELETE OR UPDATE ON EMP
FOR EACH ROW
ENABLE
DECLARE
    v_user VARCHAR2(20);
BEGIN
    SELECT USER INTO v_user FROM DUAL;
    IF INSERTING THEN
        DBMS_OUTPUT.PUT_LINE( 'One row inseted by' || v_user );
    ELSIF DELETING THEN
        DBMS_OUTPUT.PUT_LINE( 'One row deleted by' || v_user );
    ELSIF UPDATING THEN
        DBMS_OUTPUT.PUT_LINE( 'One row updated by' || v_user );
    END IF;
END;

--Triggers can be user to monitor the user activity on table ( Security )
--Populate the backup table --CREATE TABLE BACKUP_EMP AS SELECT * FROM EMP WHERE 1=2;
--TODO
/

--TODO Cursers------------------------------------------------------------------




--PL/SQL Functions -------------------------------------------------------------
CREATE OR REPLACE FUNCTION calculate_circle_area( radius NUMBER) RETURN NUMBER
IS
    pi CONSTANT NUMBER (7,2) := 3.14;
    area NUMBER (7,2);
BEGIN
    area := pi* radius * radius;
    RETURN area;
END;
/

SET SERVEROUTPUT ON;
BEGIN
    DBMS_OUTPUT.PUT_LINE( 'Area of the circle is ' || calculate_circle_area( 2 ) );
END;


