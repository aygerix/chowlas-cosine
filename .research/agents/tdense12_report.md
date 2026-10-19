# Round 12 research report

PROVED scope: this report follows `.research/agents/tdense12_brief.md`. Conventions are f_A(x)=sum_{a in A} cos(ax), M(A)=-min f_A, n=|A|, X=max A. This round changes only this report and `.research/agents/tdense12_scratch/`, uses no subagents, makes no commits, and produces no LaTeX. All mathematical computation is restricted to the prescribed dirichlet VM command with at most four cores; all LP/MILP/QP work, if needed, uses Gurobi.

## Current checkpoint

PROVED final round-12 results: Task 1 alternative (B), the CSFG(20) coupled cyclic reduction with its exact conditional range; the exact partial-period Fejér transfer and cyclic homogenization lemma R12-H; the nested-schedule theorem R12-N, M>=n/((3*pi+2)r); the unrestricted nonnested counterexample R12-U; corrected complex/real Parseval identities; and the precise scalar exponent barrier R12-S. The full proofs and quantifiers are below. No unconditional uniform front gap and no unconditional exponent above 1/3 are claimed.

PROVED quoted baseline remains unchanged: P58–P63 give T-dense(C) for every fixed C<2000/259, with an ineffective positive constant. P61 defines the exact second-order constant D; 1/D about 8.5708 is NUMERICAL, not a proved decimal endpoint. The round-11 report supplies the DC barrier, repair-energy inequality, total rational-atom budget, and Paley boundary. Round 12 proves no new unconditional T-dense endpoint.

PROVED reading record: read CLAUDE.md first after the brief, the number-theory research skill and its arithmetic/experiment references, P58–P63, NOTEBOOK continuations 12–16, the round-11 report, P26/P34/P53, and src/dirun.sh. Project-wide root research records will not be edited. Relevant PROOFS searches precede any novelty claim.

CONJECTURED remaining main target: a universal a*<1/2 for positive-density binary limits with M=o(sqrt(X)). This round takes the authorized alternative (B), with the precise missing hypothesis CSFG(20). The front Fejér reduction, cyclic normalization/partial-period identity, and Parseval roughness audits are complete below.

HEURISTIC research frontier:

| Known | Exact gap | Discriminating next step |
| --- | --- | --- |
| Exact Fejér transfer and R12-H prove the cyclic barrier | A mesoscopic front need not be a fixed Haar model | Quantify the support/taper gap in CSFG(20) |
| R12-N gives X/N for nested schedules | The stronger nested X*sqrt(p0/N) bound is unresolved | Extend the zero-class argument to controlled repeated removals |
| Sanders v2's 1/3 statement is source-verified; R12-S blocks scalar refinements | A genuine full-convolution or arithmetic gain | Test PK(eta) on exact half-set spectra |

PROVED status: unrestricted nonnested X/N and X*sqrt(p0/N) bounds are false by R12-U; the stronger square-root-in-N bound for nested schedules remains CONJECTURED. Failed steps and counterexamples are preserved below.

## Task 1 audit checkpoint: exact Fejér front and cyclic transfer

PROVED exact front identity: for every binary A, integer Y>=2, tau_k=1-k/Y, and F_Y(x)=sum_{|k|<Y}(1-|k|/Y)exp(ikx),

    S_Y(x)=sum_{k=1}^{Y-1} tau_k*(2*1_A(k)-1)*cos(kx)
          =2*(F_Y*f_A)(x)-(F_Y(x)-1)/2.

PROVED consequence: normalized circle convolution preserves f_A>=-M(A), so S_Y>=-2M(A)+1/2-F_Y/2. On Y^(-1/2)<=|x|<=pi, F_Y<=pi^2, giving S_Y>=-2M(A)-(pi^2-1)/2. This holds with no smoothing hypothesis and is enough for the proposed front reduction. In the counterexample regime M=o(sqrt(Y)), the brief's asymptotic form S_Y>=-4m-o(sqrt(Y)) follows as well for ANY m>=0, by absorbing 2M+O(1) into the error. No separate smooth-profile mismatch estimate is necessary. A stronger finite bound whose error is controlled solely by m has not been proved here.

PROVED exact cyclic identity: let q>=2, s:Z_q->{-1,1} even, H_gamma=sum_c s_c exp(-2*pi*i*gamma*c/q), and extend s periodically. Then

    S_Y(x)=(1/(2q))*sum_gamma H_gamma*F_Y(x+2*pi*gamma/q)-s_0/2.

PROVED root-of-unity filter: sum_gamma F_Y(x+2*pi*gamma/q)=q when 1<=Y<=q, since F_Y has degree Y-1<q. More generally the sum equals q*sum_{|j|q<Y}(1-|j|q/Y)exp(ijqx); for Y=Lq it equals q*F_L(qx)<=qL. Consequently, if ALL H_gamma>=-K, then S_Y>=-K/2-1/2 for Y<=q, and S_(Lq)>=-KL/2-1/2. No estimate of Fejér tails is needed.

PROVED normalization correction: if lambda_gamma=sum_{c in S}exp(-2*pi*i*gamma*c/q), then H_gamma=2*lambda_gamma for gamma!=0 and H_0=2|S|-q. A half-set assumption |2|S|-q|<=1 and lambda_gamma>=-K only give the bound with sign threshold max(2K,1). The coefficient multiplying F_Y in the sign identity is H_gamma, not lambda_gamma.

PROVED audit requirement, resolved by R12-H below: the cyclic transfer also needs local balance and the vanishing of fixed rational atoms. Primality and half cardinality alone do not state those properties; the small-negative-spectrum/binary argument supplies them.

