"""
Một dãy đối xứng là một dãy có dạng như sau
aa
aba
acca
abcba
....
- Viết 1 hàm nhập vào 1 dãy, nếu dãy đó là dãy đối xứng, in ra dãy đó là dãy đối xứng
- Nhập vào các dãy cho đến khi gặp 1 dãy rỗng. In ra danh sách các dãy và kết quả kiểm tra dãy đối xứng hay không đối xứng
"""

def day_doi_xung(s):
    if len(s)>1 and s[::] == s[::-1]:
        print('dãy đối xứng')
    else:
        print('dãy không đối xứng')

while True:
    string = input()
    if len(string) == 0:
        break
    print(string)
    day_doi_xung(string)