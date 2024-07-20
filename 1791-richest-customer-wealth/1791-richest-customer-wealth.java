class Solution {
    public int maximumWealth(int[][] acc) {

        ArrayList<Integer> maxi = new ArrayList<Integer>();
        int sum = 0,m=0;

        for(int i = 0; i<acc.length;i++){
            for(int j = 0 ; j<acc[i].length ; j++){
                sum += acc[i][j];
            }
            maxi.add(sum);
            sum=0;
        }
        return Collections.max(maxi);
    }
}