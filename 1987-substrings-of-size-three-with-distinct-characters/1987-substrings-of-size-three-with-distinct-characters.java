class Solution {
    public int countGoodSubstrings(String s)
    {
        int cnt=0;
        for (int i=0;i<s.length()-2;i++)
        {
            String res="";
            for (int j=i;j<i+3;j++)
            {
                if(res.indexOf(s.charAt(j))>=0)
                {
                    res="";
                    break;
                }

                res+=s.charAt(j);
                if(res.length()==3)
                {
                    cnt++;
                    System.out.println(res);
                }


            }
        }
        return cnt;
        
    }
}