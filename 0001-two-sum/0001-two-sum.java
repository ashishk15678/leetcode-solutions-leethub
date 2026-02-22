class Solution {
    public int[] twoSum(int[] array, int target) {
        int[] returnArray = new int[2];

        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array.length; j++) {
                if (i == j)
                    continue;
                else if (array[i] + array[j] == target) {
                    returnArray[0] = i;
                    returnArray[1] = j;
                    return returnArray;
                }
            }
        }

        return null;
    }
}