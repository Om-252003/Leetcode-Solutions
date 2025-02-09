class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        

         int[] frequencyArray = new int[1001];

         for(int num : nums1)
         {
            frequencyArray[num]++;
         }

         ArrayList<Integer> list = new ArrayList<>();
         for(int num:nums2)
         {
            if(frequencyArray[num]>0)
            {
                list.add(num);
                frequencyArray[num]--;
            }
         }

         int[] res = new int[list.size()];

         for(int i=0;i<list.size();i++)
         {
            res[i] = list.get(i);
         }
        return res;
    }
}