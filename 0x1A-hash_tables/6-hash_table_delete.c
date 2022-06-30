#include <stdio.h>
#include "hash_tables.h"
/**
 *hash_table_delete - deletes a hash table.
 *@ht:Hash table.
 *Return: Nothing.
 */

void hash_table_delete(hash_table_t *ht)
{
	unsigned long int i;
	hash_node_t *tmp, *holder;

	if (ht == NULL)
		return;
	for (i = 0; i < ht->size; i++)
	{
		if (ht->array[i] != NULL)
		{
			tmp = ht->array[i];
			while (tmp != NULL)
			{
				holder = tmp;
				tmp = tmp->next;
				free(holder->key);
				free(holder->value);
				free(holder);
			}
		}
	}
	free(ht->array);
	free(ht);
}
