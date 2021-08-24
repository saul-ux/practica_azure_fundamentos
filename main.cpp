#include <iostream>
#include <vector>

using namespace std;

 int main(){
bool haspairwhitsum(const vector<int>data, int sum){
                    unordered_set<int>comp;
                    for(int value:data){
                        if(comp.find(value)!=comp.end)
                            return true;
                        comp.add(sum-value);
                    }
    return false;
}
}
