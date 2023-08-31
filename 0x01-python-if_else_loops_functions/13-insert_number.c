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

	prev = *head;
	cur = *head;
	new->n = number;
	new->next = NULL;

	if (!head)
		return (NULL);
	if (!(*head))
	{
		(*head) = new;
		return (new);
	}

	while (cur->next)
	{
		if (new->n <= cur->n)
		{
			new->next = cur;
			if (prev != *head)
				prev->next = new;
			else
				prev = new;
			return (new);
		}
		prev = cur;
		cur = cur->next;
	}

	cur->next = new;
	return (new);
}
