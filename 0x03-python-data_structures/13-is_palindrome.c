#include "lists.h"
#include <stdlib.h>

void reverse_list(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next = NULL;

    while (current)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    *head = prev;
}

int is_palindrome(listint_t **head)
{
    listint_t *fast = *head, *slow = *head, *second_half, *prev_of_slow = *head;
    int is_palindrome = 1;

    if (*head && (*head)->next)
    {
        while (fast && fast->next)
        {
            fast = fast->next->next;
            prev_of_slow = slow;
            slow = slow->next;
        }

        if (fast)
            slow = slow->next;

        second_half = slow;
        prev_of_slow->next = NULL;
        reverse_list(&second_half);

        while (second_half)
        {
            if (prev_of_slow->n != second_half->n)
            {
                is_palindrome = 0;
                break;
            }
            prev_of_slow = prev_of_slow->next;
            second_half = second_half->next;
        }

        reverse_list(&slow);

        if (fast)
            prev_of_slow->next = slow;
        else
            prev_of_slow->next = second_half;
    }

    return is_palindrome;
}
