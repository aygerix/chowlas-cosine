import ChowlaCosine

/-! Axiom audit for the T0--T3 formalization in `lean_o4plus_brief.md`. -/

-- T0: Fourier Schur product and all natural powers.
#print axioms ChowlaCosine.FibreSchur.fourier_inversion
#print axioms ChowlaCosine.FibreSchur.fourier_mul_card
#print axioms ChowlaCosine.FibreSchur.PositiveDefinite.mul
#print axioms ChowlaCosine.FibreSchur.PositiveDefinite.pow

-- Shared Fourier and quotient bridges, not assumptions of the final bounds.
#print axioms ChowlaCosine.FibreSchur.fourier_fibre
#print axioms ChowlaCosine.FibreSchur.shifted_fibre_positiveDefinite
#print axioms ChowlaCosine.FibreSchur.power_certificate_bound
#print axioms ChowlaCosine.FibreSchur.fibreSet_eq_image
#print axioms ChowlaCosine.FibreSchur.quotientPower_apply

-- T1: exact order-three table, bound, zero fibre, and both run-top corollaries.
#print axioms ChowlaCosine.FibreSchur.fibre_table_three
#print axioms ChowlaCosine.FibreSchur.fibre_cube_table
#print axioms ChowlaCosine.FibreSchur.order_three_fibre_bound
#print axioms ChowlaCosine.FibreSchur.order_three_zero_fibre
#print axioms ChowlaCosine.FibreSchur.order_three_runTops_card
#print axioms ChowlaCosine.FibreSchur.order_three_runTops_bound

-- T2: exact table, agreement with actual two-run fibres, bound, and zero fibre.
#print axioms ChowlaCosine.FibreSchur.fibre_table_four
#print axioms ChowlaCosine.FibreSchur.mem_twoRunCosets_iff
#print axioms ChowlaCosine.FibreSchur.fibre_fourth_table
#print axioms ChowlaCosine.FibreSchur.order_four_fibre_bound
#print axioms ChowlaCosine.FibreSchur.order_four_zero_fibre

-- T3(a)--(c), including the requested audit of the general constant.
#print axioms ChowlaCosine.HalfSet.hat_conv_hat
#print axioms ChowlaCosine.HalfSet.shiftedHat_square
#print axioms ChowlaCosine.HalfSet.shiftedHat_square_off_zero
#print axioms ChowlaCosine.HalfSet.shiftedHat_cube
#print axioms ChowlaCosine.HalfSet.cubicConstant_eq_brief
#print axioms ChowlaCosine.HalfSet.cubicConstant_of_neg_one
#print axioms ChowlaCosine.HalfSet.shiftedHat_cube_neg_one

-- T3(d)--(e), including the realness and positivity bridges.
#print axioms ChowlaCosine.HalfSet.hat_im_eq_zero
#print axioms ChowlaCosine.HalfSet.realShiftedHat_cast
#print axioms ChowlaCosine.HalfSet.realShiftedHat_nonneg
#print axioms ChowlaCosine.HalfSet.cube_delete
#print axioms ChowlaCosine.HalfSet.spectral_gap
#print axioms ChowlaCosine.HalfSet.coefficient_upper_bound
