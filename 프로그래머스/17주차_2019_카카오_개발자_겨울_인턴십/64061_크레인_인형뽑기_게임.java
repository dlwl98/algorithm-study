import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        int n = board.length;
        int m = board[0].length;
        
        Stack<Integer> prize = new Stack<Integer>();
        Stack<Integer>[] stacks = new Stack[m];
        for(int i=m-1; i>=0; i--){
            stacks[i] = new Stack<Integer>();
            for(int j=n-1; j>=0; j--){
                if(board[j][i] != 0){
                    stacks[i].push(board[j][i]);   
                }
            }
        }
        
        for(int move : moves){
            int idx = move - 1;
            if (stacks[idx].isEmpty()){
                continue;
            }
            int cur = stacks[idx].pop();
            if(prize.isEmpty()){
                prize.push(cur);
                continue;
            }
            if(prize.peek() == cur){
                answer += 2;
                prize.pop();
                continue;
            }
            prize.push(cur);
        }
        
        return answer;
    }
}
