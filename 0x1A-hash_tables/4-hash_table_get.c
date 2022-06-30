#include "hash_tables.h"
#include "string.h"
/**
 *hash_table_get - Retrieves a value associated with a key.
 *@ht:The hash table to look into.
 *@key: Key for which to retrieve the value.
 *
 *Return:Value associated with the key, NULL if key not found.
 */

char *hash_table_get(const hash_table_t *ht, const char *key)
{
	unsigned long int index;
	hash_node_t *tmp;

	if (ht == NULL || key == NULL)
	{
		return (NULL);
	}
	index = key_index((const unsigned char *)key, ht->size);
	if (index >= ht->size)
		return (NULL);
	tmp = (ht->array[index]);
	if (tmp == NULL)
	{
		return (NULL);
	}
	else
	{

		while (strcmp(strdup(key), tmp->key) != 0)
			tmp = tmp->next;
		if (tmp == NULL)
			return (NULL);
		else
			return (tmp->value);
	}
}
