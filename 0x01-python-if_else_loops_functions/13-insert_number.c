#include <stddef.h>
#include <stdlib.h>
#include "lists.h"

int main(void)
{
    listint_t *head;

    head = NULL;
    print_listint(head);

    printf("-----------------\n");

    insert_node(&head, 27);

    print_listint(head);

    free_listint(head);

    return (0);
}
