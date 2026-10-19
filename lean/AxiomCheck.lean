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
-- 12. P21: |B_t| = p³ with every t-line a single (p−1)-run and min F ≥ −3p (RunTopGroup.lean)
#check @ChowlaCosine.RunTopGroup.runSet_neg
#print axioms ChowlaCosine.RunTopGroup.runSet_neg
#check @ChowlaCosine.RunTopGroup.zero_not_mem_runSet
#print axioms ChowlaCosine.RunTopGroup.zero_not_mem_runSet
#check @ChowlaCosine.RunTopGroup.card_line_inter
#print axioms ChowlaCosine.RunTopGroup.card_line_inter
#check @ChowlaCosine.RunTopGroup.card_runTops
#print axioms ChowlaCosine.RunTopGroup.card_runTops
#check @ChowlaCosine.RunTopGroup.charSum_lower
#print axioms ChowlaCosine.RunTopGroup.charSum_lower
-- 13. P21 diagnosis: negative-definite fibre lemma (NegDefFibre.lean)
#check @ChowlaCosine.NegDefFibre.le_two_mul_card_of_negDef
#print axioms ChowlaCosine.NegDefFibre.le_two_mul_card_of_negDef

-- 14. P31: exact moments, Fejér positivity and CONDITIONAL window inequality.
-- FejerRiesz is an explicit extra hypothesis, not a proved theorem or new axiom.
#check @ChowlaCosine.P31.circleMean_weightedCos_mul
#print axioms ChowlaCosine.P31.circleMean_weightedCos_mul
#check @ChowlaCosine.P31.circleMean_shifted_weightedCos_sq
#print axioms ChowlaCosine.P31.circleMean_shifted_weightedCos_sq
#check @ChowlaCosine.P31.circleMean_fejerKernel_sq
#print axioms ChowlaCosine.P31.circleMean_fejerKernel_sq
#check @ChowlaCosine.P31.circleMean_cosSum_add_sq
#print axioms ChowlaCosine.P31.circleMean_cosSum_add_sq
#check @ChowlaCosine.P31.circleMean_swap
#print axioms ChowlaCosine.P31.circleMean_swap
#check @ChowlaCosine.P31.circleMean_window_sq
#print axioms ChowlaCosine.P31.circleMean_window_sq
#check @ChowlaCosine.P31.averaged_window_bound
#print axioms ChowlaCosine.P31.averaged_window_bound
#check @ChowlaCosine.P31.fejer_triangle_sq
#print axioms ChowlaCosine.P31.fejer_triangle_sq
#check @ChowlaCosine.P31.fejerKernel_nonneg
#print axioms ChowlaCosine.P31.fejerKernel_nonneg
#check @ChowlaCosine.P31.window_nonneg
#print axioms ChowlaCosine.P31.window_nonneg
#check @ChowlaCosine.P31.circleMean_fejerKernel_mul_cos
#print axioms ChowlaCosine.P31.circleMean_fejerKernel_mul_cos
#check @ChowlaCosine.P31.circleMean_window
#print axioms ChowlaCosine.P31.circleMean_window
#check @ChowlaCosine.P31.circleMean_window_mean_sq
#print axioms ChowlaCosine.P31.circleMean_window_mean_sq
#check @ChowlaCosine.P31.p31_of_window_bound
#print axioms ChowlaCosine.P31.p31_of_window_bound
#check @ChowlaCosine.P31.p31_of_factorization
#print axioms ChowlaCosine.P31.p31_of_factorization
#check @ChowlaCosine.P31.trigBand_mul
#print axioms ChowlaCosine.P31.trigBand_mul
#check @ChowlaCosine.P31.cos_shift_mem_trigBand
#print axioms ChowlaCosine.P31.cos_shift_mem_trigBand
#check @ChowlaCosine.P31.fejer_shift_mem_trigBand
#print axioms ChowlaCosine.P31.fejer_shift_mem_trigBand
#check @ChowlaCosine.P31.cosSum_add_mem_trigBand
#print axioms ChowlaCosine.P31.cosSum_add_mem_trigBand
#check @ChowlaCosine.P31.p31_of_fejerRiesz
#print axioms ChowlaCosine.P31.p31_of_fejerRiesz
#check @ChowlaCosine.P31.p31_main_of_fejerRiesz
#print axioms ChowlaCosine.P31.p31_main_of_fejerRiesz
#check @ChowlaCosine.P31.windowMass_eq
#print axioms ChowlaCosine.P31.windowMass_eq
#check @ChowlaCosine.P31.windowMass_pos
#print axioms ChowlaCosine.P31.windowMass_pos

