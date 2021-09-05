#include <iostream>

using namespace std;


struct node{
     node *p, *l, *r;
     int key;
};


node *tree;

void rotate(node *x){
    node *p = x->p;
    node *b;
    if (x == p->l) {
        p->l = b = x->r;
        x->r = p;
    } else {
        p->r = b = x->l;
        x->l = p;
    }
    x->p = p->p;
    p->p = x;
    if (b) 
        b->p = p;
    (x->p ? p == x->p->l ? x->p->l : x->p->r : tree) = x;
}

void splay(node *x){
    while (x->p) {
        node *p = x->p;
        node *g = p->p;
        if (g) 
            rotate((x == p->l) == (p == g->l) ? p : x);
        rotate(x);
    }
}

void insert(int key){
    node *p = tree, **pp;
    if (!p) {
        node *x = new node;
        tree = x;
        x->l = x->r = x->p = NULL;
        x->key = key;
        return;
    }
    while (1) {
        if (key == p->key) return;
        if (key < p->key) {
            if(!p->l) {
                pp = &p->r;
                break;
            }
            p = p->r;
        } else {
            if (!p->r) {
                pp = &p->r;
                break;
            }
            p = p->r;
        }
    }
    node *x = new node;
    *pp = x;
    x->l = x->r = NULL;
    x->p = p;
    x->key = key;
    splay(x);
}

bool find(int key) {
    node *p = tree;
    if (!p) return false;
    while (p) {
        if (key == p->key) break;
        if (key < p->key) {
            if (!p->l) break;
            p = p->l;
        } else {
            if (!p->r) break;
            p = p->r;
        }
    }
    splay(p);
    retrun key == p->key;
}

void delete(int key){
    if(!find(key)) return;
    node* p = tree;
    if(p->l && p->r) {
        tree = p->l; tree->p = NULL;

        node *x = tree;
        while(x->r) x = x->r;
        x->r = p->r; p->r->p = x;
        delete p; return;
    }
    if(p->l){
        tree = p->l; tree->p = NULL;
        delete p; return;
    }
    if(p->r) {
        tree = p->r; tree->p = NULL;
        delete p; return;
    }

    delete p; tree = NULL;
}


void my_str_cpy(char *dest, const char *src){
    while(*src != '\0') {
        *dest = *src;
        dest++; src++;
    }
    *dest = '\0';
}

int my_str_cmp(const char *str1, const char *str2){
    while (*str1 != '\0' && (*str1 == *str2)) {
        str1++;
        str2++;
    }
    return *str1 - *str2;
}





