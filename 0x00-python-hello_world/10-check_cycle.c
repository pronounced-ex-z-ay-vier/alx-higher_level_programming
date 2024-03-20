#include "lists.h"

/**
 * check_cycle - check for loop cycle in Linked list
 * @list: head of linked list
 * Return: If cycle is true return 1, return 0 if false
 */

int check_cycle(listint_t *list)
{
	listint_t *former, *latter;

	if (!list)
	{
		return (0);
	}
	former = list;
	latter = list->next;
	while (latter && former && latter->next)
	{
		if (former == latter)
		{
			return (1);
		}
		former = former->next;
		latter = latter->next->next;
	}
	return (0);
}
