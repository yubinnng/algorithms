//
// 二叉树
// Created by 齐语冰 on 2018/12/19.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct BiNode {
    char data;
    struct BiNode *lChild, *rChild;
} BiNode, *BiTree;

/**
 * 初始化二叉树
 * @param idxPtr 存放当前数组位置的指针
 * @param chars 初始化数组
 * @return 二叉树
 */
BiTree initBiTree(int *idxPtr, char chars[], int length) {
    char now = chars[*idxPtr];
    *idxPtr = *idxPtr + 1;
    if (now == ' ' || *idxPtr > length) {
        return NULL;
    } else {
        BiTree biTree = (BiTree) malloc(sizeof(BiNode));
        biTree->data = now;
        biTree->lChild = initBiTree(idxPtr, chars, length);
        biTree->rChild = initBiTree(idxPtr, chars, length);
        return biTree;
    }
}

/**
 * 创建二叉树
 * @return 二叉树
 */
BiTree createBiTree() {
    printf("按先序次序输入二叉树中节点的值（一个字符），空格字符表示空树:\n");
    char chars[100];
    gets(chars);
    int length = (int) strlen(chars);
    int idx = 0;
    int *idxPtr = &idx;
    return initBiTree(idxPtr, chars, length);
}

/**
 * 打印二叉树
 * @param biTree 二叉树
 * @param level 当前级数，0开始
 */
void printBiTree(BiTree biTree, int level) {
    for (int i = 0; i < level; ++i) {
        printf("   ");
    }
    level++;

    if (biTree) {
        // 先序遍历
        printf("|—— %c\n", biTree->data);
        printBiTree(biTree->lChild, level);
        printBiTree(biTree->rChild, level);
    } else {
        printf("|—— Λ\n");
    }
}

/**
 * 计算叶子节点个数
 * @param biTree 二叉树
 * @return 叶子节点个数
 */
int countLeaf(BiTree biTree) {
    int leafNum = 0;
    if (biTree) {
        if (biTree->lChild == NULL && biTree->rChild == NULL) {
            leafNum++;
        }
        leafNum += countLeaf(biTree->lChild);
        leafNum += countLeaf(biTree->rChild);
    }
    return leafNum;
}

int main(void) {
    BiTree biTree = createBiTree();
    printf("二叉树初始化完成!\n");

    printf("当前二叉树为：\n");
    printBiTree(biTree, 0);

    int leafNum = countLeaf(biTree);
    printf("叶子节点个数为：%d", leafNum);

    return 0;
}