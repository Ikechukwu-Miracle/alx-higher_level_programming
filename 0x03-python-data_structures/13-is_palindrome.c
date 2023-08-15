#include "lists.h"
#include <stddef.h>

/**
 * reverse_listint - reverses a singly linked list
 * @head: pointer to the linked list
 *
 * Return: pointer to the head node
 */
listint_t *reverse_list(listint_t **head)
{
        listint_t *prevNode = NULL;
        listint_t *nextNode = NULL;

        while (*head != NULL)
        {
                nextNode = (*head)->next;
                (*head)->next = prevNode;
                prevNode = *head;
                *head = nextNode;
        }
        *head = prevNode;

        return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is palindrome
 * @head: pointer to head of given list
 *
 * Return: 1 if palindrome or 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *revNode, *sec_half, *temp;
	size_t i, x = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	temp = *head;
	while (temp != NULL)
	{
		x++;
		temp = temp->next;
	}

	temp = *head;
	for (i = 0; i < (x / 2) - 1; i++)
		temp = temp->next;
	if (temp->n != temp->next->n && (x % 2) == 0)
		return (0);
	temp = temp->next->next;
	revNode = reverse_list(&temp);
	sec_half = revNode;

	temp = *head;
	while (revNode != NULL)
	{
		if (temp->n != revNode->n)
			return (0);
		temp = temp->next;
		revNode = revNode->next;
	}
	reverse_list(&sec_half);

	return (1);
}
