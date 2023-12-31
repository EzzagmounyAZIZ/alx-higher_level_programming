#include<stdio.h>
#include<stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the list
 * Return: 1 if there is a cycle, 0 if there is no cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *tortoise = list;
	listint_t *hare = list;

	if (list == NULL)
		return (0);

	while (hare != NULL && hare->next != NULL)
	{
		tortoise = tortoise->next;
		hare = hare->next->next;
		if (tortoise == hare)
			return (1);
	}

	return (0);
}
