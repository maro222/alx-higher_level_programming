#include "lists.h"

/**
 *check_cycle - cycle tortoise and hare
 * @list: pointer to head
 * Return: 1 on success, 0 otherwise.
 *
 */

int check_cycle(listint_t *list)
{
	listint_t *here, *there;

	if (!list)
		return (0);

	here = list;
	there = list;

	while (there->next != NULL)
	{
		there = there->next;
		if (there == here)
			return (1);
	}
	return (0);
}