-- 15. P31 T1 partial: zero degree, root pairing and a conditional compactness reduction.
#check @ChowlaCosine.P31.fejerRiesz_zero
#print axioms ChowlaCosine.P31.fejerRiesz_zero
#check @ChowlaCosine.P31.rootReflection_rootReflection
#print axioms ChowlaCosine.P31.rootReflection_rootReflection
#check @ChowlaCosine.P31.root_pair_identity
#print axioms ChowlaCosine.P31.root_pair_identity
#check @ChowlaCosine.P31.factorization_of_bounded_approximation
#print axioms ChowlaCosine.P31.factorization_of_bounded_approximation
#check @ChowlaCosine.P31.root_partition_off_circle
#print axioms ChowlaCosine.P31.root_partition_off_circle
#check @ChowlaCosine.P31.root_partition_of_even_fixed
#print axioms ChowlaCosine.P31.root_partition_of_even_fixed
#check @ChowlaCosine.P31.root_product_identity
#print axioms ChowlaCosine.P31.root_product_identity

-- 16. Finite Fejér–Riesz and T3 with factorization DISCHARGED.
#check @ChowlaCosine.P31.analyticValue_coeff
#print axioms ChowlaCosine.P31.analyticValue_coeff
#check @ChowlaCosine.P31.factorization_of_polynomial_norm
#print axioms ChowlaCosine.P31.factorization_of_polynomial_norm
#check @ChowlaCosine.P31.factorization_of_root_data
#print axioms ChowlaCosine.P31.factorization_of_root_data
#check @ChowlaCosine.P31.factorization_of_polynomial_root_conditions
#print axioms ChowlaCosine.P31.factorization_of_polynomial_root_conditions
#check @ChowlaCosine.P31.even_of_local_nonnegative_power
#print axioms ChowlaCosine.P31.even_of_local_nonnegative_power
#check @ChowlaCosine.P31.analyticOrderNatAt_even_of_nonneg
#print axioms ChowlaCosine.P31.analyticOrderNatAt_even_of_nonneg
#check @ChowlaCosine.P31.even_of_local_nonnegative_complex_power
#print axioms ChowlaCosine.P31.even_of_local_nonnegative_complex_power
#check @ChowlaCosine.P31.unit_circle_rootMultiplicity_even_at_angle
#print axioms ChowlaCosine.P31.unit_circle_rootMultiplicity_even_at_angle
#check @ChowlaCosine.P31.unit_circle_rootMultiplicity_even
#print axioms ChowlaCosine.P31.unit_circle_rootMultiplicity_even
#check @ChowlaCosine.P31.factorization_of_polynomial_root_symmetry
#print axioms ChowlaCosine.P31.factorization_of_polynomial_root_symmetry
#check @ChowlaCosine.P31.root_symmetry_of_real_circle_representation
#print axioms ChowlaCosine.P31.root_symmetry_of_real_circle_representation
#check @ChowlaCosine.P31.exists_shifted_polynomial
#print axioms ChowlaCosine.P31.exists_shifted_polynomial
#check @ChowlaCosine.P31.analytic_factor_mono
#print axioms ChowlaCosine.P31.analytic_factor_mono
#check @ChowlaCosine.P31.shifted_polynomial_reflection
#print axioms ChowlaCosine.P31.shifted_polynomial_reflection
#check @ChowlaCosine.P31.shifted_polynomial_coeff_symmetry
#print axioms ChowlaCosine.P31.shifted_polynomial_coeff_symmetry
#check @ChowlaCosine.P31.finite_fejerRiesz
#print axioms ChowlaCosine.P31.finite_fejerRiesz
#check @ChowlaCosine.P31.finite_fejerRiesz_of_coefficients
#print axioms ChowlaCosine.P31.finite_fejerRiesz_of_coefficients
#check @ChowlaCosine.P31.p31_main
#print axioms ChowlaCosine.P31.p31_main

