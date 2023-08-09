#include "list.h"

/**
 *check_cycle - cycle tortoise and hare
 * @list: pointer to head
 * Return: 1 on success, 0 otherwise.
 *
 */

int check_cycle(listint_t *list)
{
	listint_t *here, *there;

	here = list;
	there = list;

	if (!here || !there)
		return (0);

	while (there != NULL)
	{
		there = there->next;
		if (there == here)
			return (1);
	}
	return (0);
}
