//https://programmers.co.kr/learn/courses/30/lessons/64061?language=cpp

#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<vector<int> > board, vector<int> moves) {
    vector<vector<int> > col_stack (board[0].size(), vector<int>());
    for (int j = 0; j < board[0].size(); j++){
        for (int i=board.size()-1; i>=0; i--){
            if (board[i][j]){
                col_stack[j].push_back(board[i][j]);
            }
        }
    }
    
    int popped = 0;
    vector<int> drawn_stack = vector<int>();
    for (int idx = 0; idx < moves.size(); idx++){
        int col = moves[idx]-1;
        if(!col_stack[col].empty()){
            int drawn_now = col_stack[col].back();
            col_stack[col].pop_back();
            
            if(!drawn_stack.empty()){
                int drawn_last = drawn_stack.back();
                if(drawn_now == drawn_last){
                    drawn_stack.pop_back();
                    popped += 2;
                }else{
                    drawn_stack.push_back(drawn_now);
                }
            }else{
                drawn_stack.push_back(drawn_now);
            }
        }
    }
    
    
    return popped;
}

int main (){
    vector<vector<int> > board {{0,0,0,0,0},{0,0,1,0,3},{0,2,5,0,1},{4,2,4,4,2},{3,5,1,3,1}};
    vector<int> moves {1,5,3,5,1,2,1,4};
    int ans = solution (board, moves);
}