-- 17. P31-E: exact integral certificate, E1/E2, all finite unit vectors.
#check @ChowlaCosine.P31.elementaryWeight_pos
#print axioms ChowlaCosine.P31.elementaryWeight_pos
#check @ChowlaCosine.P31.elementary_integral_constant
#print axioms ChowlaCosine.P31.elementary_integral_constant
#check @ChowlaCosine.P31.elementaryCellWeight_pos
#print axioms ChowlaCosine.P31.elementaryCellWeight_pos
#check @ChowlaCosine.P31.integral_elementaryWeight
#print axioms ChowlaCosine.P31.integral_elementaryWeight
#check @ChowlaCosine.P31.elementary_cell_reciprocal_bound
#print axioms ChowlaCosine.P31.elementary_cell_reciprocal_bound
#check @ChowlaCosine.P31.elementary_bound_of_two_estimates
#print axioms ChowlaCosine.P31.elementary_bound_of_two_estimates
#check @ChowlaCosine.P31.discreteEnergy_le_pairCount
#print axioms ChowlaCosine.P31.discreteEnergy_le_pairCount
#check @ChowlaCosine.P31.discreteEnergy_le_sum_sq
#print axioms ChowlaCosine.P31.discreteEnergy_le_sum_sq
#check @ChowlaCosine.P31.pairCount_le_distance
#print axioms ChowlaCosine.P31.pairCount_le_distance
#check @ChowlaCosine.P31.massPrefix_zero
#print axioms ChowlaCosine.P31.massPrefix_zero
#check @ChowlaCosine.P31.massPrefix_total
#print axioms ChowlaCosine.P31.massPrefix_total
#check @ChowlaCosine.P31.massPrefix_bounds
#print axioms ChowlaCosine.P31.massPrefix_bounds
#check @ChowlaCosine.P31.massPrefix_step
#print axioms ChowlaCosine.P31.massPrefix_step
#check @ChowlaCosine.P31.distance_mass_identity
#print axioms ChowlaCosine.P31.distance_mass_identity
#check @ChowlaCosine.P31.massPrefix_trapezoid_sum
#print axioms ChowlaCosine.P31.massPrefix_trapezoid_sum
#check @ChowlaCosine.P31.discreteEnergy_le_cumulative
#print axioms ChowlaCosine.P31.discreteEnergy_le_cumulative
#check @ChowlaCosine.P31.elementary_discreteEnergy_bound
#print axioms ChowlaCosine.P31.elementary_discreteEnergy_bound
#check @ChowlaCosine.P31.discreteEnergy_eq_convolution
#print axioms ChowlaCosine.P31.discreteEnergy_eq_convolution
#check @ChowlaCosine.P31.elementary_convolution_bound
#print axioms ChowlaCosine.P31.elementary_convolution_bound

-- 18. Elementary analytic Nikolskii and explicit 41/100-density theorem.
#check @ChowlaCosine.P31.continuous_circleCharacter
#print axioms ChowlaCosine.P31.continuous_circleCharacter
#check @ChowlaCosine.P31.circleCharacter_add
#print axioms ChowlaCosine.P31.circleCharacter_add
#check @ChowlaCosine.P31.circleCharacter_star
#print axioms ChowlaCosine.P31.circleCharacter_star
#check @ChowlaCosine.P31.circleMean_re_mul_character
#print axioms ChowlaCosine.P31.circleMean_re_mul_character
#check @ChowlaCosine.P31.circleMean_norm_sq_sum
#print axioms ChowlaCosine.P31.circleMean_norm_sq_sum
#check @ChowlaCosine.P31.circleMean_analytic_sq
#print axioms ChowlaCosine.P31.circleMean_analytic_sq
#check @ChowlaCosine.P31.real_additive_quad_eq_energy
#print axioms ChowlaCosine.P31.real_additive_quad_eq_energy
#check @ChowlaCosine.P31.circleMean_analytic_four_le_energy
#print axioms ChowlaCosine.P31.circleMean_analytic_four_le_energy
#check @ChowlaCosine.P31.discreteEnergy_scale
#print axioms ChowlaCosine.P31.discreteEnergy_scale
#check @ChowlaCosine.P31.elementary_discreteEnergy_bound_homogeneous
#print axioms ChowlaCosine.P31.elementary_discreteEnergy_bound_homogeneous
#check @ChowlaCosine.P31.elementary_analyticNikolskii
#print axioms ChowlaCosine.P31.elementary_analyticNikolskii
#check @ChowlaCosine.P31.p31_elementary
#print axioms ChowlaCosine.P31.p31_elementary
#check @ChowlaCosine.P31.windowEnergy_nonneg
#print axioms ChowlaCosine.P31.windowEnergy_nonneg
#check @ChowlaCosine.P31.two_windowEnergy_le
#print axioms ChowlaCosine.P31.two_windowEnergy_le
#check @ChowlaCosine.P31.card_le_max_frequency
#print axioms ChowlaCosine.P31.card_le_max_frequency
#check @ChowlaCosine.P31.half_le_of_nonempty
#print axioms ChowlaCosine.P31.half_le_of_nonempty
#check @ChowlaCosine.P31.dense_large_sq
#print axioms ChowlaCosine.P31.dense_large_sq
#check @ChowlaCosine.P31.dense_elementary
#print axioms ChowlaCosine.P31.dense_elementary

