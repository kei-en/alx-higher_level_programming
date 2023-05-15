#include "lists.h"

listint_t *rev_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * rev_listint - Reverses a singly_linked list (listint_t)
 * @head: pointer to the beginning of the list
 *
 * Return: pointer to the head of the reversed list (success)
*/
listint_t *rev_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly-linked list is a palindrome
 * @head: pointer to the head of the list
 *
 * Return: 0 (not a palindrome, 1 (is a palindrome)
*/
int is_palindrome(listint_t **head)
{
	listint_t *temp, *reverse, *middle;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}

	temp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		temp = temp->next;

	temp = temp->next->next;
	reverse = rev_listint(&temp);
	middle = reverse;

	temp = *head;
	while (reverse)
	{
		if (temp->n != reverse->n)
			return (0);
		temp = temp->next;
		reverse = reverse->next;
	}
	rev_listint(&middle);
	return (1);
}
