package cn.qiyubing.word_statistics;

import cn.qiyubing.util.FileUtils;

import java.io.IOException;
import java.util.*;

/**
 * 单词统计
 *
 * @author qiyubing
 * @since 2019-06-28
 */
public class WordStatistics {

    /**
     * 单词文本文件
     */
    private static final String FILE_PATH = "";

    /**
     * 单词个数统计表
     */
    private static Map<String, Integer> statisticsTable = new HashMap<>(100);

    /**
     * 特殊字符集合
     */
    private static Set<Character> specialChar = new HashSet<>(15);

    // 添加特殊字符
    static {
        specialChar.add(' ');
        specialChar.add('.');
        specialChar.add(',');
        specialChar.add(';');
        specialChar.add('\"');
        specialChar.add('“');
        specialChar.add('”');
        specialChar.add(':');
        specialChar.add('\'');
        specialChar.add('\n');
        // 添加字符 1 - 9
        for (int i = 0; i < 9; i++) {
            specialChar.add((char) (i + '0'));
        }
    }

    public static void main(String[] args) throws IOException {
        // 读取文件中的所有字符
        String input = FileUtils.readString(FILE_PATH);
        // 转为char数组
        char[] text = input.toCharArray();
        // 当前读取到的单词
        StringBuffer nowWord = new StringBuffer();
        for (int i = 0; i < text.length; i++) {
            char ch = text[i];
            // 当前字符是否是特殊字符
            if (!specialChar.contains(ch)) {
                nowWord.append(ch);
                // 判断当前是否是结尾
                if (i == text.length - 1) {
                    putWord(nowWord);
                }
            } else {
                putWord(nowWord);
                nowWord = new StringBuffer();
            }
        }

        // 打印统计表
        Set<String> keySet = statisticsTable.keySet();
        for (String key : keySet) {
            System.out.println(key + " 出现了 " + statisticsTable.get(key) + " 次");
        }

        System.out.println("共有" + keySet.size() + "种单词");
    }

    private static void putWord(StringBuffer sb) {
        if (sb.length() > 0) {
            String word = sb.toString().toLowerCase();
            // 统计表中是否有该单词
            if (statisticsTable.containsKey(word)) {
                statisticsTable.put(word, statisticsTable.get(word) + 1);
            } else {
                // 统计表中无该单词
                statisticsTable.put(word, 1);
            }
        }
    }
}
