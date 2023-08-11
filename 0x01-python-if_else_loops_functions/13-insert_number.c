#include "lists.h"

/**
 *insert_node - insert node in sorted linked list
 *
 * @head: head of list
 * @number: item to be sorted
 *
 *Return: return address of new node, NULL on fail
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *cur = NULL;
	listint_t *prev = NULL;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	cur = *head;
	new->n = number;

	while (cur->n)
	{
		cur = cur->next;
		if (new->n > cur->n)
			break;
		prev = cur;
	}

	prev->next = new;
	new->next = cur;

	return (new);
}
