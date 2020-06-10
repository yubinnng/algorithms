//
// 二分查找
// Created by 齐语冰 on 2018/12/5.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct SSTable {
    int elem[20];
    int length;
} SSTable;

/**
 * 创建静态搜索表
 * @return 静态搜索表
 */
SSTable createSSTable() {
    SSTable ssTable = *(SSTable *) malloc(sizeof(SSTable));
    int length = 0;
    char string[50];
    printf("请输入有序数列（用英文逗号隔开各元素）：");
    gets(string);
    // 将字符串分割并转为整型数组
    char *temp = strtok(string, ",");
    while (temp) {
        ssTable.elem[length] = atoi(temp);
        temp = strtok(NULL, ",");
        length++;
    }
    ssTable.length = length;
    return ssTable;
}

/**
 * 二分查找
 * @param s 静态查找表
 * @param low 最低位
 * @param high 最高位
 * @param key 查找元素
 * @return 元素位置
 */
int binarySearch(SSTable ssTable, int low, int high, int key) {
    int mid = (low + high) / 2;
    if (high >= low) {
        if (key == ssTable.elem[mid]) {
            return mid;
        } else if (key < ssTable.elem[mid]) {
            return binarySearch(ssTable, low, mid - 1, key);
        } else {
            return binarySearch(ssTable, mid + 1, high, key);
        }
    } else {
        return -1;
    }
}

int main(void) {
    int key;
    SSTable ssTable = createSSTable();
    printf("请输入要查找的元素值：");
    scanf("%d", &key);
    int index = binarySearch(ssTable, 0, ssTable.length, key);
    if (index == -1) {
        printf("无此元素！");
    } else {
        printf("元素 %d 在有序数列中的下标为：%d", key, index);
    }
}
