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
-- 9. P16: half-integer square structure of Bu et al.'s sets (HalfSquare.lean)
#check @cosSum_buSet
#print axioms cosSum_buSet
#check @cosSum_buSet_of_sidon
#print axioms cosSum_buSet_of_sidon
#check @two_sum_pairs_half
#print axioms two_sum_pairs_half
#check @halfP_sq_sub_sum_sq
#print axioms halfP_sq_sub_sum_sq
#check @sum_cos_half_sq
#print axioms sum_cos_half_sq
#check @injOn_buSet_diff
#print axioms injOn_buSet_diff
#check @injOn_buSet_sum
#print axioms injOn_buSet_sum
#check @buSet_pos
#print axioms buSet_pos
#check @card_buSet
#print axioms card_buSet
#check @sidon_quad_count
#print axioms sidon_quad_count
#check @integral_halfC_pow_four
#print axioms integral_halfC_pow_four
#check @normalized_halfC_pow_four
#print axioms normalized_halfC_pow_four
#check @integral_halfC_pow_four_le
#print axioms integral_halfC_pow_four_le
#check @integral_cos_mul_triK
#print axioms integral_cos_mul_triK
#check @integral_cos_mul_triK_real
#print axioms integral_cos_mul_triK_real
#check @integral_triK
#print axioms integral_triK
#check @visit_lemma
#print axioms visit_lemma
#check @exists_visit_of_sinc_sum_lt
#print axioms exists_visit_of_sinc_sum_lt
#check @halfC_periodic
#print axioms halfC_periodic
#check @abs_halfC_sub_le
#print axioms abs_halfC_sub_le
#check @halfSquare_lower_bound_of_visit
#print axioms halfSquare_lower_bound_of_visit
#check @halfSquare_lower_bound
#print axioms halfSquare_lower_bound
#check @sinc_sq_le_min
#print axioms sinc_sq_le_min
#check @halfSquare_lower_bound_min
#print axioms halfSquare_lower_bound_min
-- 10. P16 explicit (Sidon counting, rank majorant, unconditional final theorem)
#check @IsSidon.mono
#print axioms IsSidon.mono
#check @injOn_sub_ltPairs_of_sidon
#print axioms injOn_sub_ltPairs_of_sidon
#check @sidon_card_mul_pred_le_of_diam
#print axioms sidon_card_mul_pred_le_of_diam
#check @sidon_card_mul_pred_le_of_Ico
#print axioms sidon_card_mul_pred_le_of_Ico
#check @le_one_add_sqrt_of_mul_pred_le
#print axioms le_one_add_sqrt_of_mul_pred_le
#check @sidon_card_le_one_add_sqrt_of_Ico
#print axioms sidon_card_le_one_add_sqrt_of_Ico
#check @sidon_card_mul_pred_le_real
#print axioms sidon_card_mul_pred_le_real
#check @card_filter_abs_half_le
#print axioms card_filter_abs_half_le
#check @card_filter_abs_half_le_sqrt
#print axioms card_filter_abs_half_le_sqrt
#check @absB_injective
#print axioms absB_injective
#check @absB_pos
#print axioms absB_pos
#check @rankB_lt_rankB
#print axioms rankB_lt_rankB
#check @rankB_injOn
#print axioms rankB_injOn
#check @rankB_lt_card
#print axioms rankB_lt_card
#check @rankB_bound
#print axioms rankB_bound
#check @one_div_sq_sq_le
#print axioms one_div_sq_sq_le
#check @telG_nonneg
#print axioms telG_nonneg
#check @sum_range_telG_le
#print axioms sum_range_telG_le
#check @min_le_telG
#print axioms min_le_telG
#check @sum_min_absB_le
#print axioms sum_min_absB_le
#check @sum_min_le_sidon
#print axioms sum_min_le_sidon
#check @halfSquare_hcond_explicit
#print axioms halfSquare_hcond_explicit
#check @halfSquare_lower_bound_explicit
#print axioms halfSquare_lower_bound_explicit
#check @halfSquare_lower_bound_explicit'
#print axioms halfSquare_lower_bound_explicit'
-- 11. P16' (rate exponent 1/5): Gallagher large sieve (HalfSquareSieve.lean)
#check @gallagher_local
#print axioms gallagher_local
#check @sum_integral_le_of_sorted
#print axioms sum_integral_le_of_sorted
#check @gallagher_sum
#print axioms gallagher_sum
#check @continuous_halfS
#print axioms continuous_halfS
#check @halfS_periodic
#print axioms halfS_periodic
#check @hasDerivAt_halfC
#print axioms hasDerivAt_halfC
#check @cc_nonneg
#print axioms cc_nonneg
#check @sin_mul_sin_int
#print axioms sin_mul_sin_int
#check @integral_cos_cos_mul_sin_mul_sin
#print axioms integral_cos_cos_mul_sin_mul_sin
#check @sum_sq_mul_sum_sq
#print axioms sum_sq_mul_sum_sq
#check @integral_halfC_sq_mul_halfS_sq_le
#print axioms integral_halfC_sq_mul_halfS_sq_le
#check @integral_abs_halfC_cube_mul_halfS_le
#print axioms integral_abs_halfC_cube_mul_halfS_le
#check @sieve_halfC_pow_four
#print axioms sieve_halfC_pow_four
#check @halfP_visit_explicit
#print axioms halfP_visit_explicit
#check @sieve_numerics
#print axioms sieve_numerics
#check @sieve_arith
#print axioms sieve_arith
#check @halfSquare_lower_bound_sieve
#print axioms halfSquare_lower_bound_sieve
#check @halfSquare_lower_bound_sieve'
#print axioms halfSquare_lower_bound_sieve'
