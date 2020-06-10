package cn.qiyubing.algorithm.greedy;

import java.util.*;

/**
 * 最小延迟调度问题
 *
 * @author qiyubing
 * @since 2019-05-13
 */
public class MinDelaySchedule {

    /**
     * 任务列表
     */
    private static List<Task> taskList;

    static {
        taskList = new ArrayList<>();
        taskList.add(new Task(5, 10));
        taskList.add(new Task(8, 12));
        taskList.add(new Task(4, 15));
        taskList.add(new Task(10, 11));
        taskList.add(new Task(3, 20));
    }

    /**
     * 总耗时
     */
    private static int time = 0;

    /**
     * 最大延迟
     */
    private static int maxDelay = Integer.MIN_VALUE;

    public static void main(String[] args) {

        while (!taskList.isEmpty()) {
            int minDelay = Integer.MAX_VALUE;
            Task minDelayTask = null;
            for (Task task : taskList) {
                int delay = time + task.getPredictTime() - task.getExpectTime();
                delay = delay < 0 ? 0 : delay;
                if (delay < minDelay) {
                    minDelay = delay;
                    minDelayTask = task;
                }
            }
            if (minDelay > maxDelay) {
                maxDelay = minDelay;
            }
            time += minDelayTask.getPredictTime();

            System.out.println("minDelay = " + minDelay);
            System.out.println(minDelayTask);
            System.out.println("time = " + time);

            taskList.remove(minDelayTask);
        }
        System.out.println("maxDelay = " + maxDelay);
    }

    private static class Task {

        /**
         * 预计耗时
         */
        private int predictTime;

        /**
         * 用户期望耗时
         */
        private int expectTime;

        private Task(int predictTime, int expectTime) {
            this.predictTime = predictTime;
            this.expectTime = expectTime;
        }

        private int getPredictTime() {
            return predictTime;
        }

        private int getExpectTime() {
            return expectTime;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Task)) return false;
            Task task = (Task) o;
            return predictTime == task.predictTime &&
                    expectTime == task.expectTime;
        }

        @Override
        public int hashCode() {
            return Objects.hash(predictTime, expectTime);
        }

        @Override
        public String toString() {
            return "Task{" +
                    "predictTime=" + predictTime +
                    ", expectTime=" + expectTime +
                    '}';
        }
    }
}
