package cn.qiyubing.algorithm.dynamic_programming;

/**
 * 动态规划求解最大子段和
 *
 * @author qiyubing
 */
public class MaximumIntervalSum2 {

    public static void main(String[] args) {

        int[] nums = new int[]{1, 2, 3, -4, 5};

        int maxSum = 0;

        int[] subSums = new int[nums.length];
        subSums[0] = nums[0];

        for (int j = 1; j < nums.length; j++) {
            if (subSums[j - 1] > 0) {
                subSums[j] = subSums[j - 1] + nums[j];
            } else {
                subSums[j] = nums[j];
            }
        }

        // 选出最大字段和
        for (int j = 0; j < subSums.length; j++) {
            if (subSums[j] > maxSum) {
                maxSum = subSums[j];
            }
        }

        System.out.println("最大子段和是:" + maxSum);
    }
}