## Task 2 audit checkpoint: corrections and a quantitative route

PROVED correction to the roughness interpretation: the complex transform energy cannot be used as real cosine-spike energy without a separate real-part identity. For a smooth nested density p with p(1)=0, the subtracted term |integral p(t)exp(i*xi*t)dt|^2 has leading term p(0)^2/xi^2. Thus the complex nonprincipal energy has leading coefficient 2p(0)-p(0)^2, rather than 2p(0), under the required oscillatory-decay assumptions. For finite staircase schedules no pointwise large-xi asymptotic is automatic.

HEURISTIC pivot: retain the exact Parseval identities, but prove X/N by combining the root-grid second moment with restriction to the zero residue class. In a nested removal model that class is an initial arithmetic progression, whose negative minimum is linear in its length. This avoids converting arbitrary complex energy into negative real values.

## Task 2 theorem: exact quantitative exclusion of nested periodic schedules

PROVED theorem R12-N (paper proof, not kernel-checked). Let N>=1 be an integer and A a nonempty finite set of positive integers. Write n=|A|, r=|{a mod N:a in A}|, and ell_0=|A intersect NZ|. Suppose A intersect NZ={N,2N,...,ell_0*N}, with the empty set allowed. Then

    M(A) >= n/((3*pi+2)*r).

PROVED symmetric-count strengthening: if ell_c=ell_{-c} for every residue c, the lower bound is 2n/((3*pi+2)r). The set itself need not be symmetric. All these assertions hold for every finite N and A under the stated zero-class hypothesis, without asymptotic quadrature errors.

PROVED proof. At x_s=2*pi*s/N let v_s=f_A(x_s). Root orthogonality gives

    sum_s v_s=N*ell_0,
    sum_s v_s^2=N*sum_c ((ell_c+ell_{-c})/2)^2
                >= (N/2)*sum_c ell_c^2 >= N*n^2/(2r).

PROVED details: the first inequality follows because sum ell_c*ell_{-c}>=0; the last is Cauchy–Schwarz over the r occupied residues. Since -M<=v_s<=n, (v_s+M)(n-v_s)>=0, so

    n^2/(2r) <= n*ell_0 + (n-ell_0)*M <= n*(ell_0+M).

PROVED hence M>=n/(2r)-ell_0. Restriction to NZ preserves the lower bound by circle averaging. For ell=ell_0>=1, the initial progression has, at t=3*pi/(2ell+1),

    sum_{j=1}^ell cos(jt)=-(1+csc(3*pi/(4ell+2)))/2
                        <= -2ell/(3*pi).

PROVED thus M>=c*ell_0, c=2/(3*pi). Combining ell_0<=M/c with M+ell_0>=n/(2r) gives M>=n/((3*pi+2)r). If ell_0=0 the root-grid inequality already gives M>=n/(2r). Symmetric counts remove the factor 1/2 in the second moment and give the stated factor-two improvement. This includes N=1. No estimate of sampled minima is being promoted to a circle lower bound: both the root values and the progression value are actual evaluation/averaging witnesses.

PROVED nested-model corollary with exact quantifiers. Fix H,N positive integers and cutoffs U_c in [0,H], c in Z_N, and put

    A={k in {1,...,H}: k<=U_(k mod N)}.

PROVED let X=max A as usual. If p0=|{c:U_c>0}|/N>0 and d=|A|/X, then r<=p0*N and

    M(A) >= d*X/((3*pi+2)*p0*N).

PROVED consequence: for every fixed d0>0, a sequence of these sets with d>=d0 and N=o(sqrt(X)) has M/sqrt(X)->infinity. If N<=B*sqrt(X), it has M>=d0*sqrt(X)/((3*pi+2)B). Thus all nested mesoscopic residue schedules below the square-root modulus scale are excluded from dense counterexamples, including every removal order and highly concentrated positive spectra. This does not prove the conjectured X*sqrt(p0/N) bound, and for sqrt(X)<<N<<X it does not exclude a counterexample.

PROVED stability scope: if a set differs in at most E entries from such a nested set A*, then M(A)>=M(A*)-E and |A*|>=|A|-E. Consequently the bound survives o(X/N) Hamming errors when d,p0 stay bounded away from zero. Arbitrary o(X) modeling error is insufficient at this scale.

PROVED novelty check: PROOFS P29 contains the root-of-unity/Fejér density mechanism, and P63 contains subgroup restrictions; these ingredients are quoted. Searches for removal, roughness, and partial-period/homogenization statements did not find R12-N. The count-second-moment plus zero-class progression assembly and its exact n/r bound are new to the grepped project record. External priority is unchecked.

## Task 2 model and exact roughness identities

PROVED model definition. Let b_c(t)=1[c in E_t], 0<=t<=1, on Z_N with normalized Fourier coefficients

    e_s(t)=(1/N)*sum_c b_c(t)*exp(2*pi*i*s*c/N),
    p(t)=|E_t|/N, B_c(xi)=integral_0^1 b_c(t)*exp(i*xi*t)dt,
    Z_s(xi)=integral_0^1 e_s(t)*exp(i*xi*t)dt.

PROVED a finite realization is a piecewise constant schedule on time cells of length L/H, with N<<L<<H, where H is its ambient endpoint. On each cell of L consecutive integers the coefficient pattern is N-periodic; windows crossing a change are excluded from this local description. If there are J changes, summation on each residue progression gives f_A(2*pi*s/N+xi/H)=H*Re Z_s(xi)+O(N*(J+|xi|)); this is only a useful quantitative approximation when that error is smaller than the claimed dip. A continuum description by itself does not authorize ignoring this error. In the nested single-removal model the direct theorem R12-N is preferable and exact. When the final occupied frequency is smaller than H, X=max A remains the actual degree; H is only the scaling parameter.

