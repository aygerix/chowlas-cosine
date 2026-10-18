import ChowlaCosine

open ChowlaCosine

-- 1. Difference-set identity
#check @norm_sq_sum_exp
#print axioms norm_sq_sum_exp
-- 2. Sidon consequence
#check @cosSum_diffSet_ge_of_sidon
#print axioms cosSum_diffSet_ge_of_sidon
#check @card_diffSet_of_sidon
#print axioms card_diffSet_of_sidon
#check @diffSet_pos
#print axioms diffSet_pos
#check @two_mul_card_ltPairs
#print axioms two_mul_card_ltPairs
#check @sidon_diffSet_main
#print axioms sidon_diffSet_main
-- 3. Mean zero and Parseval
#check @integral_cosSum
#print axioms integral_cosSum
#check @integral_cosSum_sq
#print axioms integral_cosSum_sq
#check @normalized_mean_sq
#print axioms normalized_mean_sq
-- 4. Intersection lemma
#check @cosSum_inter_ge
#print axioms cosSum_inter_ge
#check @cosSum_inter_ge'
#print axioms cosSum_inter_ge'
-- 5. Cube framework
#check @sum_prod_two_cos_eq_cubeSum
#print axioms sum_prod_two_cos_eq_cubeSum
#check @multilinPoly_min_at_vertex
#print axioms multilinPoly_min_at_vertex
#check @multilinPoly_min_at_vertex_two
#print axioms multilinPoly_min_at_vertex_two
#check @cubeSum_min
#print axioms cubeSum_min
-- 6. Star / induced-subgraph lemma (P9)
#check @integral_cos_nat_mul_cos_int
#print axioms integral_cos_nat_mul_cos_int
#check @quadTrig_eq
#print axioms quadTrig_eq
#check @integral_quadTrig
#print axioms integral_quadTrig
#check @integral_cosSum_mul_quadTrig
#print axioms integral_cosSum_mul_quadTrig
#check @star_lemma
#print axioms star_lemma
#check @nonneg_of_cosSum_ge
#print axioms nonneg_of_cosSum_ge
#check @star_bound
#print axioms star_bound
-- 7. Multiplicity bound for square certificates (P8)
#check @norm_sq_eq_sqTrig
#print axioms norm_sq_eq_sqTrig
#check @Rp_le
#print axioms Rp_le
#check @lam_eq_of_sq_certificate
#print axioms lam_eq_of_sq_certificate
#check @coeff_eq_one_of_sq_certificate
#print axioms coeff_eq_one_of_sq_certificate
#check @card_pairs_natAbs_le
#print axioms card_pairs_natAbs_le
#check @card_le_of_sq_certificate
#print axioms card_le_of_sq_certificate
#check @card_le_of_sq_certificate'
#print axioms card_le_of_sq_certificate'
-- 8. Averaging over q-th roots of unity
#check @sum_range_cos_shift
#print axioms sum_range_cos_shift
#check @sum_cosSum_shift
#print axioms sum_cosSum_shift
#check @averaging_identity
#print axioms averaging_identity
#check @cosSum_filter_dvd_ge
#print axioms cosSum_filter_dvd_ge
#check @card_sub_le_of_cosSum_ge
#print axioms card_sub_le_of_cosSum_ge
#check @le_of_cosSum_ge_mixed
#print axioms le_of_cosSum_ge_mixed
#check @card_le_of_no_multiples
#print axioms card_le_of_no_multiples
#check @card_le_of_no_multiples'
#print axioms card_le_of_no_multiples'