-- 19. Beckner M1: non-sharp Young on R, all finite triples and conjugate boundary.
#print axioms ChowlaCosine.Beckner.young_L1_integral
#print axioms ChowlaCosine.Beckner.young_L1
#print axioms ChowlaCosine.Beckner.aestronglyMeasurable_convolution
#print axioms ChowlaCosine.Beckner.young_conjugate_pointwise
#print axioms ChowlaCosine.Beckner.young_conjugate
#print axioms ChowlaCosine.Beckner.lintegral_weighted_three
#print axioms ChowlaCosine.Beckner.lintegral_weighted_two
#print axioms ChowlaCosine.Beckner.lintegral_weighted_three_nonneg
#print axioms ChowlaCosine.Beckner.young_pointwise_power
#print axioms ChowlaCosine.Beckner.lintegral_convolution_ennreal
#print axioms ChowlaCosine.Beckner.young_lintegral_power
#print axioms ChowlaCosine.Beckner.young_finite_gt_one
#print axioms ChowlaCosine.Beckner.young_finite

-- 20. Project exponents, non-sharp specialization only.
#print axioms ChowlaCosine.Beckner.young_four_thirds

-- 21. Gaussian norms, convolution, and exact project-factor attainment (M3).
#print axioms ChowlaCosine.Beckner.gaussian_rpow
#print axioms ChowlaCosine.Beckner.integrable_gaussian
#print axioms ChowlaCosine.Beckner.integral_gaussian_exact
#print axioms ChowlaCosine.Beckner.integral_gaussian_rpow
#print axioms ChowlaCosine.Beckner.gaussian_mul_completed_square
#print axioms ChowlaCosine.Beckner.gaussian_convolution
#print axioms ChowlaCosine.Beckner.eLpNorm_complexGaussian
#print axioms ChowlaCosine.Beckner.memLp_complexGaussian
#print axioms ChowlaCosine.Beckner.complexGaussian_convolution
#print axioms ChowlaCosine.Beckner.eLpNorm_complexGaussian_convolution
#print axioms ChowlaCosine.Beckner.sharpBeta_pos
#print axioms ChowlaCosine.Beckner.gaussian_attains_project_constant
#print axioms ChowlaCosine.Beckner.project_constant_lower_bound

-- 22. M4 PARTIAL: frame variance, heat kernel, and L1 heat equation.
-- The geometric-product differentiated identity is a named HYPOTHESIS in the conditional reduction.
#print axioms ChowlaCosine.Beckner.frame_variance_identity
#print axioms ChowlaCosine.Beckner.frame_variance_nonneg
#print axioms ChowlaCosine.Beckner.heatKernel_pos
#print axioms ChowlaCosine.Beckner.integrable_heatKernel
#print axioms ChowlaCosine.Beckner.integral_heatKernel
#print axioms ChowlaCosine.Beckner.hasDerivAt_gaussian
#print axioms ChowlaCosine.Beckner.hasDerivAt_heatKernel_space
#print axioms ChowlaCosine.Beckner.hasDerivAt_gaussian_slope
#print axioms ChowlaCosine.Beckner.heatKernel_eq
#print axioms ChowlaCosine.Beckner.hasDerivAt_heatKernel_slope
#print axioms ChowlaCosine.Beckner.hasDerivAt_heatKernel_time
#print axioms ChowlaCosine.Beckner.heatKernel_semigroup
#print axioms ChowlaCosine.Beckner.heatFlow_nonneg
#print axioms ChowlaCosine.Beckner.integral_heatFlow
#print axioms ChowlaCosine.Beckner.heatKernel_le
#print axioms ChowlaCosine.Beckner.continuous_heatKernel
#print axioms ChowlaCosine.Beckner.integrable_heatFlow_integrand
#print axioms ChowlaCosine.Beckner.heatFlow_pos
#print axioms ChowlaCosine.Beckner.gaussian_shift_le
#print axioms ChowlaCosine.Beckner.heatFlow_gaussian_bound
#print axioms ChowlaCosine.Beckner.frame_gaussian_identity
#print axioms ChowlaCosine.Beckner.frame_product_gaussian_bound
#print axioms ChowlaCosine.Beckner.monotone_of_heat_defect_identity
#print axioms ChowlaCosine.Beckner.gaussian_quadratic_le
#print axioms ChowlaCosine.Beckner.heatKernel_time_slope_bound
#print axioms ChowlaCosine.Beckner.heatKernel_time_envelope_le
#print axioms ChowlaCosine.Beckner.hasDerivAt_heatFlow_time
#print axioms ChowlaCosine.Beckner.heatKernel_space_slope_bound
#print axioms ChowlaCosine.Beckner.hasDerivAt_heatFlow_space
#print axioms ChowlaCosine.Beckner.hasDerivAt_heatFlow_space_slope
#print axioms ChowlaCosine.Beckner.heatFlow_heat_equation

