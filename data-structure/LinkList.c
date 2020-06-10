//
// 链表
// Created by 齐语冰 on 2018/11/14.
//

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct LNode {
    int data;
    struct LNode *next;
} LNode, *LinkList;

/**
 * 创建链表
 * @return 带头节点的链表
 */
LinkList create() {
    //建立头节点
    LinkList linkList = (LinkList) malloc(sizeof(LNode));
    LNode *lastPtr = linkList;

    char string[50];
    printf("请输入数列（用英文逗号隔开各元素）：");
    gets(string);
    // 将字符串分割并转为整型数组
    char *temp = strtok(string, ",");
    while (temp) {
        LNode *newNode = (LNode *) malloc(sizeof(LNode));
        newNode->data = atoi(temp);
        lastPtr->next = newNode;
        lastPtr = newNode;
        temp = strtok(NULL, ",");
    }
    return linkList;
}

/**
 * 输出链表各元素
 * @param linkList
 */
void print(LinkList linkList) {
    LNode *nowPtr = linkList->next;
    printf("[");
    while (nowPtr) {
        printf("%d,", nowPtr->data);
        nowPtr = nowPtr->next;
    }
    printf("]\n");
}

/**
 * 在节点后添加新节点
 * @param head 头结点
 * @param value 新节点元素值
 */
void insertToNext(LNode *head, int value) {
    LNode *newNode = (LinkList) malloc(sizeof(LNode));
    newNode->data = value;
    newNode->next = head->next;
    head->next = newNode;
}

/**
 * 在顺序链表中插入新元素仍保持顺序
 * @param linkList 链表
 * @param value 插入元素值
 */
void insert(LinkList linkList, int value) {
    LNode *head = linkList;
    while (head->next) {
        if (value <= head->next->data) {
            insertToNext(head, value);
            return;
        }
        head = head->next;
    }
    insertToNext(head, value);
}

int main(void) {
    // 创建一个链表
    LinkList linkList = create();

    // 查看数组当前元素
    printf("当前数组: ");
    print(linkList);

    int insertNum;
    printf("请输入要插入的元素: ");
    scanf("%d", &insertNum);

    insert(linkList, insertNum);

    printf("插入后的数组:");
    // 查看数组当前元素
    print(linkList);

    return 0;
}
