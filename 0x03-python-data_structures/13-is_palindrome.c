#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - chacks is linked list is palindrome
 * @head: head of list
 * Return: 1 if palindrome, 0 if not
 */

int is_palindrome(listint_t **head)
{
int i, j, k, len = 0;
listint_t *tmp1, *tmp2;

tmp1 = *head;
while (tmp1)
{
tmp1 = tmp1->next;
len++;
}
tmp1 = *head;
tmp2 = *head;
for (i = 0; i < len / 2; i++)
{
for (j = 0; j < i; j++)
tmp1 = tmp1->next;
for (k = 0; k < len - i - 1; k++)
tmp2 = tmp2->next;
if (tmp1->n != tmp2->n)
return (0);
tmp1 = *head;
tmp2 = *head;
}
return (1);
}
