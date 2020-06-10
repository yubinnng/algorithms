package cn.qiyubing.algorithm.recursion;

/**
 * 斐波那契数列: 0、1、1、2、3、5、8
 * 可以这样理解 f0 = 0; f1 = 1; fn = f(n-1) + f(n - 2) （n >= 2）
 *
 * @author qiyubing
 */
public class Fibonacci {

    public static void main(String[] args) {
        for (int i = 0; i < 10; i++) {
            System.out.print(f(i) + " ");
        }
    }

    private static int f(int n) {
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else {
            return f(n - 1) + f(n - 2);
        }
    }
}