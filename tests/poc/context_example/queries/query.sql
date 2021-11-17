/*skip-formatter*/
SELECT *
FROM   poc.examples_entity
WHERE  id = {{ id }}
   {% if name %}
   and name ilike {{ name }}
   {% endif %}
