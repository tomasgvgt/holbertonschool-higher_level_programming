#include "lists.h"

/**
 * check_cycle - Checks if there is a loop in a linked list.
 * @list: head of a listint_t list.
 * Return: 0 if no loop, 1 if loop.
 */

int check_cycle(listint_t *list)
{
	listint_t *tmp = list;
	listint_t *tmp1 = list;

	while (tmp && tmp1 && tmp1->next)
	{
		tmp = tmp->next;
		tmp1 = tmp1->next->next;
		if (tmp == tmp1)
			return (1);
	}
	return (0);
}
