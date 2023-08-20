#include <iostream>

using namespace std;

int main()
{
    string str;
    cin >> str;

    int wordValue = 0;

    for (char ch : str)
    {
        int num = static_cast<int>(ch);

        // 대문자: 65~90 -> 27~52, 소문자: 97~122 -> 1~26
        if (num <= 90) // 대문자인 경우
        {
            num -= 38;
        }
        else // 소문자인 경우
        {
            num -= 96;
        }

        wordValue += num;
    }

    // 소수 체크
    bool primeFlag = true;

    for (int i = 2; i < wordValue; i++)
    {
        if (wordValue % i == 0)
        {
            primeFlag = false;
            cout << "It is not a prime word." << endl;
            break;
        }
    }
    if (primeFlag == true)
    {
        cout << "It is a prime word." << endl;
    }
}