#include "lists.h"
#include <stdlib.h>

/**
  * check_cycle - checks if a singly linked list has a cycle in it
  * @list: singly linked list
  *
  * Return: 0 no cycle, 1 there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fox, *crow;

	if (list == NULL || list->next == NULL)
		return (0);

	fox = list->next;
	crow = list->next->next;

	while (fox && crow && crow->next)
	{
		if (fox == crow)
			return (1);

		fox = fox->next;
		crow = crow->next->next;
	}

	return (0);
}