PROVED general overlap identity, with no nestedness hypothesis:

    sum_{s!=0} |Z_s(xi)|^2
      = integral integral (|E_t intersect E_v|/N)*exp(i*xi*(t-v))dt dv
        - |integral p(t)*exp(i*xi*t)dt|^2.

PROVED proof: finite-character Parseval says sum_s e_s(t)*conj(e_s(v))=|E_t intersect E_v|/N; integrate and subtract s=0. The overlap kernel, not p(max(t,v)), is what replaces nestedness. The corresponding general increment identity is sum_s |e_s(t)-e_s(v)|^2=|E_t symmetric-difference E_v|/N. The formula is real and nonnegative even though the double-integral notation is complex.

PROVED real-part identity, needed for actual cosine values:

    sum_s (Re Z_s(xi))^2
      = (1/(2N))*sum_c (|B_c(xi)|^2+Re(B_c(xi)*B_{-c}(xi))).

PROVED proof: sum (Re Z)^2=(sum |Z|^2+Re sum Z^2)/2, and character orthogonality gives the two displayed terms. If E_t=-E_t for every t, then B_c=B_{-c} and this reduces to (1/N)*sum_c (integral b_c(t)cos(xi*t)dt)^2. Subtract (Re Z_0)^2 for the nonprincipal real energy. The mean across characters is exactly sum_s Re Z_s=Re B_0, which cannot be discarded.

PROVED nested specialization. If b_c(t)=1[0<=t<u_c], u_c in [0,1], let nu=(1/N)*sum_{u_c>0} delta_(u_c), so p(t)=nu((t,1]) for t>=0 and p0=nu((0,1]). Then, for xi!=0,

    sum_{s!=0}|Z_s|^2
      = integral 4*sin(xi*u/2)^2/xi^2 dnu(u) - |integral p(t)exp(i*xi*t)dt|^2.

PROVED for symmetric cutoffs u_c=u_{-c}, the corresponding real energy is

    sum_{s!=0}(Re Z_s)^2
      = integral sin(xi*u)^2/xi^2 dnu(u) - (integral p(t)cos(xi*t)dt)^2.

PROVED these formulas include atoms and a terminal atom at u=1. Writing dnu=-dp is valid in the Stieltjes sense, including boundary masses. For a continuum removal-time distribution nu with an L1 density (or with the explicitly needed oscillatory decay), integration by parts and Riemann–Lebesgue yield the following asymptotics for its energy functionals:

    xi^2*sum_{s!=0}|Z_s|^2 -> 2p0-p0^2,
    xi^2*sum_{s!=0}(Re Z_s)^2 -> p0/2  [symmetric case].

PROVED quantifier/order-of-limits clarification: if finite empirical removal measures nu_j converge weakly on [0,1] to the above absolutely continuous nu, first take j->infinity at each fixed xi in the exact formulas, then xi->infinity. Here p0 is the total mass of nu and it has no atom at zero. No joint-limit uniformity for xi=xi_j is asserted. A nonzero finite empirical measure itself is atomic and cannot have an L1 density.

PROVED correction: the brief's complex asymptotic coefficient 2p0 omits p0^2. A single cutoff u_c=u gives exact vanishing at xi=2*pi*j/u, so there is no unconditional pointwise asymptotic for a finite schedule. The exact increment identity for nested families is

    sum_s |e_s(t)-e_s(v)|^2=|p(t)-p(v)|.

PROVED this is an L2 vector metric statement. If a limiting p is differentiable with nonzero derivative, its square-root increment scale is |t-v|^(1/2). It does not assert that each individual finite-character envelope is Hölder-1/2: the finite envelopes are staircases and are discontinuous at removals. No stronger individual regularity claim is used.

PROVED failed roughness-to-minimum step: from positive complex energy alone one cannot infer negative real spikes; at xi=0, take E_t=H for t<u, zero afterward, where H is a subgroup. Then e_s(0)=p0*1[s in H-perp], so every real spike at that xi is nonnegative while nonprincipal energy is p0*(1-p0)*u^2>0. The exact mean is u when 0 is in H. R12-N recovers the dip at another xi through the zero-class progression.

## Task 1: completion of the cyclic barrier, with balance proved

PROVED cyclic homogenization lemma R12-H. Let q_j->infinity be odd primes and B_j=-B_j in Z_(q_j) have |B_j|/q_j->1/2. Let lambda_j(gamma)=sum_{c in B_j} exp(2*pi*i*gamma*c/q_j) and K_j=max(0,-min_gamma lambda_j(gamma)). If K_j=o(sqrt(q_j)), then for each fixed nonzero integer b,

    sup_{cyclic intervals I} |sum_{k in I}(1_Bj(b*k)-1/2)|/q_j -> 0.

PROVED in particular this gives local balance on every interval of length proportional to q_j, including intervals with moving endpoints. For every fixed rational angle theta=2*pi*a/b!=0 mod 2*pi and every continuous psi on [0,1],

    (1/q_j)*sum_{k=1}^{q_j} psi(k/q_j)*(2*1_Bj(k)-1)*exp(i*k*theta) -> 0.

PROVED proof of the homogenization lemma. It suffices to treat b=1, because multiplication by every fixed b is invertible modulo q_j eventually and permutes the nonprincipal eigenvalues. Extract a weak limit p(t)dt of the coefficient measures on R/Z. For each fixed integer Fourier mode its coefficient is nonnegative, since lambda/q>=-K/q->0. A bounded function on the circle with all Fourier coefficients nonnegative has a continuous PD representative: its Fejér sums at zero are bounded by its essential supremum, so monotone convergence sums all its nonnegative Fourier coefficients, and the Fourier series converges absolutely. Thus 0<=p<=1, p(0)=max p, and integral p=1/2.

