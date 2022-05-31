#include "lists.h"

/**
 * insert_node - insert node in an ordered linked list
 * @head: the list passed in
 * @number: value of the new node
 * Return: address of new node or NULL if failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *future;

	future = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (future->next != NULL)
	{
		if ((future->next)->n >= number)
		{
			new->next = future->next;
			future->next = new;
			return (new);
		}
		future = future->next;
	}
	future->next = new;
	new->next = NULL;
	return (new);
}
