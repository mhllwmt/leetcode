class Solution {
public:
    string add(string num1, string num2) {
        int n = max(num1.size(), num2.size());
        string ans;
        int k = 0;
        for (int i=0; i<n; i++) {
            int t1, t2;
            t1 = t2 = 0;
            if(i<num1.size()) t1 = num1[num1.size() - 1 - i] - '0';
            if(i<num2.size()) t2 = num2[num2.size() -1 - i] - '0';
            int tmp = k + t1 + t2;
            k = tmp / 10;
            ans.push_back('0' + tmp % 10);
        }
        if(k) ans.push_back('0' + k);
        reverse(ans.begin(), ans.end());
        return ans;
    }
    string multiply(string num1, string num2) {
        string ans = "0";
        if(num1 == ans || num2 == ans)
            return ans;
        string init;
        for(int i=num1.size()-1; i>=0; i--) {
            string mul = init;
            int k = 0;
            for(int j=num2.size()-1; j>=0; j--) {
                int tmp = int(num2[j] - '0') * int(num1[i]-'0') + k;
                k = tmp / 10;
                mul.push_back('0' + tmp % 10);
            }
            if(k)   mul.push_back('0' + k);
            reverse(mul.begin(), mul.end());
            // cout << mul << "\n";
            init.push_back('0');
            ans = add(ans, mul);
            // cout << ans << "\n\n";
        }
        return ans;
    }
};