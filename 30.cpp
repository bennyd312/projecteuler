#include <iostream>
#include <array>
#include <cmath>
#include <string>

int powerSum(std::array<int,6> arr){
    
    int sum=0;

    for(int i=0; i<6;i++){
        sum += static_cast<int>(std::pow(arr[i],5));
    }
    
    return sum;
}

std::array<int,6> getDigits(int num){
    std::array<int,6> arr;
    std::string s = std::to_string(num);
    while(s.size()<6){
        s = "0" + s;
    }
    for(int i =0; i<6; i++){
        char digit = s[i];
        arr[i] = digit - '0';
    }
    return arr;
}



int main() {
    int sum = 0;

    for(int num=2;num<1000000;num++){
        std::array<int,6> digits = getDigits(num);
        if(num==powerSum(getDigits(num))){
            sum += num;
        }
    }
    std::cout << sum;
    return 0;
}