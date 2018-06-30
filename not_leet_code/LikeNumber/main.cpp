#include <stdio.h>

char str[] = "2220";
int nStr = sizeof(str)-1;
int arr[10] = {};

void K(int l, int &cnt)
{
    if (l == nStr) {
        printf("%s\n",str);
        cnt++;
        return;
    }
    for(int i=0; i<10;i++) {
        if (i==0 && l==0) {
            continue;
        }
        if (arr[i]==0) {
            continue;
        }
        arr[i]-=1;
        str[l]=i+'0';
        K(l+1,cnt);
        arr[i]+=1;
    }
}

int main()
{
    // init
    for (int i=0; i < nStr; i++) {
        arr[str[i]-'0']++;
    }

    /*
    for (int i=0; i < 10; i++) {
        printf ("arr[%d]=%d\n", i, arr[i]);
    }*/

    int cnt = 0;
    K(0,cnt);
    printf ("%d\n",cnt);

    return 0;
}
