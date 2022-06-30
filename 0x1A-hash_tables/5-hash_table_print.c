#include <stdio.h>
#include "hash_tables.h"
/**
 *hash_table_print - Prints a hash table.
 *@ht:Hash table.
 *Return: Nothing.
 */

void hash_table_print(const hash_table_t *ht)
{
	hash_node_t *tmp;
	char *delimeter = "";
	unsigned long int i;

	if (ht == NULL)
		return;
	printf("{");
	for (i = 0; i < ht->size; i++)
	{
		if (ht->array[i] != NULL)
		{
			tmp = ht->array[i];
			while (tmp != NULL)
			{
				printf("%s\'%s\': \'%s\'", delimeter, tmp->key, tmp->value);
				delimeter = ", ";
				tmp = tmp->next;
			}
		}
	}
	printf("}\n");
}
