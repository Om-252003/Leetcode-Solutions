class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {

        Map<Integer, Integer> map = new HashMap();
        int idx=0;
        for(int num:nums)
        {
            if(map.containsKey(num) && (Math.abs((idx - map.get(num)) )<=k)) return true;
                
            else{
                map.put(num, idx);
            }
            idx++;
        }
        return false;
        
    }
}