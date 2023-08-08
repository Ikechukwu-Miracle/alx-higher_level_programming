#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - inserts a number in a sorted singly linked list
 * @head: pointer to pointer of list
 * @number: number to be inserted
 *
 * Return: pointer to the newNode or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode, *currNode = *head;

	newNode = malloc(sizeof(listint_t));

	if (!newNode)
		return (NULL);
	newNode->n = number;

	if (!currNode || currNode->n >= number)
	{
		newNode->next = currNode;
		*head = newNode;
		return (newNode);
	}

	while (currNode && currNode->next && currNode->next->n < number)
		currNode = currNode->next;

	newNode->next = currNode->next;
	currNode->next = newNode;

	return (newNode);

}
