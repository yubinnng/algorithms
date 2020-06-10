package cn.qiyubing.algorithm.recursion;

/**
 * 生成格雷码
 *
 * @author qiyubing
 * @since 2019-05-12
 */
public class GrayCode {

    public static void main(String[] args) {
        String[] grayCodes = generate(3);
        for (String grayCode : grayCodes) {
            System.out.println(grayCode);
        }
    }

    /**
     * 递归生成格雷码
     *
     * @param n 格雷码位数
     */
    private static String[] generate(int n) {
        if (n == 1) {
            return new String[]{"0", "1"};
        } else {
            // 获取n-1位格雷码的数组
            String[] lastCodes = generate(n - 1);
            String[] newCodes = new String[2 * lastCodes.length];
            // 前半部分加"0"
            for (int i = 0; i < lastCodes.length; i++) {
                newCodes[i] = "0" + lastCodes[i];
            }
            // 后半部分加"1"
            for (int i = 0; i < lastCodes.length; i++) {
                newCodes[newCodes.length - 1 - i] = "1" + lastCodes[i];
            }
            return newCodes;
        }
    }
}

