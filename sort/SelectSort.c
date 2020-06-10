//
// 选择排序
// Created by 齐语冰 on 2019/1/2.
//

#include <stdio.h>
#include <stdlib.h>
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
 * 获取从链表头结点开始元素值最小的节点
 * @param linkList 链表
 * @return 节点
 */
LNode *getMin(LinkList linkList) {
    // 头结点的下一位
    LNode *min = linkList->next;
    LNode *nowPtr = linkList->next;
    while (nowPtr) {
        if (nowPtr->data < min->data) {
            min = nowPtr;
        }
        nowPtr = nowPtr->next;
    }
    return min;
}

/**
 * 链表的直接选择排序
 * @param linkList 待排序的链表
 */
void selectSort(LinkList linkList) {
    if (linkList->next) {
        LNode * min = getMin(linkList);
        int temp = linkList->next->data;
        linkList->next->data = min->data;
        min->data = temp;
        // r 之后的元素未排序，之前的元素已排序
        selectSort(linkList->next);
    } else {
        return;
    }
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

int main(void) {
    LinkList linkList = create();
    printf("原链表各元素:");
    print(linkList);
    selectSort(linkList);
    printf("排序后链表各元素:");
    print(linkList);
    return 0;
}