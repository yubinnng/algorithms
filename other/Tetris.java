package cn.qiyubing.tetris;

import cn.qiyubing.util.FileUtils;

import java.io.IOException;
import java.util.List;

/**
 * 俄罗斯方块
 *
 * @author qiyubing
 * @since 2019-06-10
 */
public class Tetris {

    /**
     * 示例内容：
     * 从上到下顺序为：画布、下落块、水平位置（左）
     * 0 0 0 0 0 0 0 0 0 0
     * 0 0 0 0 0 0 0 0 0 0
     * 0 0 0 0 0 0 0 0 0 0
     * 0 0 0 0 0 0 0 0 0 0
     * 0 0 0 0 0 0 0 0 0 0
     * 0 0 0 0 0 0 0 0 0 0
     * 0 0 0 0 0 0 0 0 0 0
     * 0 0 0 0 0 0 0 0 0 0
     * 0 0 0 0 0 0 0 0 0 0
     * 0 0 0 0 0 0 0 0 0 0
     * 0 0 0 0 0 0 0 1 0 0
     * 0 0 0 0 0 0 1 0 0 0
     * 0 0 0 0 0 0 1 0 0 0
     * 1 1 1 0 0 0 1 1 1 1
     * 0 0 0 0 0 0 0 0 0 0
     * 0 0 0 0
     * 0 1 1 1
     * 0 0 0 1
     * 0 0 0 0
     * 3
     */
    private static final String FILE_PATH = "";

    private static final int CANVAS_ROW = 15;
    private static final int CANVAS_COL = 10;

    private static final int BLOCK_ROW = 4;
    private static final int BLOCK_COL = 4;

    /**
     * 画布图层
     */
    private static String[][] canvas = new String[CANVAS_ROW][CANVAS_COL];

    /**
     * 下落块图层
     */
    private static String[][] block = new String[CANVAS_ROW][CANVAS_COL];

    public static void main(String[] args) throws IOException {
        init();

        System.out.println("初始：");
        print();

        while (canMoveDown()) {
            moveDown();
            System.out.println("移动：");
            print();
        }
    }

    /**
     * 初始化图册
     */
    private static void init() throws IOException {
        List<String> inputLines = FileUtils.readAllLine(FILE_PATH);

        // 初始化画布图层
        for (int i = 0; i < CANVAS_ROW; i++) {
            String[] e = inputLines.get(i).split(" ");
            System.arraycopy(e, 0, canvas[i], 0, CANVAS_COL);
        }

        // 初始化下落块图层
        for (int i = 0; i < CANVAS_ROW; i++) {
            for (int j = 0; j < CANVAS_COL; j++) {
                block[i][j] = "0";
            }
        }

        // 初始化左位置
        int left = Integer.parseInt(inputLines.get(19));

        // 初始化下落块
        Integer topOffset = null;
        Integer leftOffset = null;
        for (int i = 0; i < BLOCK_ROW; i++) {
            String[] e = inputLines.get(CANVAS_ROW + i).split(" ");
            for (int j = 0; j < BLOCK_COL; j++) {
                if ("1".equals(e[j])) {
                    if (topOffset == null) {
                        topOffset = i;
                        leftOffset = j;
                    }
                    block[i - topOffset][j + left - leftOffset] = e[j];
                }
            }
        }
    }

    /**
     * 将画布和下落块合并输出
     */
    private static void print() {
        for (int i = 0; i < CANVAS_ROW; i++) {
            for (int j = 0; j < CANVAS_COL; j++) {
                if ("1".equals(block[i][j])) {
                    System.out.print(block[i][j] + " ");
                } else {
                    System.out.print(canvas[i][j] + " ");
                }
            }
            System.out.println();
        }
    }

    /**
     * 判断能否向下移动
     */
    private static boolean canMoveDown() {
        for (int i = 0; i < CANVAS_ROW; i++) {
            for (int j = 0; j < CANVAS_COL; j++) {
                // 触底
                boolean isEnd = "1".equals(block[i][j]) && i == CANVAS_ROW - 1;
                if (isEnd) {
                    return false;
                }
                // 下落阻塞
                boolean canNotMoveDown = "1".equals(block[i][j]) && "1".equals(canvas[i + 1][j]);
                if (canNotMoveDown) {
                    return false;
                }
            }
        }
        return true;
    }

    /**
     * 将下落块向下移动
     */
    private static void moveDown() {
        for (int i = CANVAS_ROW - 1; i > 0; i--) {
            for (int j = CANVAS_COL - 1; j >= 0; j--) {
                if ("1".equals(block[i - 1][j])) {
                    block[i - 1][j] = "0";
                    block[i][j] = "1";
                }
            }
        }
    }
}
