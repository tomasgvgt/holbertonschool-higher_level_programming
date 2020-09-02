#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - insterts a number into a sorted linked list.
 * @head: head of linked list.
 * @number: integer.
 * Return: pointer to the new node.
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *tmp1 = *head;
listint_t *new;

if (!head)
return (NULL);
new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);

new->n = number;
new->next = NULL;

if (tmp1 == NULL)
{
tmp1 = new;
return (new);
}

while (tmp1->next && tmp1->next-n < number)
{
tmp1 = tmp1->next;
}
new->next = tmp1->next;
tmp1->next = new;
return (new);
}
