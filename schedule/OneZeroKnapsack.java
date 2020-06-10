package cn.qiyubing.algorithm.greedy;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * @author qiyubing
 * @since 2019-05-21
 */
public class OneZeroKnapsack {

    private static List<Goods> goodsList = new ArrayList<>();

    private static final double MAX_WEIGHT = 12;

    static {
        goodsList.add(new Goods(2, 13));
        goodsList.add(new Goods(1, 10));
        goodsList.add(new Goods(3, 24));
        goodsList.add(new Goods(2, 15));
        goodsList.add(new Goods(4, 28));
        goodsList.add(new Goods(5, 33));
        goodsList.add(new Goods(3, 20));
        goodsList.add(new Goods(1, 8));
    }

    public static void main(String[] args) {
        goodsList.sort(Collections.reverseOrder());

        double bagWeight = 0;
        double bagValue = 0;
        for (Goods goods : goodsList) {
            if (bagWeight + goods.getWeight() <= MAX_WEIGHT) {
                bagWeight += goods.getWeight();
                bagValue += goods.getValue();
            }
        }
        System.out.println("背包重量：" + bagWeight);
        System.out.println("背包价值：" + bagValue);
    }
    // 11

    private static class Goods implements Comparable<Goods> {

        private double weight;

        private double value;

        public double getWeight() {
            return weight;
        }

        public void setWeight(double weight) {
            this.weight = weight;
        }

        public double getValue() {
            return value;
        }

        public void setValue(double value) {
            this.value = value;
        }

        public Goods(double weight, double value) {
            this.weight = weight;
            this.value = value;
        }

        @Override
        public int compareTo(Goods o) {
            double thisUnitValue = this.value / this.weight;
            double otherUnitValue = o.getValue() / o.getWeight();
            if (thisUnitValue > otherUnitValue) {
                return 1;
            } else if (thisUnitValue < otherUnitValue) {
                return -1;
            } else {
                return 0;
            }
        }
    }
}