PROVED cyclic energy-PD step (the finite analogue of P58–P59). Smooth the binary coefficient array by a normalized triangular coefficient kernel at a diagonal scale h_j->infinity, h_j/q_j->0, chosen so the smoothed array tends strongly in L2 to p. This diagonal exists by first taking fixed proportional smoothing and then sending its width to zero. Its eigenvalue multiplier L_j is in [0,1]. For r=b-smooth(b), define H_gamma=(1-L_j(gamma))*lambda(gamma)+K>=0. The inverse transform of H is r(k)+K*1[k=0]. Consequently convolution positivity gives

    Fourier(r^2)(gamma) >= -K^2-2K,

PROVED since |r(0)|<=1. Binary algebra and strong smoothing give r^2 weakly -> e=p(1-p). Dividing by q and using K^2/q->0 shows e is PD on the circle. The same Fejér argument makes e continuous and e(0)=max e.

PROVED finish: p(0)>=1/2. If p(0)>1/2, either p is constant (contradicting its mean) or p takes a value <=1/2. Continuity then gives a point where p=1/2 and e=1/4>p(0)(1-p(0)), contradicting energy-PD. Thus p(0)=1/2, p<=1/2, and its mean forces p identically 1/2. Every subsequential limit is constant. Bounded densities give uniform convergence of cumulative integrals, hence the displayed supremum over intervals. For the rational-angle statement, split k into the fixed b residue classes; k=r+b*l becomes a cyclic interval in the dilated array 1_B(b*l), with a possibly moving starting point r*b^(-1) mod q. Each class has half density up to o(q), so the nontrivial root-of-unity weighted sum is o(q). Approximate continuous psi by step functions. This also proves the assertion for every fixed subinterval and every fixed rational angle simultaneously after a countable diagonal.

PROVED cyclic barrier with exact quantifiers. Define asymptotic TBS as the assertion that there is c>0 such that every sequence of signs s_(j,k), 1<=k<Y_j, Y_j->infinity (extended evenly when a two-sided sequence is needed), satisfying

    Y_j^(-1)*sum_{alpha*Y_j<=k<beta*Y_j} s_(j,k) -> 0
    Y_j^(-1)*sum_{alpha*Y_j<=k<beta*Y_j} s_(j,k)*exp(i*k*theta) -> 0

PROVED hypotheses for every 0<=alpha<beta<=1 and every fixed nonzero rational theta, has liminf (-min_{Y_j^(-1/2)<=|x|<=pi} S_(Y_j)(x))/sqrt(Y_j)>=c. If TBS holds, then some absolute c'>0 satisfies -min_{gamma!=0}lambda_B(gamma)>=c'*sqrt(q) for all symmetric half-sets B in every odd prime group q>=5. Proof by contradiction for unbounded q: a failing cyclic square-root theorem gives K_j=o(sqrt(q_j)); set Y_j=q_j and use R12-H for both hypotheses and the exact Fejér identity for S>=-max(2K,1)/2-1/2, so its negative minimum divided by sqrt(Y) has limsup at most zero. The same proof works with Y_j=floor(alpha*q_j) for any fixed alpha in (0,1]. For bounded q>=5, a half-set is neither a subgroup nor the empty set, so it has a strictly negative eigenvalue by the classical 0/1-PD subgroup lemma; a finite minimum adjusts c'. The q=3, |B|=1 singleton subgroup is explicitly excluded.

PROVED corrections to the lead's reduction: (i) no tail estimate or repeated periods are needed; (ii) rational-atom removal is an asymptotic statement for every fixed denominator, not a cutoff b<L; (iii) the rate q^(-1/2)(b/L)^2 stated in the notes has not been derived and is unnecessary; (iv) local balance follows from K=o(sqrt(q)), binary algebra, and half density, not merely from a set having half cardinality.

PROVED integer front reduction with quantifiers. If a dense binary counterexample limit has p(0)=1/2, choose Y_j=epsilon_j*X_j with epsilon_j->0 sufficiently slowly that M_j=o(sqrt(Y_j)), Y_j->infinity, and every countable tested coefficient interval/rational twist on this shrinking front has its limiting zero-density defect. Continuity of p at zero and P63's vanishing rational profiles supply these conditions by a diagonal over fixed epsilon. The exact front bound then contradicts TBS. For a fixed positive epsilon the local density is p(epsilon*t), not exactly 1/2; the slow diagonal is necessary.

PROVED logical qualification: this proves that TBS excludes the exact endpoint a=1/2. It does not by itself supply a UNIVERSAL a*<1/2. That requires a uniform stability/separation statement. In particular p(0) is not continuous under weak profile convergence: a narrowing PD bump can retain its height at zero while its mass disappears. No unsupported compactness upgrade from endpoint exclusion to a uniform gap is made here.

## Task 1 deliverable (B): a precise coupled cyclic lemma sufficient beyond 1/D

CONJECTURED coupled support-front gap, CSFG(20). There exists eta in (0,1/2) with the following property. For every sequence of odd primes q_j->infinity and symmetric sets B_j in Z_(q_j), represented by centered residues, assume

    B_j is contained in {|c|<=q_j/4},
    |B_j|/q_j >= 1/80,
    K_j=max(0,-min_gamma lambda_Bj(gamma))=o(sqrt(q_j)).

