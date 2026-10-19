// Exact finite falsification of eta=1/10, B=2 in the localized moment lemma.
// Compile and execute ONLY on the VM via dirun.sh.
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <vector>

int main(int argc,char**argv){
  int cap=argc>1?std::stoi(argv[1]):18;
  uint64_t checked=0, failures=0;
  auto start=std::chrono::steady_clock::now();
  for(int X=1;X<=cap;++X){
    uint64_t before=checked;
    for(uint64_t mask=uint64_t(1)<<(X-1);mask<(uint64_t(1)<<X);++mask){
      int n=__builtin_popcountll(mask);
      if(10*n<X)continue;
      ++checked;
      auto av=[&](int j)->int{j=std::abs(j);return j>=1&&j<=X?((mask>>(j-1))&1):0;};
      std::vector<int>S;
      for(int j=1;j<=X;++j)if(av(j)){S.push_back(j);S.push_back(-j);}
      std::vector<int>pairs(4*X+1,0),triples(3*X+1,0);
      for(int a:S)for(int b:S)++pairs[a+b+2*X];
      for(int k=0;k<=3*X;++k)for(int a:S)
        if(std::abs(k-a)<=2*X)triples[k]+=pairs[k-a+2*X];
      bool success=false;
      for(int q=1;q<=X&&!success;++q){
        int64_t E=0;
        for(int j=1;j<=X+q;++j){
          int b=2*av(j)-av(j-q)-av(j+q);
          E+=b*b;
        }
        if(10*E<8*n)continue;
        int64_t Delta=10*triples[0]-15*triples[q]+6*triples[2*q]-triples[3*q];
        int64_t Wnum=Delta+6*av(q)*E+4*av(q);
        if(Wnum<=0||Wnum*Wnum<=8*E*E*E)success=true;
      }
      if(!success){
        ++failures;
        std::cout<<"{\"status\":\"EXACT COUNTEREXAMPLE TO eta=.1 B=2, not to quantified lemma\",\"X\":"
                 <<X<<",\"n\":"<<n<<",\"A\":[";
        bool first=true;
        for(int j=1;j<=X;++j)if(av(j)){if(!first)std::cout<<",";std::cout<<j;first=false;}
        std::cout<<"],\"sets_checked\":"<<checked<<"}\n";
        return 0;
      }
    }
    std::cout<<"{\"completed_X\":"<<X<<",\"sets_at_X\":"<<checked-before<<",\"sets_checked\":"<<checked<<"}\n";
  }
  double secs=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
  std::cout<<"{\"status\":\"EXACT EXHAUSTIVE PASS\",\"cap\":"<<cap
           <<",\"density_condition\":\"X<=10n\",\"sets_checked\":"<<checked
           <<",\"failures\":"<<failures<<",\"seconds\":"<<secs<<"}\n";
}
