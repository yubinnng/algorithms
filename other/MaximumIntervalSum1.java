package cn.qiyubing.algorithm.divide_and_conquer;

import java.util.Arrays;
import java.util.List;

/**
 * 分治法求解最大子段和
 *
 * @author qiyubing
 * @since 2019-05-21
 */
public class MaximumIntervalSum1 {

    private static final List<Integer> NUM_LIST = List.of(1, 2, 3, -4, 5);

    public static void main(String[] args) {
        System.out.println("最大子段和是:" + maximumIntervalSum(NUM_LIST));
    }

    private static int maximumIntervalSum(List<Integer> list) {
        if (list.size() == 1) {
            return list.get(0);
        } else {
            int midIndex = list.size() / 2;
            // 左子段最大和
            int leftMax = maximumIntervalSum(list.subList(0, midIndex));
            // 右子段最大和
            int rightMax = maximumIntervalSum(list.subList(midIndex, list.size()));
            // 从中点开始子段最大和
            int sumMax = 0;
            int temp = 0;
            //从中点往左
            for (int i = midIndex - 1; i >= 0; i--) {
                temp += list.get(i);
                if (temp > sumMax) {
                    sumMax = temp;
                }
            }
            //从中点往右
            for (int i = midIndex; i < list.size(); i++) {
                temp += list.get(i);
                if (temp > sumMax) {
                    sumMax = temp;
                }
            }
            return max(leftMax, rightMax, sumMax);
        }
    }

    private static int max(int... nums) {
        Arrays.sort(nums);
        return nums[nums.length - 1];
    }
}