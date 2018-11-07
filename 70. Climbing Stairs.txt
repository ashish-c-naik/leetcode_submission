class Solution {
    HashMap<Integer, Integer> hmap = new HashMap<Integer, Integer>();
    public int rec(int n){
        if (n < 0)
            return 0;
        if (n == 0)
            return 1;
        int val1,val2;
        if (hmap.get(n-1) == null){
             val1 = rec(n-1);
             hmap.put(n-1,val1);
        }else{
            val1 = hmap.get(n-1);
        }
        if(hmap.get(n-2) == null){
            val2 = rec(n-2);
            hmap.put(n-2,val2);
        }else{
            val2 = hmap.get(n-2);
        }
        return val1+val2;
    }
    public int climbStairs(int n) {
        return rec(n);
    }
}