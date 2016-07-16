#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <stdbool.h>
#include "linkedlist.h"

#define KNRM  "\x1B[0m"
#define KRED  "\x1B[31m"
#define KGRN  "\x1B[32m"
#define KYEL  "\x1B[33m"
#define KBLU  "\x1B[34m"
#define KMAG  "\x1B[35m"
#define KCYN  "\x1B[36m"
#define KWHT  "\x1B[37m"

typedef struct Queue {
    LinkedList *data_list;
    size_t elemsize;
} Queue;

void queue_init(Queue * q, size_t elemsize);
bool queue_enqueue(Queue *q, void * data);
void * queue_dequeue(Queue *q);

typedef struct Animals {
    Queue *general;
    /* cats and dogs are queues of node references */
    Queue *cats;
    Queue *dogs;
} Animals;

typedef struct Animal {
    char *name;
    char specie;
} Animal;

#define CAT 'c'
#define DOG 'd'

void animals_init(Animals * animals);
bool animals_enqueue(Animals * animals, Animal * animal);
Animal * animals_dequeue_any(Animals * animals);
Animal * animals_dequeue_cat(Animals * animals);
Animal * animals_dequeue_dog(Animals * animals);
void print_all_animals(Animals * animals);
void print_all_specie(Animals * animals, char specie);
void print_animal(Animal * animal);

/* People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type) */

int main(int argc, char const *argv[])
{
    Animals animals;
    animals_init(&animals);

    Animal a1, a2, a3, a4;
    a1.name = strdup("Mingau");
    a1.specie = CAT;
    a2.name = strdup("Thor");
    a2.specie = DOG;
    a3.name = strdup("Gertrudez");
    a3.specie = DOG;
    a4.name = strdup("Pretinho");
    a4.specie = CAT;
    animals_enqueue(&animals, &a1);
    animals_enqueue(&animals, &a2);
    animals_enqueue(&animals, &a3);
    animals_enqueue(&animals, &a4);
    print_all_animals(&animals);
    print_all_specie(&animals, DOG);
    print_all_specie(&animals, CAT);

    Animal *a = animals_dequeue_any(&animals);
    printf("%sOP 1 Dequeued any:%s\n", KRED, KNRM);
    print_animal(a);
    print_all_animals(&animals);
    print_all_specie(&animals, DOG);
    print_all_specie(&animals, CAT);
    // free(a);
    a = animals_dequeue_cat(&animals);
    printf("%sOP 2 Dequeued cat: %s\n", KRED, KNRM);
    print_animal(a);
    print_all_animals(&animals);
    print_all_specie(&animals, DOG);
    print_all_specie(&animals, CAT);

    a = animals_dequeue_dog(&animals);
    printf("%sOP 3 Dequeued dog:%s\n", KRED, KNRM);
    print_animal(a);
    print_all_animals(&animals);
    print_all_specie(&animals, DOG);
    print_all_specie(&animals, CAT);


    a = animals_dequeue_dog(&animals);
    printf("%sOP 4 Dequeued dog:%s\n", KRED, KNRM);
    print_animal(a);
    print_all_animals(&animals);
    print_all_specie(&animals, DOG);
    print_all_specie(&animals, CAT);

    return 0;
}

void queue_init(Queue * q, size_t elemsize)
{
    q->data_list = malloc(sizeof(LinkedList));
    list_init(q->data_list, elemsize);
}

bool queue_enqueue(Queue *q, void * data)
{
    return list_append(q->data_list, data);
}

void * queue_dequeue(Queue *q)
{
    return list_pop_tail(q->data_list);
}

void animals_init(Animals * animals)
{
    animals->general = malloc(sizeof(Queue));
    queue_init(animals->general, sizeof(Animal));
    animals->cats = malloc(sizeof(Queue));
    queue_init(animals->cats, sizeof(Node **));
    animals->dogs = malloc(sizeof(Queue));
    queue_init(animals->dogs, sizeof(Node **));
}

bool animals_enqueue(Animals * animals, Animal * animal)
{
    if (animal->specie == DOG || animal->specie == CAT) {
        queue_enqueue(animals->general, animal);
        if (animal->specie == DOG)
            queue_enqueue(animals->dogs, &animals->general->data_list->head);
        else
            queue_enqueue(animals->cats, &animals->general->data_list->head);
        return true;
    }
    return false;
}

Animal * animals_dequeue_any(Animals * animals)
{
    Animal *animal = queue_dequeue(animals->general);
    if (animal) {
        if (animal->specie == DOG)
            queue_dequeue(animals->dogs);
        else
            queue_dequeue(animals->cats);
    }
    return animal;
}

Animal * animals_dequeue_cat(Animals * animals)
{
    Node * animal_ref = queue_dequeue(animals->cats);
    Animal * animal = (Animal *)*(Node **)animal_ref->data;
    if (animal_ref) {
        list_remove_node(animals->general->data_list, *(Node **)animal_ref);
    }

    return animal;
}

Animal * animals_dequeue_dog(Animals * animals)
{
    Node * animal_ref = queue_dequeue(animals->dogs);
    Animal * animal = (Animal *)*(Node **)animal_ref->data;
    if (animal_ref) {
        list_remove_node(animals->general->data_list, *(Node **)animal_ref);
    }

    return animal;
}

void print_all_animals(Animals * animals)
{
    printf("%s###############################%s\n", KRED, KNRM);
    printf("All animals: \n");
    Node *curr = animals->general->data_list->head;
    while (curr) {
        print_animal(curr->data);
        curr = curr->next;
    }
}

void print_all_specie(Animals * animals, char specie)
{
    Node *curr = NULL;
    printf("%s######### START ###############%s\n", KRED, KNRM);
    if (specie == DOG) {
        printf("All dogs:\n");
        curr = animals->dogs->data_list->head;
    }
    else {
        printf("All cats:\n");
        curr = animals->cats->data_list->head;
    }
    // these data are of type (Node **), and the data of *(Node **) is of type (Animal *)
    while (curr) {
        print_animal((*(Node **)curr->data)->data);
        curr = curr->next;
    }
    printf("%s########## END ################%s\n", KRED, KNRM);
}

void print_animal(Animal * animal)
{
    assert(animal);
    printf("%s-  -  -  -  -  -  -  -  -  -  -%s\n", KBLU, KNRM);
    printf("Name: %s\n", animal->name);
    if (animal->specie == DOG)
        printf("Specie: Dog\n");
    else
        printf("Specie: Cat\n");
}