-- 23. M4 PARTIAL: relative scores, actual geometric differential inequality,
-- and a global R2 integral bridge with EXPLICIT analytic hypotheses.
#print axioms ChowlaCosine.Beckner.abs_integral_le_scaled_integral
#print axioms ChowlaCosine.Beckner.integrable_heatSpaceSlope_integrand
#print axioms ChowlaCosine.Beckner.integrable_heatTimeSlope_integrand
#print axioms ChowlaCosine.Beckner.heatFlow_space_moment_bound
#print axioms ChowlaCosine.Beckner.heatFlow_time_moment_bound
#print axioms ChowlaCosine.Beckner.heatFlow_space_score_bound
#print axioms ChowlaCosine.Beckner.heatFlow_time_score_bound
#print axioms ChowlaCosine.Beckner.weighted_product_eq_exp
#print axioms ChowlaCosine.Beckner.hasDerivAt_weighted_product
#print axioms ChowlaCosine.Beckner.hasDerivAt_weighted_product_slope
#print axioms ChowlaCosine.Beckner.frame_laplacian_identity
#print axioms ChowlaCosine.Beckner.frame_heat_defect_nonneg
#print axioms ChowlaCosine.Beckner.hasDerivAt_heatFlow_affine
#print axioms ChowlaCosine.Beckner.hasDerivAt_heatSpaceMoment_affine
#print axioms ChowlaCosine.Beckner.hasDerivAt_geometricHeatProduct_time
#print axioms ChowlaCosine.Beckner.geometricHeatPath_second_derivative
#print axioms ChowlaCosine.Beckner.geometricHeat_defect_nonneg
#print axioms ChowlaCosine.Beckner.integral_partial_x_eq_zero
#print axioms ChowlaCosine.Beckner.integral_partial_y_eq_zero
#print axioms ChowlaCosine.Beckner.parabolic_integral_derivative_nonneg

-- 24. P34: arbitrary complex coefficients, full-circle windows and Littlewood bounds.
#check @ChowlaCosine.P34.circleMean_trigSum_mul
#print axioms ChowlaCosine.P34.circleMean_trigSum_mul
#check @ChowlaCosine.P34.circleMean_trigSum_add_sq
#print axioms ChowlaCosine.P34.circleMean_trigSum_add_sq
#check @ChowlaCosine.P34.circleMean_fejer_mul_re
#print axioms ChowlaCosine.P34.circleMean_fejer_mul_re
#check @ChowlaCosine.P34.circleMean_window_mean_sq
#print axioms ChowlaCosine.P34.circleMean_window_mean_sq
#check @ChowlaCosine.P34.p34_main
#print axioms ChowlaCosine.P34.p34_main
#check @ChowlaCosine.P34.p34_main_bounded
#print axioms ChowlaCosine.P34.p34_main_bounded
#check @ChowlaCosine.P34.p34_elementary
#print axioms ChowlaCosine.P34.p34_elementary
#check @ChowlaCosine.P34.p34_main_real
#print axioms ChowlaCosine.P34.p34_main_real
#check @ChowlaCosine.P34.p34_main_real_bounded
#print axioms ChowlaCosine.P34.p34_main_real_bounded
#check @ChowlaCosine.P34.p34_A
#print axioms ChowlaCosine.P34.p34_A
#check @ChowlaCosine.P34.p34_A_real
#print axioms ChowlaCosine.P34.p34_A_real
#check @ChowlaCosine.P34.p34_A_phases
#print axioms ChowlaCosine.P34.p34_A_phases
#check @ChowlaCosine.P34.p34_A_exists_le
#print axioms ChowlaCosine.P34.p34_A_exists_le
#check @ChowlaCosine.P34.p34_A_exists_ge
#print axioms ChowlaCosine.P34.p34_A_exists_ge
#check @ChowlaCosine.P34.p34_B
#print axioms ChowlaCosine.P34.p34_B
#check @ChowlaCosine.P34.p34_C
#print axioms ChowlaCosine.P34.p34_C
#check @ChowlaCosine.P34.p34_C_real
#print axioms ChowlaCosine.P34.p34_C_real

