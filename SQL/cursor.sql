--Oracle Cursor
/*
Cursor is a pointer to a memory area called context area inside the Process Global Area (PGA)
1. Implicit Cursors ( When execute the DML statements server will create automatically )
2. Explicit Cursors

Declare - Open - Fetch - Close

*/

SET SERVEROUTPUT ON

DECLARE
    emp_name emp.ename%TYPE;
    
    -- Without parameter
    CURSOR get_emp_name IS
    SELECT ename FROM emp WHERE empno < 7900;
    
    -- With a parameter
    CURSOR get_emp_name_by_id( emp_id IN emp.empno%TYPE := 7000 ) IS
    SELECT ename FROM emp WHERE empno = emp_id;
    
BEGIN

    OPEN get_emp_name;
    FETCH get_emp_name INTO emp_name;
    -- Simple loop
    LOOP
        FETCH get_emp_name INTO emp_name;
        DBMS_OUTPUT.PUT_LINE( emp_name );
        EXIT WHEN get_emp_name%NOTFOUND;
    END LOOP;
    CLOSE get_emp_name;
    
    DBMS_OUTPUT.PUT_LINE( '--------------------------------------' );
    OPEN get_emp_name_by_id( 7839 );
    FETCH get_emp_name_by_id INTO emp_name;
    CLOSE get_emp_name_by_id;
    DBMS_OUTPUT.PUT_LINE( emp_name );
    
    DBMS_OUTPUT.PUT_LINE( '--------------------------------------' );
    -- For loop with implicit cursor
    FOR get_emp_name_list IN ( SELECT ename FROM emp WHERE empno = 7839 )
    LOOP
        DBMS_OUTPUT.PUT_LINE( get_emp_name_list.ename );
    END LOOP;
    
    DBMS_OUTPUT.PUT_LINE( '--------------------------------------' );
    -- For loop with cursor calling
    FOR get_emp_name_list IN get_emp_name_by_id( 7839 )
    LOOP
        DBMS_OUTPUT.PUT_LINE( get_emp_name_list.ename );
    END LOOP;
    
    // Use  the record data type (<Cursor_name>%ROWTYPE) as same as above %TYPE after defining the cursor
    // When there are two or more tables involve in the select query, then we can not use implicit record type. Therefore,
    // we need to use user defined records.
       TYPE emp_data IS RECORD( variable name with data type );
       var_emp_data emp_data%ROWTYPE
		
END;
/

