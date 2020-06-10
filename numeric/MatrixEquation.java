package cn.qiyubing;

/**
 * 求解矩阵方程
 *
 * @author qiyubing
 * @since 2019-03-26
 */
public class MatrixEquation {

    /**
     * 初始增广矩阵
     */
    private static double[][] matrix1 = {
            {1, 2, 3, 14},
            {0, 1, 2, 8},
            {2, 4, 1, 13}
    };

    public static void main(String[] args) {
        // 高斯消元
        for (int mainRow = 0; mainRow < matrix1.length - 1; mainRow++) {
            for (int nowRow = mainRow + 1; nowRow < matrix1.length; nowRow++) {
                double ratio = (matrix1[nowRow][mainRow] / matrix1[mainRow][mainRow]);
                for (int nowCol = mainRow; nowCol < matrix1[nowRow].length; nowCol++) {
                    matrix1[nowRow][nowCol] -= ratio * matrix1[mainRow][nowCol];
                }
            }
        }
        System.out.println("高斯消元结果为：");
        for (double[] nowRow : matrix1) {
            for (double nowElem : nowRow) {
                System.out.print(nowElem + " ");
            }
            System.out.println();
        }

        // 回代解x1 x2 x3...
        double[] xArray = new double[matrix1.length];
        for (int nowRow = matrix1.length - 1; nowRow >= 0; nowRow--) {
            // ax = right
            double right = matrix1[nowRow][matrix1[nowRow].length - 1];
            for (int j = nowRow + 1; j < matrix1[nowRow].length - 1; j++) {
                right -= matrix1[nowRow][j] * xArray[j];
            }
            xArray[nowRow] = right / matrix1[nowRow][nowRow];
        }
        System.out.println("回代得：");
        for (int i = 0; i < xArray.length; i++) {
            System.out.println("x" + (i + 1) + " = " + xArray[i]);
        }
    }
}
