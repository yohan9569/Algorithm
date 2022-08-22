-- Binary Tree Nodes


/*   WHEN N NOT IN (SELECT P FROM BST) THEN 'Leaf' -> Why doesn't this work?

SQL uses three-value logic, for which the three possible values of a logical expression are true, false or unknown. 
Comparison of a value to a NULL is unknown and if any one of those NOT IN comparisons is unknown then the result is also deemed to be unknown.

- https://stackoverflow.com/questions/16038414/and-field-not-innull-returns-an-empty-set   */


SELECT N,
    CASE
        WHEN P IS NULL THEN 'Root'
        WHEN N IN (SELECT P FROM BST) THEN 'Inner'
        ELSE 'Leaf'
    END
FROM BST
ORDER BY N;
