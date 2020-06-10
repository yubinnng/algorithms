import java.util.ArrayList;
import java.util.List;

/**
 * 根据利润/重量得到的权重，冒泡排序后装入背包
 * @author qiyubing
 * @since 2019-04-03
 */
public class KnapsackDemo {

    public static final double MAX_WEIGHT = 30.0;

    public static void main(String[] args) {
        List<Knapsack> knapsackList = new ArrayList<>(List.of(
                new Knapsack(0, 4.0, 10.0),
                new Knapsack(1, 3.0, 9.0),
                new Knapsack(2, 6.0, 4.0),
                new Knapsack(3, 20.0, 1.0),
                new Knapsack(4, 1.0, 20.0),
                new Knapsack(5, 7.0, 3.0),
                new Knapsack(6, 8.0, 7.0)
        ));

        // 冒泡倒排
        for (int i = 0; i < knapsackList.size(); i++) {
            for (int j = 0; j < knapsackList.size() - i - 1; j++) {
                double gap = knapsackList.get(j).countRight() - knapsackList.get(j + 1).countRight();
                if (gap < 0) {
                    // 交换
                    var temp = knapsackList.get(j);
                    knapsackList.set(j, knapsackList.get(j + 1));
                    knapsackList.set(j + 1, temp);
                }
            }
        }

        // 装入背包
        double nowWeight = 0;
        for (int i = 0; i < knapsackList.size(); i++) {
            double nextWeight = knapsackList.get(i + 1).getWeight();
            if (nowWeight + nextWeight < MAX_WEIGHT) {
                nowWeight += nextWeight;
            } else {
                break;
            }
            System.out.println("装入背包：" + knapsackList.get(i));
        }
    }


    /**
     * 背包
     */
    private static class Knapsack {

        private int id;

        private double weight;

        private double profit;

        private Knapsack(int id, double weight, double profit) {
            this.id = id;
            this.weight = weight;
            this.profit = profit;
        }

        private double countRight() {
            return this.profit / this.weight;
        }

        public int getId() {
            return id;
        }

        public void setId(int id) {
            this.id = id;
        }

        public double getWeight() {
            return weight;
        }

        public void setWeight(double weight) {
            this.weight = weight;
        }

        public double getProfit() {
            return profit;
        }

        public void setProfit(double profit) {
            this.profit = profit;
        }

        @Override
        public String toString() {
            return "Knapsack{" +
                    "id=" + id +
                    ", weight=" + weight +
                    ", profit=" + profit +
                    ", right=" + countRight() +
                    '}';
        }
    }
}
