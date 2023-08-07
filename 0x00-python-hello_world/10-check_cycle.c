#include "lists.h"

/**
 * check_cycle - checks for cycle in the singly linked list
 * @list: pointer to the linked list
 *
 * Return: 0 if no cycle and 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *hare = list;
	listint_t *tortoise = list;

	if (list == NULL)
		return (0);

	while (hare && tortoise && hare->next)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}
	return (0);
}
