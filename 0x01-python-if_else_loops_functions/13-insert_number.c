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

	if (!head)
	{
		*head = new;
		new->next = NULL;
	}

	while (cur->next)
	{
		if (new->n < cur->n)
			break;
		prev = cur;
		cur = cur->next;
	}

	prev->next = new;
	new->next = cur;

	return (new);
}
