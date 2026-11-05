class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set numsSet = new HashSet<>();
        for (int i : nums){
            if (numsSet.contains(i)){
                return true;
            }
            numsSet.add(i);
        }
        return false;
    }
}