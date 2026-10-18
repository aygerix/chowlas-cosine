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
