#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void) {
FILE*  ptr;
double x;
int ct = 0;
long double s=0;
char c[10];
ptr = fopen("uni.dat","r");
while(fgets(c,sizeof(c),ptr) != NULL){
   x = atof(c);
    s = s + x;
    ct = ct + 1;   
}
 fseek(ptr, 0,SEEK_SET);
double  mean = s/ct;
s =0;
while(fgets(c,sizeof(c),ptr) != NULL){
   x = atof(c);
    s += (x-mean)*(x - mean);  
}   

 double  var = s/ct;
printf("mean = %lf\n",mean);
printf("var = %lf\n",var);
fclose(ptr);
  return 0;
}
