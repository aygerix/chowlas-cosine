### Corrected four-certificate audit

NUMERICAL only. Spread is sampled P28; W2 is full P9 on {0} union ±A; BD is the cutoff bound on A at sqrt(n); Gibbs is P29(b) restricted to L=X+h and the tested h. Every entry is divided by sqrt(n). The objective is their maximum (also including the redundant graph-A and compressed-star checks). Finer audits use h=floor(X/d), d=1,2,4,8,16,32; center step max(1,h//4); circle grid >=8(2X+1).

| seed | n | P28 | W2 | BD | Gibbs | maximum | R estimate |
|---|---:|---:|---:|---:|---:|---:|---:|
| smallN_36 | 36 | 0.234085 | 0.440954 | 0.116529 | 0.419937 | 0.440954 | 0.564795 |
| smallN_50 | 50 | 0.213414 | 0.461718 | 0.098591 | 0.463661 | 0.463661 | 0.611995 |
| singer_bu_31 | 992 | 0.225492 | 0.377355 | 0.095496 | 0.509678 | 0.509678 | 0.672615 |
| smallN_100 | 100 | 0.221938 | 0.492606 | 0.109868 | 0.513264 | 0.513264 | 0.665025 |
| singer_bu_11 | 132 | 0.236498 | 0.406814 | 0.115613 | 0.538216 | 0.538216 | 0.791552 |
| taper_random_96_1.2 | 105 | 0.259084 | 0.699811 | 0.135638 | 1.044212 | 1.044212 | 1.550215 |
| taper_Bohr_r2_96_smooth_round | 84 | 0.270001 | 0.531964 | 0.093147 | 1.015624 | 1.015624 | 2.182179 |
| taper_Bohr_r3_96_smooth_round | 104 | 0.258701 | 0.554858 | 0.100800 | 0.946485 | 0.946485 | 1.947936 |
| taper_Bohr_r4_96_smooth_round | 101 | 0.259647 | 0.525037 | 0.106025 | 1.009893 | 1.009893 | 1.783991 |
| prefix_1024_0.833 | 789 | 0.188172 | 0.595544 | 0.064513 | 0.505923 | 0.595544 | 1.161437 |
| quadric_3_False | 30 | 0.257312 | 0.576012 | 0.129029 | 1.464619 | 1.464619 | 2.063441 |

NUMERICAL local search: seed 171702, 400 fixed-cardinality swap proposals per start, annealed acceptance. The optimization objective is the maximum of the certificates, not M. Every retained winner was re-evaluated with the finer parameters above.

| start | n | coarse initial | coarse winner | fine winner | fine P28 | fine W2 | fine Gibbs | R estimate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| smallN_36 | 36 | 0.440954 | 0.428184 | 0.428184 | 0.227918 | 0.428184 | 0.425785 | 0.659987 |
| smallN_50 | 50 | 0.463661 | 0.447344 | 0.460102 | 0.219094 | 0.447344 | 0.460102 | 0.840630 |
| smallN_100 | 100 | 0.513264 | 0.513264 | 0.513264 | 0.221938 | 0.492606 | 0.513264 | 0.665025 |
| taper_Bohr_r3_96_smooth_round | 104 | 0.929851 | 0.782621 | 0.797199 | 0.273274 | 0.559826 | 0.797199 | 1.628934 |
| taper_random_96_0.6 | 99 | 1.036364 | 0.827425 | 0.831932 | 0.284074 | 0.529146 | 0.831932 | 1.971210 |
| taper_random_256_0.6 | 252 | 1.625058 | 1.030116 | 1.040353 | 0.275762 | 0.472337 | 1.040353 | 2.177668 |
| taper_Bohr_r2_96_hard_window | 96 | 1.303736 | 0.725674 | 0.762883 | 0.270383 | 0.496506 | 0.762883 | 1.777173 |
| taper_Bohr_r3_96_hard_window | 98 | 1.044883 | 0.783195 | 0.806544 | 0.272689 | 0.592313 | 0.806544 | 1.658467 |
| prefix_128_0.667 | 96 | 0.599294 | 0.561977 | 0.580342 | 0.219920 | 0.558599 | 0.580342 | 1.143418 |
| singer_bu_11 | 132 | 0.538216 | 0.538216 | 0.538216 | 0.236498 | 0.406814 | 0.538216 | 0.791552 |