CONJECTURED conclusion: every weak coefficient profile P(t) on R/Z has P(0)<=1/2-eta. Such profiles have continuous PD representatives, and P(1/2)=0, by the proof of R12-H and the support gap. This is a cyclic assertion with an explicit mandatory empty taper region; it is not the unrestricted prime-cyclic half-set conjecture. The same support gap makes the actual coefficient row vanish away from its front. No exact finite-group continuous binary interpolation is assumed.

PROVED conditional theorem R12-B. If CSFG(20) holds with eta, put a*=1/2-eta, sigma=4a*(1-a*)=1-4eta^2, and

    D_sigma=sup_{w in P61's W} integral_0^1 phi(sigma*|w(t)|^2)dt.

PROVED then T-dense(C) holds for every fixed C<min(20,1/D_sigma). Moreover D_sigma<=sigma*D<D, so this conditional range extends strictly beyond 1/D.

PROVED proof. Suppose first X<=20n and M=o(sqrt(X)). Choose a prime q in (4X,8X] and embed B=A union (-A) in centered Z_q. Then B is supported in |c|<=q/4, |B|/q=2n/q>=1/80, and lambda_B(gamma)=2f_A(2*pi*gamma/q)>=-2M. Pass to a subsequence q/X->u in [4,8]. If p is the integer coefficient profile, the cyclic profile is P(t)=p(u*|t|), extended by zero, so P(0)=p(0)=a. CSFG gives a<=a*. In the P61 Gabor argument, use the convex increasing function x->phi(sigma*x), rather than phi(x). Since 4e(0)=4a(1-a)<=sigma, the same Jensen argument gives d=integral p<=D_sigma. Thus d>=1/C contradicts C<1/D_sigma. Finally convexity and phi(0)=0 give phi(sigma*x)<=sigma*phi(x), hence D_sigma<=sigma D<D. The triangular generator has D>1/10 (use pi<16/5), so 1/D<10<20; truncating at C=20 still leaves a nonempty improvement beyond 1/D. All constants remain ineffective.

PROVED weakest version USED in this reduction: CSFG is needed only for the above embeddings, at density >=1/80, with front heights approaching 1/2; its conclusion can be replaced by the NONEXISTENCE of a sequence of such admissible limiting profiles whose front heights tend to 1/2. It is unnecessary to classify all cyclic half-sets, all support sizes, or all taper laws. The quantitative exclusion of an approaching sequence is essential; exclusion of an isolated exact endpoint is weaker. This is a precise sufficient coupled statement, not a proof of that statement or of a new unconditional T-dense range.

PROVED failure of exact finite TD-COUPLE as a meaningful quantitative formulation. On a fixed finite group, if every nonprincipal coefficient of 1_(E_t) is a continuous function of t, its centered indicator 1_(E_t)-|E_t|/N takes values in a finite set and is continuous, hence constant. Starting from a nonempty proper E_0, this forbids reaching the empty set at all. In particular continuous PD envelopes with exact binary laws make the proposed finite continuation class empty, regardless of K. Even an index-two subgroup fails to have such an exact taper. A usable finite-envelope lemma therefore needs an explicit approximation norm and error rate as N grows; this missing tolerance cannot be suppressed.

HEURISTIC strategic review after the front and roughness audits: the front-only route encounters an actual cyclic square-root implication, while the exact finite-envelope route is vacuous. Stop treating either as a proof of FRONT. Continue with the nonvacuous support-gap version above and with the exact nested X/N theorem. The remaining mechanism needed for unconditional progress is a quantitative binary continuation bound uniform over growing mesoscopic dimension; second-order positivity and unquantified continuity do not supply it.

## Task 2: arbitrary nonnested schedules refute a uniform X/N claim

PROVED nonnested counterexample theorem R12-U. There is a sequence A_X in [1,X], with |A_X|/X->1/4 and macroscopic profile p(t)=(1-t)/2, that is locally 2-periodic on cells of length L comparable to sqrt(X), but has M(A_X)=O(X^(3/4)*sqrt(log X))=o(X). Hence neither M>=c(d,p0)*X/N nor M>=c(d,p0)*X*sqrt(p0/N), with a positive constant depending only on d,p0, is true for ALL locally periodic nonnested schedules, even at N=2, p0=1/2, and limiting d=1/4. This is no counterexample to square-root Chowla: the displayed bound is much larger than sqrt(X).

PROVED construction and proof. Take X=T*L with T,L tending to infinity and L comparable to T. On cell j of L consecutive integers choose independently its entire contents with probability p_j=(1-(j-1/2)/T)/2, or choose none. Force the first cell instead to contain only its even integers and the last cell to be full; this costs at most 2L in the polynomial and ensures max A=X. Each other cell has E_t=Z_2 or the empty set, so the model is 2-periodic inside cells, and is not nested. The expected coefficient array differs in l1 by O(L) from the sampled triangular PD profile (1-k/(X+1))/2, whose cosine sum is >=-1/4. For the centered block error, each independent summand has magnitude at most L at every angle. Hoeffding on an O(X^3)-point circle grid, plus the deterministic derivative bound O(X^2), gives with probability tending to one

    sup_x |block_error(x)| <= C*sqrt(X*L*log X).

PROVED the cell count also concentrates and its weak macroscopic measures converge to p(t)dt, using a countable-test diagonal if desired. Thus a realization exists with the claimed density, profile, and global minimum bound. The first cell has exact local residue density 1/2; the continuous limiting profile also has p(0)=1/2. Since L/X->0, N<<L<<X holds. A global low-complexity assumption on the number of time changes is therefore indispensable if an X/N statement is meant outside the nested class.

NUMERICAL supporting VM probe, seed 2026101913: ambient endpoints H=65536, 262144, 1048576, with L=256,512,1024 and N=2, gave sampled M/H=0.0729651, 0.0360164, 0.0342205. These probes force only the first cell; the theorem's optional last-cell completion costs at most L. These are uncertified global estimates; the theorem above supplies the asymptotic all-circle upper bound. Independent 220-bit Arb evaluations certify the saved negative points, not an upper bound on their actual M. Exact run endpoints and grid indices are saved in `nonnested_X*.json`; the filename's X denotes the ambient H in this experiment.

## Task 2 adversarial VM search and certificate record

NUMERICAL reproducible search: `roughness_probe.py`, seed 2026101912, enumerates the specified structured families at N=29,61,127,257,64,128,256. The finite family list includes multiplicative coset orderings, Paley fronts with multiplicative/Bohr/random removals, subgroup-coset fronts with bit and Bohr removals, Bohr slices, and symmetric random fronts. Every saved cutoff is rational after exact reconstruction. The searched offset interval is 0<=xi<=200 on 1601 grid points, with bounded one-dimensional refinement at the 12 lowest sampled offsets. Values outside this interval and missed grid dips can only increase the true negative minimum. No grid supplies a global nonnegativity certificate.

NUMERICAL strongest sampled schedules by N (including the two Gurobi searches below):

| N | Family | sampled mu=-min Re Z | sampled mu*sqrt(N) | minimizing xi |
| --- | --- | ---: | ---: | ---: |
| 29 | Gurobi nested | 0.04609249 | 0.2482157 | 0 |
| 61 | Gurobi nested | 0.03342734 | 0.2610759 | 0 |
| 64 | coset + Bohr removal | 0.03867761 | 0.3094209 | 5.187108 |
| 127 | Bohr + random removal | 0.03883570 | 0.4376561 | 0 |
| 128 | coset + Bohr removal | 0.04068652 | 0.4603154 | 5.187388 |
| 256 | Bohr + random removal | 0.04014525 | 0.6423240 | 0 |
| 257 | Bohr + random removal | 0.03094494 | 0.4960852 | 0 |

NUMERICAL MILP details: `schedule_milp.py`, Gurobi 13.0.3, four threads, seed 1912. Each nonzero +/- residue pair is assigned to one removal time or is absent; the zero residue is absent. N=29 uses seven time levels (j+1/2)/7, one active pair per level. N=61 uses five levels, three active pairs per level. The constraints impose Re Z_s(xi)>=-mu for every independent character and the union of 121 equally spaced offsets in [0,60] with 20 equally spaced offsets in [0.1,4]. N=29 was solved to the solver's numerical optimality tolerance in 4.07 seconds, objective 0.046092493. N=61 hit its 55-second limit, incumbent 0.0334273425 and solver lower bound 0.0132331847. These are floating MILP results for the finite discretized class, not exact global optima and not theorems about all schedules. The later wider-offset probe found no worse dip for these incumbents, which is only numerical evidence.

PROVED point-certificate examples, reconstructed from the saved cutoffs and independently evaluated at 220 bits:

| Model | N | ambient H | n | certified actual value less than |
| --- | ---: | ---: | ---: | ---: |
| Gurobi nested | 29 | 118784 | 28671 | -5474 |
| Gurobi nested | 61 | 249856 | 61442 | -8351 |
| coset + Bohr removal | 64 | 262144 | 65537 | -10139 |
| Bohr + random removal | 257 | 1052672 | 264192 | -32574 |

PROVED these are actual finite binary sets defined by k<=floor(H*u_(k mod N)); all frequencies are distinct positive integers. The table's ambient H is the Riemann-sum endpoint, not necessarily X=max A. The certificates use exact residue counts at root angles, or finite-geometric-sum identities at a rational offset xi/H. `independent_checks.json` contains the enclosing Arb balls and model errors, and `final_audit.json` records the actual maxima. No apparent small value of a sampled minimum is used to prove a counterexample. All tested structured removal families fail to evade square-root-sized negative spikes at these finite parameters; this is a bounded negative search, not a universal X*sqrt(p0/N) theorem.

NUMERICAL identities were cross-checked by independent direct character sums and FFTs: maximum general real-Parseval residual 8.4e-17 and Fejér-transfer residual 1.5e-14. Exact rational checks of the root-count second moment passed for 980 independently generated count arrays, N=1,...,49. These finite checks support the separate paper proofs. The subgroup example above shows that positive concentration at an individual offset is real, so it was preserved as an obstruction to the proposed one-offset argument rather than dismissed by the search.

PROVED excluded structures, with scope: all nested initial-column schedules with N=o(sqrt(X)) at positive density; their o(X/N)-Hamming perturbations; and, by finite Arb point dips, the six explicitly saved schedule realizations. Not excluded: arbitrary nonnested schedules; nested schedules with sqrt(X)<<N<<X; near-periodic fronts with N comparable to X; and growing-rank Bohr structures outside this residue model. The conjectured X*sqrt(p0/N) bound remains unresolved in the nested class and is refuted in the unrestricted nonnested class.

## Task 3: conditional exponent and a precise scalar barrier

PROVED quoted normalization for line D. For an even sign function g:Z_p->{-1,1}, take g(0)=-1 and lambda>=max(0,-min ghat), set h=ghat+lambda>=0, and use UNNORMALIZED convolution on Z_p. Then

    sum h=p*(lambda-1),
    sum h^2=p^2+p*lambda*(lambda-2),
    h*h=p^2*delta_0+p*lambda*(lambda-2)*1,
    h*h*h=p^2*h+p^2*lambda*(lambda-1)*(lambda-2)*1.

PROVED these follow by Fourier inversion from g^2=1; the corresponding project identities are kernel-checked in P26/line D. The half-set condition is |sum g|=1; it fixes h(0)=lambda+/-1. Toggling the point 0, when needed, changes the set eigenvalues by at most one and does not affect an asymptotic exponent. The special case h(0)=lambda-1 is used for the barrier below.

CONJECTURED missing peak lemma PK(eta), explicitly named: there exist eta in (0,1] and C>0 such that every symmetric prime-cyclic half-set sign array in this normalization, with lambda>=2 its actual negative spectral threshold, satisfies max h<=C*lambda^(2-eta).

PROVED conditional exponent: PK(eta) implies lambda>=(p/C)^(1/(3-eta)) for lambda>=2, hence a prime half-set exponent theta=1/(3-eta)>1/3. Indeed sum h^2>=p^2 and sum h<=p*lambda, so p^2<=max(h)*sum h<=C*p*lambda^(3-eta). At eta=1 it would give square-root strength. This is a consequence of a missing lemma, not a claimed exponent improvement. The existing cubic spectral peak bound quoted in the brief does not imply PK(eta).

PROVED scalar-relaxation barrier R12-S: for every sufficiently large odd prime p (for example p>=10^6), write lambda=p^(1/3), h0=lambda-1,

    T=p*(lambda-1), E=p^2+p*lambda*(lambda-2),
    T'=T-h0, E'=E-h0^2,
    m=4*ceil(T'^2/(4E')),
    H=T'/m, v=E'/m-H^2.

