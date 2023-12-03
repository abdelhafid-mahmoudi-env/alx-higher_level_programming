#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the list
 *
 * Return: pointer to the new head of the list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *current = head, *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
 * compare_lists - compares two lists
 * @head1: pointer to the head of the first list
 * @head2: pointer to the head of the second list
 *
 * Return: 1 if lists are the same, 0 otherwise
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
	listint_t *temp1 = head1, *temp2 = head2;

	while (temp1 && temp2)
	{
		if (temp1->n != temp2->n)
			return (0);
		temp1 = temp1->next;
		temp2 = temp2->next;
	}
	return (temp1 == NULL && temp2 == NULL);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 *
 * Return: 1 if it is a palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head;
	listint_t *midnode = NULL, *second_half, *prev_slow = *head;
	int res = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}
		if (fast != NULL)
		{
			midnode = slow;
			slow = slow->next;
		}
		second_half = slow;
		prev_slow->next = NULL;
		second_half = reverse_list(second_half);
		res = compare_lists(*head, second_half);
		second_half = reverse_list(second_half);
		if (midnode != NULL)
		{
			prev_slow->next = midnode;
			midnode->next = second_half;
		}
		else
			prev_slow->next = second_half;
	}
	return (res);
}
