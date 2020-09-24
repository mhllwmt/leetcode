#include<bits/stdc++.h>
using namespace std;
int num[300];
int isok[300];
struct node{
    char ch;
    int id;
};
class Solution {
public:
    string minWindow(string s, string t) {
        queue<node> q;
        int n = s.size(), m = t.size(), sum=0;
        for (int i = 0; i<300; i++)
            num[i] = isok[i] = 0;
        for (int i = 0; i < m; i++)  {
            if (isok[t[i]]==0)
                sum++;
            isok[t[i]] += 1;
        }
        int tot = 0;
        int l=0, len=n+1;
        for (int i = 0; i < n; i++) {
            if(isok[s[i]]) {
                num[s[i]]++;
                node tmp = {s[i], i};
                q.push(tmp);
                if(num[s[i]]==isok[s[i]])
                    tot++;
                // cout << s[i] << "##" << num[s[i]] << " ";
                // cout << tot << endl;
                if(tot==sum) {
                    int start = q.front().id;
                    if(len>i-start+1) {
                        len = i-start+1;
                        l = start;
                    }
                    num[q.front().ch]--;
                    tot--;
                    q.pop();
                }
                while (!q.empty()) {
                        char ch = q.front().ch;
                        int id = q.front().id;
                        if (num[ch]<=isok[ch])
                            break;
                        else {
                            num[ch]--;
                            q.pop();
                        }
                    }
            }
        }
        if (len==n+1) return "";
        else          return s.substr(l, len);
    }
};