-- 25. P33 ratio and dilation pinch, with exact finite-root averaging.
#check @ChowlaCosine.P34.p33_ratio
#print axioms ChowlaCosine.P34.p33_ratio
#check @ChowlaCosine.P34.p33_ratio_min_max
#print axioms ChowlaCosine.P34.p33_ratio_min_max
#check @ChowlaCosine.P34.dilation_identity
#print axioms ChowlaCosine.P34.dilation_identity
#check @ChowlaCosine.P34.dilation_pinch
#print axioms ChowlaCosine.P34.dilation_pinch

-- 26. P34 supporting lemmas: audit every new public theorem as well.
#print axioms ChowlaCosine.P34.energy_eq_card
#print axioms ChowlaCosine.P34.windowMass_le_succ
#print axioms ChowlaCosine.P34.circleCharacter_norm
#print axioms ChowlaCosine.P34.trigSum_le_card
#print axioms ChowlaCosine.P34.energy_le_two_card_mul
#print axioms ChowlaCosine.P34.trigSum_periodic
#print axioms ChowlaCosine.P34.trigSum_exists_min
#print axioms ChowlaCosine.P34.trigSum_neg
#print axioms ChowlaCosine.P34.littlewoodSum_eq
#print axioms ChowlaCosine.P34.re_character_mem_trigBand
#print axioms ChowlaCosine.P34.trigSum_add_mem_trigBand
#print axioms ChowlaCosine.P34.nikolskii_constant_one_le
#print axioms ChowlaCosine.P34.windowEnergy_le
#print axioms ChowlaCosine.P34.nonneg_of_trigSum_ge
#print axioms ChowlaCosine.P34.continuous_trigSum
#print axioms ChowlaCosine.P34.circleMean_trigSum
#print axioms ChowlaCosine.P34.re_mul_re
#print axioms ChowlaCosine.P34.circleMean_re_character_mul
#print axioms ChowlaCosine.P34.circleCharacter_re
#print axioms ChowlaCosine.P34.circleCharacter_im
#print axioms ChowlaCosine.P34.circleMean_window
#print axioms ChowlaCosine.P34.coefficients_norm_sq
#print axioms ChowlaCosine.P34.trigSum_coefficients
#print axioms ChowlaCosine.P34.energy_coefficients
#print axioms ChowlaCosine.P34.windowEnergy_interval
#print axioms ChowlaCosine.P34.phaseCoefficients_norm_sq
#print axioms ChowlaCosine.P34.trigSum_phase
#print axioms ChowlaCosine.P34.fejerKernel_zero

-- 27. P36: exact sine kernel, quadratic Fourier increments, and all-real gap truncation.
#print axioms ChowlaCosine.P36.squareKernel_nonneg
#print axioms ChowlaCosine.P36.squareKernel_expansion
#print axioms ChowlaCosine.P36.circleMean_squareKernel
#print axioms ChowlaCosine.P36.circleMean_squareKernel_mul_shift
#print axioms ChowlaCosine.P36.squareCoeff_pair_formula
#print axioms ChowlaCosine.P36.squareCoeff_one
#print axioms ChowlaCosine.P36.squareCoeff_eq_zero
#print axioms ChowlaCosine.P36.abs_sin_nat_mul_le
#print axioms ChowlaCosine.P36.one_sub_cos_nat_mul_le
#print axioms ChowlaCosine.P36.kernelCoeff_le_mass
#print axioms ChowlaCosine.P36.kernelCoeff_increment_le
#print axioms ChowlaCosine.P36.truncation_of_kernel
#print axioms ChowlaCosine.P36.sineAngle_pos
#print axioms ChowlaCosine.P36.sineAngle_lt_pi
#print axioms ChowlaCosine.P36.sineWeight_last
#print axioms ChowlaCosine.P36.sineMass_pos
#print axioms ChowlaCosine.P36.sineWeight_recurrence
#print axioms ChowlaCosine.P36.sine_adjacent_sum
#print axioms ChowlaCosine.P36.sineKernel_nonneg
#print axioms ChowlaCosine.P36.circleMean_sineKernel
#print axioms ChowlaCosine.P36.kernelCoeff_sineKernel
#print axioms ChowlaCosine.P36.kernelCoeff_sineKernel_one
#print axioms ChowlaCosine.P36.kernelCoeff_sineKernel_eq_zero
#print axioms ChowlaCosine.P36.circleMean_sineKernel_mul_shift
#check @ChowlaCosine.P36.p36_truncation
#print axioms ChowlaCosine.P36.p36_truncation
#check @ChowlaCosine.P36.p36_gap
#print axioms ChowlaCosine.P36.p36_gap
#check @ChowlaCosine.P36.p36_gap_pi
#print axioms ChowlaCosine.P36.p36_gap_pi

