package cn.qiyubing;

/**
 * 方程求根
 *
 * @author qiyubing
 * @since 2019-03-19
 */
public class SolvingEquation {

    /**
     * 精度
     */
    private static final Double PRECISION = 0.5 * Math.pow(10, -5);

    public static void main(String[] args) {
        dichotomy();
        newton();
    }

    // 二分法
    private static void dichotomy() {
        Double a = 1.0;
        Double b = 2.0;
        int n = 1;
        while (true) {
            // x为二分点
            Double x = (a + b) / 2;
            Double fx = f(x);
            if (fx > 0) {
                // 若f(x)大于0则右边界左移至x
                b = x;
            } else if (fx < 0) {
                // 若f(x)小于0则左边界右移至x
                a = x;
            } else {
                // 若f(x)等于0则根x的值
                System.out.println("二分法结果为：" + x);
                break;
            }
            // 精度足够时
            if (b - a <= PRECISION) {
                System.out.println("二分法结果为：" + b);
                break;
            }
            System.out.println(String.format("第%s次：中点%s值为%s", n++, x, fx));
        }
    }

    // 牛顿法
    private static void newton() {
        Double x = 1.5;
        int n = 1;
        while (true) {
            Double nowX = getNowX(x);
            // 精度足够
            if (Math.abs(nowX - x) < PRECISION) {
                System.out.println(String.format("第%s次：牛顿法结果为%s", n, nowX));
                break;
            }
            x = nowX;
            System.out.println(String.format("第%s次：x为%s", n++, x));
        }
    }

    /**
     * f(x)
     */
    private static Double f(Double x) {
        return Math.pow(x, 3) + 4 * Math.pow(x, 2) - 10;
    }

    /**
     * 求Xn+1
     *
     * @param x Xn
     * @return Xn+1
     */
    private static Double getNowX(Double x) {
        return x - f(x) / (3 * Math.pow(x, 2) + 8 * x);
    }
}
