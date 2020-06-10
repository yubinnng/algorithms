//
// 无向图（邻接表）
// Created by 齐语冰 on 2018/12/24.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_VERTEX_NUM 20

typedef struct ArcNode {
     int adjVex;
     struct ArcNode *nextArc;
     int info;
} ArcNode;

typedef struct VNode {
     char data;
     ArcNode *firstArc;
} VNode, AdjList[MAX_VERTEX_NUM];

typedef struct {
     AdjList vertices;
     int vexNum, arcNum;
     char kind[10];
} ALGraph;

// 清空缓冲区用
char lastedStr[20];

/**
 * 在链表末端添加一个节点
 * @param graph 图
 * @param vexIndex 当前顶点的数组下标
 * @param adjVex 指向顶点位置
 * @param info 该路径的权值
 */
void addArcNode(ALGraph *graph, int vexIndex, int adjVex, int info) {
    VNode *vNode = &graph->vertices[vexIndex];
    ArcNode *nowPtr = vNode->firstArc;
    if (!nowPtr) {
         ArcNode *arcNode = (ArcNode *) malloc(sizeof(arcNode));
         arcNode->adjVex = adjVex;
         arcNode->info = info;
         arcNode->nextArc = NULL;
         vNode->firstArc = arcNode;
    } else {
         while (nowPtr->nextArc) {
             nowPtr = nowPtr->nextArc;
         }
         ArcNode *arcNode = (ArcNode *) malloc(sizeof(arcNode));
         arcNode->adjVex = adjVex;
         arcNode->info = info;
         arcNode->nextArc = NULL;
         nowPtr->nextArc = arcNode;
    }
}

/**
 * 创建一个无向图
 * @return 无向图
 */
ALGraph createUDG() {
    ALGraph graph = *(ALGraph *) malloc(sizeof(ALGraph));
    strcpy(graph.kind, "UDG");
    printf("请输入顶点个数：");
    scanf("%d", &graph.vexNum);
    gets(lastedStr);
    for (int i = 0; i < graph.vexNum; ++i) {
         graph.vertices[i].firstArc = NULL;
         printf("请输入顶点V%d的信息：", i + 1);
         scanf("%c", &graph.vertices[i].data);
         gets(lastedStr);
         char string[50];
         for (int j = 0; j < 50; ++j) {
             int adjVex;
             int info;
             printf("请输入顶点V%d的第%d个邻接点和对应路径权值(形式如：'邻接点编号,路径权值')(输入q退出)：", i + 1, j + 1);
             scanf("%s", string);
             gets(lastedStr);
             if (strcmp(string, "q") == 0) {
                 break;
             }
             char *temp = strtok(string, ",");
             for (int k = 0; k < 2; ++k) {
                 if (k == 0) {
                     adjVex = atoi(temp) - 1;
                 } else {
                     info = atoi(temp);
                 }
                 temp = strtok(NULL, ",");
             }
             addArcNode(&graph, i, adjVex, info);
             graph.arcNum++;
         }
    }
    return graph;
}

/**
 * 计算连通分量个数
 * @param graph 邻接表
 * @return 连通分量个数
 */
int count(ALGraph *graph) {
    int num = 0;
    int visited[50];
    for (int i = 0; i < graph->vexNum; ++i) {
         if (visited[i] != 1) {
             num++;
         }
         visited[i] = 1;
         ArcNode *nowPtr = graph->vertices[i].firstArc;
         while (nowPtr) {
             visited[nowPtr->adjVex] = 1;
             nowPtr = nowPtr->nextArc;
         }
    }
    return num;
}

int main(void) {
     setvbuf(stdout, NULL, _IONBF, 0);
     ALGraph graph = createUDG();
     int num = count(&graph);
     printf("该无向图的连通分量个数为：%d", num);
}