-- 28. M4: uniform domination and the concrete global heat-product integration bridge.
#print axioms ChowlaCosine.Beckner.heatTailConstant_nonneg
#print axioms ChowlaCosine.Beckner.heatFlow_gaussian_bound_interval
#print axioms ChowlaCosine.Beckner.geometricHeatProduct_gaussian_bound_interval
#print axioms ChowlaCosine.Beckner.heatTimeScore_bound_interval
#print axioms ChowlaCosine.Beckner.heatSpaceScore_bound_interval
#print axioms ChowlaCosine.Beckner.geometricHeatProduct_time_derivative_bound_interval
#print axioms ChowlaCosine.Beckner.continuous_heatFlow_space
#print axioms ChowlaCosine.Beckner.continuous_heatSpaceMoment_space
#print axioms ChowlaCosine.Beckner.measurable_heatTimeMoment
#print axioms ChowlaCosine.Beckner.measurable_heatTimeScore
#print axioms ChowlaCosine.Beckner.integrable_plane_polynomial_gaussian
#print axioms ChowlaCosine.Beckner.heat_score_polynomial_bound
#print axioms ChowlaCosine.Beckner.continuous_planePoint
#print axioms ChowlaCosine.Beckner.norm_planePoint_sq
#print axioms ChowlaCosine.Beckner.continuous_geometricHeatProduct_space
#print axioms ChowlaCosine.Beckner.measurable_geometricHeatTimeSlope_plane
#print axioms ChowlaCosine.Beckner.geometricHeatTimeSlope_plane_bound_interval
#print axioms ChowlaCosine.Beckner.integrable_geometricHeatProduct_plane
#print axioms ChowlaCosine.Beckner.hasDerivAt_integral_geometricHeatProduct_plane
#print axioms ChowlaCosine.Beckner.abs_weighted_directional_score_le
#print axioms ChowlaCosine.Beckner.abs_weighted_second_score_le
#print axioms ChowlaCosine.Beckner.hasDerivAt_geometricHeatSpaceSlope_line
#print axioms ChowlaCosine.Beckner.geometricHeat_spatial_envelopes
#print axioms ChowlaCosine.Beckner.measurable_heatSpaceScore
#print axioms ChowlaCosine.Beckner.measurable_geometricHeat_spatial_slopes_plane
#print axioms ChowlaCosine.Beckner.integrable_geometricHeat_spatial_slopes_plane
#print axioms ChowlaCosine.Beckner.integrable_geometricHeatTimeSlope_plane
#print axioms ChowlaCosine.Beckner.geometricHeatProduct_integral_derivative_nonneg
#print axioms ChowlaCosine.Beckner.geometricHeatProduct_integral_monotone

-- 29. M4 scalar rescaling: exact dilation and all-L1 large-time asymptotics.
#print axioms ChowlaCosine.Beckner.tendsto_rescaledHeatFlow
#print axioms ChowlaCosine.Beckner.heatKernel_rescale
#print axioms ChowlaCosine.Beckner.rescaledHeatFlow_eq_heatFlow
#print axioms ChowlaCosine.Beckner.tendsto_heatFlow_large_time
#print axioms ChowlaCosine.Beckner.tendsto_sqrt_mul_heatFlow

#print axioms ChowlaCosine.P36.continuous_squareKernel
#print axioms ChowlaCosine.P36.continuous_sineKernel

-- 30. M4: whole-plane large-time limit and the initial-time Fatou passage.
#print axioms ChowlaCosine.Beckner.weightedFrame_sum_weights
#print axioms ChowlaCosine.Beckner.geometricHeatProduct_rescale
#print axioms ChowlaCosine.Beckner.rescaled_heatFlow_gaussian_bound
#print axioms ChowlaCosine.Beckner.integrable_plane_gaussian
#print axioms ChowlaCosine.Beckner.integral_plane_gaussian
#print axioms ChowlaCosine.Beckner.integral_plane_dilate
#print axioms ChowlaCosine.Beckner.planePoint_smul
#print axioms ChowlaCosine.Beckner.frame_heatKernel_product
#print axioms ChowlaCosine.Beckner.integral_frame_heatKernel_product
#print axioms ChowlaCosine.Beckner.tendsto_integral_rescaled_geometricHeatProduct
#print axioms ChowlaCosine.Beckner.tendsto_integral_geometricHeatProduct_sq
#print axioms ChowlaCosine.Beckner.tendsto_integral_geometricHeatProduct
#print axioms ChowlaCosine.Beckner.integral_geometricHeatProduct_le_mass
#print axioms ChowlaCosine.Beckner.heatFlow_initial_rescale
#print axioms ChowlaCosine.Beckner.tendsto_heatFlow_initial_sq
#print axioms ChowlaCosine.Beckner.integrable_and_integral_le_of_nonneg_limit
#print axioms ChowlaCosine.Beckner.tendsto_geometricHeatProduct_initial_sq
#print axioms ChowlaCosine.Beckner.geometric_brascamp_lieb_bounded_continuous

