package cn.qiyubing.deliver;

import cn.qiyubing.util.FileUtils;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * 贪心法旅行商问题
 *
 * @author qiyubing
 * @since 2019-07-03
 */
public class Tsp {

    /**
     * 示例内容：
     * 4 5
     * 1 2
     * 1 3
     * 1 4
     * 2 4
     * 3 4
     */
    private static final String FILE_PATH = "";

    /**
     * 图的邻接矩阵
     */
    private static int[][] graph;

    /**
     * 节点数
     */
    private static int nodeNum;

    /**
     * 边数
     */
    private static int edgeNum;

    /**
     * 路径开始节点
     */
    private final static int INIT_NODE = 0;

    /**
     * 移动路径
     */
    private static List<Integer> path = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        init();
        printGraph();
        // 设置并输出首个节点
        int targetNode = INIT_NODE;
        path.add(targetNode);
        // 移动edgeNum次
        for (int i = 0; i < edgeNum; i++) {
            targetNode = move(targetNode);
        }
        if (checkAllPassed()) {
            printPath();
        } else {
            System.out.println(-1);
        }
    }

    /**
     * 初始化邻接矩阵
     */
    private static void init() throws IOException {
        List<String> lines = FileUtils.readAllLine(FILE_PATH);
        nodeNum = lines.get(0).charAt(0) - '0';
        edgeNum = lines.get(0).charAt(2) - '0';

        graph = new int[nodeNum][nodeNum];

        for (int i = 0; i < edgeNum; i++) {
            int node1 = lines.get(i + 1).charAt(0) - '0' - 1;
            int node2 = lines.get(i + 1).charAt(2) - '0' - 1;
            // 设置两节点的边
            graph[node1][node2] = 1;
            graph[node2][node1] = 1;
        }
    }

    /**
     * 移动到下一个节点
     *
     * @param sourceNode 源节点
     * @return 移动后的目标节点
     */
    private static int move(int sourceNode) {
        // 相邻的节点
        int[] neighborNodes = graph[sourceNode];

        // 可用节点中选取权值最小的节点作为目标节点
        int targetNode = Integer.MAX_VALUE;
        for (int i = 0; i < nodeNum; i++) {
            if (neighborNodes[i] == 1 && !checkPassed(sourceNode, i) && i < targetNode) {
                targetNode = i;
            }
        }
        path.add(targetNode);
        return targetNode;
    }

    /**
     * 查看node1和node2构成的边是否已经过
     */
    private static boolean checkPassed(int node1, int node2) {
        for (int i = 0; i < path.size(); i++) {
            boolean isNext = path.get(i) == node1 && (i + 1 < path.size() && path.get(i + 1) == node2);
            boolean isBefore = path.get(i) == node1 && (i - 1 >= 0 && path.get(i - 1) == node2);
            if (isNext || isBefore) {
                return true;
            }
        }
        return false;
    }

    /**
     * 判断是否经过全部的边
     */
    private static boolean checkAllPassed() {
        for (int i = 0; i < nodeNum; i++) {
            for (int j = 0; j < nodeNum; j++) {
                if (graph[i][j] == 1 && !checkPassed(i, j)) {
                    return false;
                }
            }
        }
        return true;
    }

    /**
     * 输出移动路径
     */
    private static void printPath() {
        System.out.print("移动路径：");
        for (int node : path) {
            System.out.print((node + 1) + " ");
        }
    }

    /**
     * 输出邻接矩阵：
     */
    private static void printGraph() {
        System.out.println("邻接矩阵：");
        for (int i = 0; i < nodeNum; i++) {
            for (int j = 0; j < nodeNum; j++) {
                System.out.print(graph[i][j] + " ");
            }
            System.out.println();
        }
    }
}
