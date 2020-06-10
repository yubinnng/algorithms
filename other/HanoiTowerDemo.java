package cn.qiyubing.algorithm.recursion;

import java.lang.reflect.Field;
import java.util.Stack;

/**
 * 汉诺塔
 *
 * @author qiyubing
 * @since 2019-05-11
 */
public class HanoiTowerDemo {

    private static final int N = 3;

    private static HanoiTower hanoiTower = HanoiTower.of(N);

    public static void main(String[] args) throws Exception {
        System.out.println(hanoiTower);
        func("a", "b", "c", N);
        // System.out.println(hanoiTower);
    }

    /**
     * 转移函数
     *
     * @param source 起始柱
     * @param temp   中介柱
     * @param target 目标柱
     * @param num    转移个数
     */
    private static void func(String source, String temp, String target, int num) throws Exception {
        if (num == 1) {
            //当只移动数量为1时，直接移动
            hanoiTower.move(source, target);
        } else {
            // 将n - 1个棋子从起始柱移动到中介柱
            func(source, target, temp, num - 1);
            // 移动最下层棋子到目标柱
            hanoiTower.move(source, target);
            // 将n-1个棋子从中介柱移到目标柱
            func(temp, source, target, num - 1);
        }
    }

    private static class HanoiTower {
        // 以下为三根柱子

        private Stack<Plate> a;

        private Stack<Plate> b;

        private Stack<Plate> c;

        private HanoiTower() {
        }

        /**
         * 创建汉诺塔对象
         *
         * @param initNum 初始棋子数量
         */
        private static HanoiTower of(int initNum) {
            Stack<Plate> initPlateStack = new Stack<>();
            for (int i = initNum; i > 0; i--) {
                initPlateStack.add(new Plate(i));
            }
            HanoiTower hanoiTower = new HanoiTower();
            hanoiTower.a = initPlateStack;
            hanoiTower.b = new Stack<>();
            hanoiTower.c = new Stack<>();
            return hanoiTower;
        }

        /**
         * 移动一个最上层棋子
         *
         * @param source 起始柱
         * @param target 目标柱
         * @throws Exception
         */
        private void move(String source, String target) throws Exception {
            Field sourceField = this.getClass().getDeclaredField(source);
            Field targetField = this.getClass().getDeclaredField(target);

            Stack<Plate> sourcePlateStack = (Stack<Plate>) sourceField.get(this);
            Stack<Plate> targetPlateStack = (Stack<Plate>) targetField.get(this);

            Plate pop = sourcePlateStack.pop();
            targetPlateStack.push(pop);
            System.out.println(this);
        }

        @Override
        public String toString() {
            StringBuilder sb = new StringBuilder();

            sb.append("a:\n");
            Stack<Plate> temp = (Stack<Plate>) a.clone();
            while (!temp.empty()) {
                sb.append(temp.pop()).append("\n");
            }

            sb.append("b:\n");
            temp = (Stack<Plate>) b.clone();
            while (!temp.empty()) {
                sb.append(temp.pop()).append("\n");
            }

            sb.append("c:\n");
            temp = (Stack<Plate>) c.clone();
            while (!temp.empty()) {
                sb.append(temp.pop()).append("\n");
            }
            sb.append("**********************************");
            return sb.toString();
        }
    }

    private static class Plate {

        private int size;

        private Plate(int level) {
            this.size = level;
        }

        @Override
        public String toString() {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < size; i++) {
                sb.append("-");
            }
            return sb.toString();
        }
    }
}