-- 31. M4: compact density, null-set pullback, and unrestricted planar geometric BL.
#print axioms ChowlaCosine.Beckner.geometric_brascamp_lieb_continuous_compact
#print axioms ChowlaCosine.Beckner.ae_plane_linear
#print axioms ChowlaCosine.Beckner.ae_plane_inner
#print axioms ChowlaCosine.Beckner.exists_positive_compact_datum
#print axioms ChowlaCosine.Beckner.exists_positive_compact_approximation
#print axioms ChowlaCosine.Beckner.exists_positive_compact_approximation_seq
#print axioms ChowlaCosine.Beckner.exists_common_support_radius
#print axioms ChowlaCosine.Beckner.integrable_and_integral_le_of_nonneg_limit_bounds
#print axioms ChowlaCosine.Beckner.geometric_brascamp_lieb

-- 32. M4: explicit interior Young frame, determinant, and exact Beckner factors.
#print axioms ChowlaCosine.Beckner.isWeightedFrame_plane_of_coefficients
#print axioms ChowlaCosine.Beckner.youngFrameMatrix_det
#print axioms ChowlaCosine.Beckner.youngFrame_coordinate_relation
#print axioms ChowlaCosine.Beckner.young_scalar_factor
#print axioms ChowlaCosine.Beckner.young_scalar_factor_beckner
#print axioms ChowlaCosine.Beckner.youngFrame_sharp_factor
#print axioms ChowlaCosine.Beckner.youngFrame_matrix
#print axioms ChowlaCosine.Beckner.youngFrame_isWeightedFrame
#print axioms ChowlaCosine.Beckner.youngFrame_unit
#print axioms ChowlaCosine.Beckner.youngFrame_relation
#print axioms ChowlaCosine.Beckner.geometric_brascamp_lieb_youngFrame
#check @ChowlaCosine.Beckner.tendsto_integral_geometricHeatProduct
#check @ChowlaCosine.Beckner.geometric_brascamp_lieb
#check @ChowlaCosine.Beckner.youngFrame_sharp_factor

-- 33. M4b: exact planar substitution and sharp Young, all extended exponents.
#print axioms ChowlaCosine.Beckner.youngFrameMap_det
#print axioms ChowlaCosine.Beckner.plane_linear_change
#print axioms ChowlaCosine.Beckner.youngFrameMap_apply
#print axioms ChowlaCosine.Beckner.youngFrameMap_third
#print axioms ChowlaCosine.Beckner.young_trilinear_complement
#print axioms ChowlaCosine.Beckner.young_trilinear_interior
#print axioms ChowlaCosine.Beckner.memLp_normConvolution
#print axioms ChowlaCosine.Beckner.young_power_cancel
#print axioms ChowlaCosine.Beckner.sharp_young_normConvolution_interior
#print axioms ChowlaCosine.Beckner.becknerFactor_zero
#print axioms ChowlaCosine.Beckner.becknerFactor_one
#print axioms ChowlaCosine.Beckner.becknerFactor_mul_complement
#print axioms ChowlaCosine.Beckner.sharp_young_finite_interior
#print axioms ChowlaCosine.Beckner.sharp_young_finite
#print axioms ChowlaCosine.Beckner.sharp_young_ennreal
#print axioms ChowlaCosine.Beckner.sharp_young

-- 34. M5: exact project constant, autocorrelation, and interval support.
#print axioms ChowlaCosine.Beckner.becknerFactor_three_quarters_fourth
#print axioms ChowlaCosine.Beckner.becknerFactor_half
#print axioms ChowlaCosine.Beckner.sharp_young_four_thirds_sq
#print axioms ChowlaCosine.Beckner.memLp_reflectConj
#print axioms ChowlaCosine.Beckner.eLpNorm_reflectConj
#print axioms ChowlaCosine.Beckner.sharp_autocorrelation
#print axioms ChowlaCosine.Beckner.interval_four_thirds_le_two
#print axioms ChowlaCosine.Beckner.sharp_interval_selfConvolution
#print axioms ChowlaCosine.Beckner.sharp_interval_autocorrelation