PROVED choose m nonzero residues in +/- pairs; on half of these pairs put H+sqrt(v), on the others H-sqrt(v); set all remaining nonzero entries to zero and h(0)=h0. Then h is nonnegative and symmetric, and has EXACT sum T and squared sum E. For lambda>=100, T'^2/E' is comparable to lambda^2, m differs from it by less than four, and 0<=v<=H^2. Thus m<p-1 and the assignment exists. The elementary bounds H<=2p/lambda and max h<=2H<=4p/lambda imply

    h(gamma)^2<=p*lambda*(lambda-2) for gamma!=0,
    max h<=lambda^3/2.

PROVED for clarity, the first inequality follows from 16p^2/lambda^2 <= p*lambda*(lambda-2) when lambda>=100; the second from 4p/lambda<=p/2. These arrays therefore satisfy the exact scalar mass, energy, front value, symmetry, the individual off-zero square bound, and even a stronger version of the quoted cubic peak bound, at exponent exactly 1/3. Also z=h-lambda has z(0)=-1, sum z=-p and sum z^2=p^2, as required by the corresponding scalar sign identities.

PROVED implication of this example: NO argument retaining only those scalar deductions from line D can force an exponent strictly above 1/3. The missing information is the FULL off-zero convolution equation (or an equally strong arithmetic/binary substitute). The constructed h generally FAILS that equation and is not asserted to be the Fourier transform of a binary half-set. Thus this is a rigorous barrier to the specified scalar relaxation, not to all uses of line D and not a conditional Chowla counterexample. The same example violates every PK(eta) in the relaxed class, since max h has order p^(2/3)=lambda^2.

