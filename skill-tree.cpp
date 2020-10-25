//https://programmers.co.kr/learn/courses/30/lessons/49993?language=cpp
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;


int valid(string skill, string skill_tree){
    if (skill.empty() || skill_tree.empty())
        return 1;
    else{
        size_t found = skill.find(skill_tree.at(0));
        if(found!=string::npos){
            if(skill.at(0)==skill_tree.at(0)){
                return valid(skill.substr(1, string::npos), skill_tree.substr(1, string::npos));
            } 
            else return 0;
        }else{
            return valid(skill, skill_tree.substr(1, string::npos));
        }
    }
}
int solution(string skill, vector<string> skill_trees) {
    vector<char> skill_q = vector<char>();
    for (int i = skill.size()-1; i>=0; i--){
        skill_q.push_back(skill[i]);
    }
    int ans = 0;
    for (int i=0; i<skill_trees.size(); i++){
        if (valid(skill, skill_trees[i])) {
            ans++;
        }
    }
    return ans;
}
