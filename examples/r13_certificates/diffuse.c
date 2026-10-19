#include <math.h>
#include <stdlib.h>
/* Profile-count-preserving sequential negative-error diffusion, 64 tracked modes. */
void diffuse(int X,int F,int B,const double *p,const double *w,const double *angles,unsigned char *bits){
 double *c=calloc(F,sizeof(double)),*s=calloc(F,sizeof(double));
 double *ca=calloc(F,sizeof(double)),*sa=calloc(F,sizeof(double)),*v=calloc(F,sizeof(double));
 for(int j=0;j<F;j++){c[j]=1;ca[j]=cos(angles[j]);sa[j]=sin(angles[j]);}
 double carry=0;
 for(int lo=0;lo<X;lo+=B){
  int hi=lo+B;if(hi>X)hi=X;double target=carry;
  for(int k=lo;k<hi;k++)target+=p[k];int need=(int)floor(target+.5);carry=target-need;
  for(int k=lo;k<hi;k++){
   double score[2]={0,0};
   for(int j=0;j<F;j++){
    double nc=c[j]*ca[j]-s[j]*sa[j];s[j]=s[j]*ca[j]+c[j]*sa[j];c[j]=nc;
    for(int b=0;b<2;b++){double z=v[j]+(b-p[k])*w[k]*nc;if(z<0)score[b]+=z*z;}
   }
   int bit=score[1]<score[0];if(need==0)bit=0;if(need==hi-k)bit=1;
   bits[k]=bit;need-=bit;
   for(int j=0;j<F;j++)v[j]+=(bit-p[k])*w[k]*c[j];
  }
 }
 free(c);free(s);free(ca);free(sa);free(v);
}
