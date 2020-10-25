//https://programmers.co.kr/learn/courses/30/lessons/60057?language=cpp
#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string s) {
    int ans = s.size();
    for (int subsize = 1; subsize <= int(s.size()/2); subsize++){
        int zipsize = subsize;
        string last_subs = s.substr(0, subsize);
        int last_occ = 1;
        for(int idx = subsize; idx < int(s.size()/subsize)*subsize; idx += subsize){
            string subs = s.substr(idx, subsize);
            if (last_subs.compare(subs)){
                zipsize += subsize;
                if (last_occ >1){
                    zipsize += to_string(last_occ).size() ;
                }
                last_occ = 1;
                last_subs = subs;
            }else{
                last_occ++;
            }
        }
        if (last_occ >1){
            zipsize += to_string(last_occ).size();
        }
        zipsize += s.size()%subsize;
        if (zipsize<ans){
            ans = zipsize;
        }
    }
    return ans;
}
int main(){
    string s= "ababcdcdababcdcd";
    cout << solution(s);
}