PROVED verification scope: `independent_check.py` reconstructs the scalar mass and energy exactly using rational lambda=10,20,50,100 and p=lambda^3, and verifies the sufficient rational inequalities. Those finite index sizes are not claimed prime; the displayed formula and inequalities are the proof for all sufficiently large prime p as well. PROOFS searches for peak, subquadratic, scalar moment, and approximate flatness did not find this barrier assembly. No external priority claim is made.

## Task 3: bounded literature check, exact versions and hypotheses

PROVED quoted, source-verified: [Sanders, arXiv:0807.5104v2, 14 October 2010](https://arxiv.org/pdf/0807.5104v2), Theorem 1.2, applies to every symmetric B in Z_p of size (p+1)/2 and gives a polynomial negative Fourier coefficient; the next sentence specifies exponent 1/3. In unnormalized set eigenvalues, some absolute c>0 gives -min_gamma lambda_B(gamma)>=c*p^(1/3). Theorem 1.3 is a positive-density finite-abelian-group distance-to-a-subgroup theorem. Neither statement is a square-root result. The (p-1)/2 convention differs by toggling 0 and an O(1) eigenvalue change when the parity permits, so it has the same asymptotic exponent.

PROVED quoted, relevant 2025 finite-group result: [Jin–Milojević–Tomon–Zhang, arXiv:2509.03490v2, 27 October 2025](https://arxiv.org/html/2509.03490v2#A1), Theorem A.1, states that for every delta>0 and 0<gamma<1/4, sufficiently large finite groups have the following property: an inverse-closed set with negative spectral threshold at most |G|^gamma is within delta*|G| of a subgroup. Its second part gives polynomial proximity for gamma<1/6. This extends to nonabelian groups and does not improve Sanders' prime half-set exponent 1/3. The theorem and its parameter range, rather than an inference from the paper title, were checked.

PROVED quoted, 2026 cross-check: [Bu et al., arXiv:2610.17160v1, 12 October 2026](https://arxiv.org/html/2610.17160v1#S9.SS2), Section 9.2, explicitly compares its dense-integer exponent 1/4 with Sanders' prime half-set exponent 1/3. Proposition 9.7 gives, for every C>=1 and every n>=2 with A in [1,Cn],

    M(A) >= ((n-1)/(64*C*C1))^(1/4), C1=200000.

PROVED quoted scope distinction: [Bedert, arXiv:2509.05260v3, revised 24 July 2026](https://arxiv.org/html/2509.05260v3), Theorem 1.1, gives the universal integer-frequency exponent 1/5-o(1). [Shankar, arXiv:2609.05338v1, 4 September 2026](https://arxiv.org/abs/2609.05338v1) states the log-free c*n^(1/5) bound for every finite positive-integer set. These are integer statements, not improvements of the prime-cyclic half-set exponent. Their versions and statement scopes were checked; their full proofs were not re-audited in this round.

PROVED search-scope statement: a short search for 2024–2026 prime half-sets, dense Chowla and cyclic cosine bounds found no primary-source theorem improving the half-set exponent beyond 1/3. The 2025 finite-group theorem and the October 2026 explicit comparison were obtained and read at the cited statements. This bounded search does not prove that no other improvement exists. No claim of exhaustive literature coverage is made.

## Final audit, novelty, and handoff

PROVED new to the grepped PROJECT record: R12-H, including the balance/rational-atom proof for hypothetical small-negative-spectrum prime half-sets; the exact assembly R12-N and its n/r bound for arbitrary nested removals; R12-U refuting the unrestricted periodic X/N formulation; the real-part roughness identity and the corrected 2p0-p0^2 asymptotic; the finite exact-envelope vacuity audit; the quantified CSFG(20) implication with D_sigma; and the scalar barrier R12-S. The root filter, ordinary Parseval, interval Dirichlet formula, binary high-pass energy mechanism, PD continuity/subgroup lemma, P61's Gabor/Jensen machinery and existing dense endpoint are quoted/classical ingredients. The partial-period observation was proposed by the lead and is VERIFIED here, not claimed as this round's discovery. External priority of the new assemblies is unchecked.

PROVED failed or unsupported steps preserved with their precise obstruction:

- Complex roughness equals negative cosine energy: false; the real-part identity and the subgroup positive-spike example show the missing information.
- Complex nonprincipal roughness has coefficient 2p0: false under the stated smooth limit; subtracting the zero character leaves 2p0-p0^2. Finite synchronized cutoffs also defeat pointwise asymptotics.
- Individual envelopes are forced to be Hölder-1/2: false as stated for finite removal staircases; only the vector increment identity is proved.
- Local balance or rational-atom decay follows from half cardinality alone: not justified; R12-H supplies the necessary small-spectrum/binary argument. The advertised explicit rational-correlation rate is not used or claimed.
- Fixed small epsilon gives an exactly balanced integer front: false in general; its profile is p(epsilon*t). A slow epsilon->0 diagonal repairs the reduction.
- Excluding the exact front endpoint automatically gives a uniform a*<1/2: not justified; weak convergence need not preserve the value at zero. CSFG explicitly includes the required uniform separation.
- Exact continuous finite-group PD-envelope binary taper is a nonvacuous class: false; continuity into a finite set prevents every nontrivial taper.
- The X/N and X*sqrt(p0/N) bounds hold for all locally periodic nonnested schedules: false by R12-U, even with fixed N=2 and positive limiting density.
- The scalar mass/energy/symmetry/gap deductions alone improve the cyclic exponent beyond 1/3: false by R12-S. Its failure of full convolution flatness is explicitly retained.

PROVED final outcome by task: (1) alternative (B), with a fully quantified conditional cyclic support-gap lemma and resulting range C<min(20,1/D_sigma); no unconditional front gap. (2) exact identities and unconditional nested X/N theorem, unrestricted-nonnested counterexample, bounded structured searches and Arb point certificates; nested X*sqrt(p0/N) remains unresolved. (3) PK(eta)'s conditional exponent and the scalar-relaxation barrier, plus verified literature statements; no unconditional exponent improvement.

HEURISTIC global review and decision: continue with three mathematically distinct directions: (i) quantify the mandatory support/taper gap in CSFG, using exact off-zero convolution rather than scalar moments; (ii) extend the zero-class argument from one removal per residue to bounded repeated entrance/exit schedules, explicitly tracking their number; (iii) test candidate subquadratic peak bounds against genuine cyclic optima and exact convolution, using the scalar fake as a rejection test for insufficient hypotheses. Stop certificate tightening and unqualified Brownian-roughness arguments in this round. The first concrete next derivation is a quantitative version of R12-N for a zero residue class that is a union of J intervals: determine the optimal dependence on J, and test whether a bound survives at J comparable to X/N without becoming the full Chowla problem. No unattended continuation is implied.

PROVED reproducibility commands (from the project root):

```sh
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -t 300 python .research/agents/tdense12_scratch/roughness_probe.py
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -t 160 python .research/agents/tdense12_scratch/schedule_milp.py
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -t 240 python .research/agents/tdense12_scratch/independent_check.py
DIRICHLET_IP=34.148.157.169 src/dirun.sh -c 4 -t 90 python .research/agents/tdense12_scratch/final_audit.py
```

PROVED artifact verification record: Python 3.12.3, NumPy version stored in `roughness_results.json`, Gurobi 13.0.3 for both MILPs, Arb precision 220 bits. `independent_checks.json` records 980 exact count checks, six independently enclosed continuum/finite-set dips, four scalar arithmetic checks and three nonnested probe records. `final_audit.json` confirms every previous source/data hash, successful compilation of all four scripts, 64 independent Arb progression checks, 36 structured schedules, the 140-offset MILP grid, and the actual maximum frequency of every certified set. `manifest.json` contains the final source/data SHA256 values. These are paper proofs plus finite exact/Arb checks, not Lean kernel proofs. All mathematical jobs used the required VM wrapper with four cores. No commits, subagents, root research-record edits or LaTeX artifacts were made by this round.
