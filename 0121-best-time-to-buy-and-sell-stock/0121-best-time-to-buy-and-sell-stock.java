class Solution {
    public int maxProfit(int[] arr) {
         
        if (arr.length == 0) {
            return 0 ;
        }		
        int minPrice = arr[0];
        int profit=0;
       

        for(int i=0;i<arr.length;i++)
        {
            if(arr[i] < minPrice) minPrice=arr[i];

            else if (arr[i] - minPrice > profit) profit = arr[i] - minPrice; 
        }
        return profit;
    }
}