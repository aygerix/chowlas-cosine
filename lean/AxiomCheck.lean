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
