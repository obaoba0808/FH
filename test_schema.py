# -*- coding: utf-8 -*-
import fix4
schema = fix4.get_special_schema()
print('Schema first 200 chars:')
print(repr(schema[:200]))
print('Has dateModified:', 'dateModified' in schema)
print('Has </script>:', '</script>' in schema)
print('Total len:', len(schema))
