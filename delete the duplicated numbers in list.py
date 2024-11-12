#include<stdio.h>
int main()
{
    int n,a[50],i,j,t;
    scanf("%d",&n);
    scanf("%d",&a[0]);
    t=a[0];
    for(i=1;i<n;i++){
        scanf("%d",&a[i]);
        if(t<a[i])
          t=a[i];
    }
    t+=1;
    for(i=0;i<n;i++){
        for(j=i+1;j<n;j++){
            if(a[i]==a[j])
               a[j]=t;
        }
        if(a[i]!=t)
          printf("%d ",a[i]);
    }
    return 0;
}
