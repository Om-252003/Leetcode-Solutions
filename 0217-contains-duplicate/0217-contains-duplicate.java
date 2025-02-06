class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> map = new HashMap();

        for(int num:nums)
        {
            map.put(num, map.getOrDefault(num,0)+1);
        }

        for(int i: map.keySet()){
            if(map.get(i)>1)  return true;
        }
        return false;
    }
}