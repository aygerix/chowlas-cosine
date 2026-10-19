import ChowlaCosine.P31.ElementaryConstant

/-! # The complete elementary finite convolution inequality P31-E -/

open Real MeasureTheory
open scoped BigOperators

namespace ChowlaCosine.P31

/-- The exact ordered-pair convolution energy, before identifying it
with the squared ℓ² norm of the coefficient convolution. -/
noncomputable def discreteEnergy (N : ℕ) (v : Fin N → ℝ) : ℝ :=
  ∑ p : Fin N × Fin N, ∑ q : Fin N × Fin N,
    if p.1.val + q.1.val = p.2.val + q.2.val then
      (v p.1 * v p.2) * (v q.1 * v q.2) else 0

noncomputable def pairCount (N : ℕ) (p : Fin N × Fin N) : ℝ :=
  ∑ q : Fin N × Fin N, if p.1.val + q.1.val = p.2.val + q.2.val then 1 else 0

/-- The AM–GM form of E1, valid even for signed vectors. The interval
pair-count and cumulative-mass identities will turn its right side into E1. -/
theorem discreteEnergy_le_pairCount (N : ℕ) (v : Fin N → ℝ) :
    discreteEnergy N v ≤
      ∑ p : Fin N × Fin N, (v p.1 * v p.2) ^ 2 * pairCount N p := by
  let F : (Fin N × Fin N) → (Fin N × Fin N) → ℝ := fun p q =>
    if p.1.val + q.1.val = p.2.val + q.2.val then (v p.1 * v p.2) ^ 2 else 0
  have hsym : (∑ p : Fin N × Fin N, ∑ q : Fin N × Fin N, F q p) =
      ∑ p : Fin N × Fin N, ∑ q : Fin N × Fin N, F p q := Finset.sum_comm
  have hAM : discreteEnergy N v ≤ ∑ p : Fin N × Fin N, ∑ q : Fin N × Fin N,
      (F p q + F q p) / 2 := by
    unfold discreteEnergy
    apply Finset.sum_le_sum
    intro p hp
    apply Finset.sum_le_sum
    intro q hq
    have hrel : (p.1.val + q.1.val = p.2.val + q.2.val) ↔
        (q.1.val + p.1.val = q.2.val + p.2.val) := by omega
    by_cases heq : p.1.val + q.1.val = p.2.val + q.2.val
    · have heq' := hrel.mp heq
      simp only [heq, heq', F, ↓reduceIte]
      nlinarith [sq_nonneg (v p.1 * v p.2 - v q.1 * v q.2)]
    · have heq' := mt hrel.mpr heq
      simp only [heq, heq', F, ↓reduceIte, zero_add, zero_div, le_refl]
  have hB : discreteEnergy N v ≤ ∑ p : Fin N × Fin N, ∑ q : Fin N × Fin N, F p q := by
    calc
      _ ≤ _ := hAM
      _ = ((∑ p : Fin N × Fin N, ∑ q : Fin N × Fin N, F p q) +
          (∑ p : Fin N × Fin N, ∑ q : Fin N × Fin N, F q p)) / 2 := by
        simp_rw [← Finset.sum_div, Finset.sum_add_distrib]
      _ = _ := by rw [hsym]; ring
  convert hB using 1
  apply Finset.sum_congr rfl
  intro p hp
  rw [pairCount, Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro q hq
  by_cases heq : p.1.val + q.1.val = p.2.val + q.2.val <;> simp [heq, F]

private theorem relation_fiber_le_one (N : ℕ) (a c b : Fin N) :
    (∑ d : Fin N, if a.val + b.val = c.val + d.val then (1 : ℝ) else 0) ≤ 1 := by
  classical
  by_cases hex : ∃ d : Fin N, a.val + b.val = c.val + d.val
  · obtain ⟨d₀, hd₀⟩ := hex
    have heq : ∀ d : Fin N, (a.val + b.val = c.val + d.val) ↔ d = d₀ := by
      intro d
      constructor
      · intro hd
        apply Fin.ext
        omega
      · rintro rfl
        exact hd₀
    simp_rw [heq]
    simp
  · push Not at hex
    simp [hex]

private theorem relation_sum_first_sq_le (N : ℕ) (v : Fin N → ℝ) (p : Fin N × Fin N) :
    (∑ q : Fin N × Fin N,
      if p.1.val + q.1.val = p.2.val + q.2.val then v q.1 ^ 2 else 0) ≤
        ∑ j : Fin N, v j ^ 2 := by
  classical
  rw [Fintype.sum_prod_type]
  apply Finset.sum_le_sum
  intro b hb
  have hs : (∑ d : Fin N, if p.1.val + b.val = p.2.val + d.val then v b ^ 2 else 0) =
      (∑ d : Fin N, if p.1.val + b.val = p.2.val + d.val then (1 : ℝ) else 0) * v b ^ 2 := by
    rw [Finset.sum_mul]
    apply Finset.sum_congr rfl
    intro d hd
    split_ifs <;> ring
  rw [hs]
  simpa only [one_mul] using mul_le_mul_of_nonneg_right
    (relation_fiber_le_one N p.1 p.2 b) (sq_nonneg (v b))

private theorem relation_sum_second_sq_le (N : ℕ) (v : Fin N → ℝ) (p : Fin N × Fin N) :
    (∑ q : Fin N × Fin N,
      if p.1.val + q.1.val = p.2.val + q.2.val then v q.2 ^ 2 else 0) ≤
        ∑ j : Fin N, v j ^ 2 := by
  have heq : (∑ q : Fin N × Fin N,
      if p.1.val + q.1.val = p.2.val + q.2.val then v q.2 ^ 2 else 0) =
      ∑ q : Fin N × Fin N,
        if p.2.val + q.1.val = p.1.val + q.2.val then v q.1 ^ 2 else 0 := by
    rw [Fintype.sum_prod_type, Fintype.sum_prod_type, Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro b hb
    apply Finset.sum_congr rfl
    intro d hd
    simp only [eq_comm]
  rw [heq]
  exact relation_sum_first_sq_le N v (p.2, p.1)

/-- E2, for every nonnegative unit vector, without a restriction on its length. -/
theorem discreteEnergy_le_sum_sq (N : ℕ) (v : Fin N → ℝ)
    (hv0 : ∀ j, 0 ≤ v j) (hv : ∑ j : Fin N, v j ^ 2 = 1) :
    discreteEnergy N v ≤ (∑ j : Fin N, v j) ^ 2 := by
  have hinner : ∀ p : Fin N × Fin N,
      (∑ q : Fin N × Fin N,
        if p.1.val + q.1.val = p.2.val + q.2.val then
          (v p.1 * v p.2) * (v q.1 * v q.2) else 0) ≤ v p.1 * v p.2 := by
    intro p
    have hp : 0 ≤ v p.1 * v p.2 := mul_nonneg (hv0 _) (hv0 _)
    let T := ∑ q : Fin N × Fin N,
      if p.1.val + q.1.val = p.2.val + q.2.val then (v q.1 ^ 2 + v q.2 ^ 2) / 2 else 0
    have hT : T ≤ 1 := by
      have h1 := relation_sum_first_sq_le N v p
      have h2 := relation_sum_second_sq_le N v p
      rw [hv] at h1 h2
      have hs : T = ((∑ q : Fin N × Fin N,
          if p.1.val + q.1.val = p.2.val + q.2.val then v q.1 ^ 2 else 0) +
          (∑ q : Fin N × Fin N,
            if p.1.val + q.1.val = p.2.val + q.2.val then v q.2 ^ 2 else 0)) / 2 := by
        calc
          _ = ∑ q : Fin N × Fin N, ((if p.1.val + q.1.val = p.2.val + q.2.val then
              v q.1 ^ 2 else 0) + (if p.1.val + q.1.val = p.2.val + q.2.val then
                v q.2 ^ 2 else 0)) / 2 := by
            apply Finset.sum_congr rfl
            intro q hq
            split_ifs <;> ring
          _ = _ := by rw [← Finset.sum_div, Finset.sum_add_distrib]
      rw [hs]
      linarith
    calc
      _ ≤ (v p.1 * v p.2) * T := by
        rw [Finset.mul_sum]
        apply Finset.sum_le_sum
        intro q hq
        by_cases heq : p.1.val + q.1.val = p.2.val + q.2.val
        · simp only [heq, ↓reduceIte]
          apply mul_le_mul_of_nonneg_left _ hp
          nlinarith [sq_nonneg (v q.1 - v q.2)]
        · simp only [heq, ↓reduceIte, mul_zero, le_refl]
      _ ≤ _ := by simpa only [mul_one] using mul_le_mul_of_nonneg_left hT hp
  unfold discreteEnergy
  calc
    _ ≤ ∑ p : Fin N × Fin N, v p.1 * v p.2 := Finset.sum_le_sum (fun p hp => hinner p)
    _ = _ := by rw [Fintype.sum_prod_type, sq, Finset.sum_mul_sum]

private theorem pairCount_le_sub_of_le (N : ℕ) (p : Fin N × Fin N)
    (hp : p.1.val ≤ p.2.val) : pairCount N p ≤ (N - (p.2.val - p.1.val) : ℕ) := by
  classical
  let s : Finset (Fin N × Fin N) := Finset.univ.filter
    (fun q => p.1.val + q.1.val = p.2.val + q.2.val)
  have hcard : pairCount N p = (s.card : ℝ) := by
    simp only [s, Finset.card_filter, Nat.cast_sum, Nat.cast_ite, Nat.cast_one,
      Nat.cast_zero, pairCount]
  have hc : s.card ≤ (Finset.range (N - (p.2.val - p.1.val))).card := by
    apply Finset.card_le_card_of_injOn (fun q : Fin N × Fin N => q.2.val)
    · intro q hq
      have hr : p.1.val + q.1.val = p.2.val + q.2.val := (Finset.mem_filter.mp hq).2
      simp only [Finset.mem_coe, Finset.mem_range]
      have hq1 := q.1.isLt
      omega
    · intro q hq r hr heq
      have hqrel := (Finset.mem_filter.mp hq).2
      have hrrel := (Finset.mem_filter.mp hr).2
      change q.2.val = r.2.val at heq
      apply Prod.ext
      · apply Fin.ext
        omega
      · exact Fin.ext heq
  rw [hcard]
  have hc' : s.card ≤ N - (p.2.val - p.1.val) := by simpa only [Finset.card_range] using hc
  exact_mod_cast hc'

private theorem pairCount_swap (N : ℕ) (p : Fin N × Fin N) :
    pairCount N (p.2, p.1) = pairCount N p := by
  unfold pairCount
  rw [Fintype.sum_prod_type, Fintype.sum_prod_type, Finset.sum_comm]
  apply Finset.sum_congr rfl
  intro b hb
  apply Finset.sum_congr rfl
  intro d hd
  simp only [eq_comm]

/-- The exact interval-overlap upper bound needed in E1. -/
theorem pairCount_le_distance (N : ℕ) (p : Fin N × Fin N) :
    pairCount N p ≤ (N : ℝ) - |(p.1.val : ℝ) - p.2.val| := by
  by_cases hp : p.1.val ≤ p.2.val
  · have h := pairCount_le_sub_of_le N p hp
    have hd : p.2.val - p.1.val ≤ N := by have := p.2.isLt; omega
    rw [Nat.cast_sub hd, Nat.cast_sub hp] at h
    have hreal : (p.1.val : ℝ) - p.2.val ≤ 0 := by
      have hr : (p.1.val : ℝ) ≤ p.2.val := by exact_mod_cast hp
      linarith
    rwa [abs_of_nonpos hreal, neg_sub]
  · have hpc : p.2.val ≤ p.1.val := Nat.le_of_lt (Nat.lt_of_not_ge hp)
    have h := pairCount_le_sub_of_le N (p.2, p.1) hpc
    rw [pairCount_swap] at h
    have hd : p.1.val - p.2.val ≤ N := by have := p.1.isLt; omega
    rw [Nat.cast_sub hd, Nat.cast_sub hpc] at h
    have hreal : (0 : ℝ) ≤ (p.1.val : ℝ) - p.2.val := by
      have hr : (p.2.val : ℝ) ≤ p.1.val := by exact_mod_cast hpc
      linarith
    rwa [abs_of_nonneg hreal]

noncomputable def massPrefix (N : ℕ) (v : Fin N → ℝ) (k : ℕ) : ℝ :=
  ∑ j : Fin N, if j.val < k then v j ^ 2 else 0

@[simp] theorem massPrefix_zero (N : ℕ) (v : Fin N → ℝ) : massPrefix N v 0 = 0 := by
  simp [massPrefix]

@[simp] theorem massPrefix_total (N : ℕ) (v : Fin N → ℝ) :
    massPrefix N v N = ∑ j : Fin N, v j ^ 2 := by
  simp [massPrefix]

theorem massPrefix_bounds (N : ℕ) (v : Fin N → ℝ)
    (hv : ∑ j : Fin N, v j ^ 2 = 1) (k : ℕ) : massPrefix N v k ∈ Set.Icc (0 : ℝ) 1 := by
  constructor
  · apply Finset.sum_nonneg
    intro j hj
    split_ifs <;> positivity
  · rw [← hv]
    apply Finset.sum_le_sum
    intro j hj
    split_ifs <;> nlinarith [sq_nonneg (v j)]

theorem massPrefix_step (N : ℕ) (v : Fin N → ℝ) (j : Fin N) :
    massPrefix N v (j.val + 1) - massPrefix N v j.val = v j ^ 2 := by
  unfold massPrefix
  rw [← Finset.sum_sub_distrib]
  have hi : ∀ k : Fin N, (if k.val < j.val + 1 then v k ^ 2 else 0) -
      (if k.val < j.val then v k ^ 2 else 0) = if k = j then v j ^ 2 else 0 := by
    intro k
    by_cases heq : k = j
    · subst k
      simp
    · have hneq : k.val ≠ j.val := by exact fun h => heq (Fin.ext h)
      split_ifs <;> simp_all <;> omega
  simp_rw [hi]
  simp

private theorem cut_count (N i j : ℕ) (hj : j ≤ N) :
    (∑ k ∈ Finset.range N, if i ≤ k ∧ k < j then (1 : ℝ) else 0) = (j - i : ℕ) := by
  classical
  have hs : (Finset.range N).filter (fun k => i ≤ k ∧ k < j) = Finset.Ico i j := by
    ext k
    simp only [Finset.mem_filter, Finset.mem_range, Finset.mem_Ico]
    omega
  rw [← Finset.sum_filter, hs]
  simp

private theorem distance_eq_cuts (N : ℕ) (i j : Fin N) :
    |(i.val : ℝ) - j.val| = ∑ k ∈ Finset.range N,
      ((if i.val ≤ k ∧ k < j.val then (1 : ℝ) else 0) +
        (if j.val ≤ k ∧ k < i.val then 1 else 0)) := by
  rw [Finset.sum_add_distrib, cut_count N i.val j.val j.isLt.le,
    cut_count N j.val i.val i.isLt.le]
  by_cases hij : i.val ≤ j.val
  · rw [Nat.sub_eq_zero_of_le hij, Nat.cast_zero, add_zero, Nat.cast_sub hij]
    rw [abs_of_nonpos (by exact sub_nonpos.mpr (by exact_mod_cast hij)), neg_sub]
  · have hji := Nat.le_of_lt (Nat.lt_of_not_ge hij)
    rw [Nat.sub_eq_zero_of_le hji, Nat.cast_zero, zero_add, Nat.cast_sub hji]
    rw [abs_of_nonneg (by exact sub_nonneg.mpr (by exact_mod_cast hji))]

private theorem filtered_mass_product {N : ℕ} (r : Fin N → ℝ) (P Q : Fin N → Prop)
    [DecidablePred P] [DecidablePred Q] :
    (∑ i : Fin N, if P i then r i else 0) * (∑ j : Fin N, if Q j then r j else 0) =
      ∑ p : Fin N × Fin N, if P p.1 ∧ Q p.2 then r p.1 * r p.2 else 0 := by
  rw [Finset.sum_mul_sum, Fintype.sum_prod_type]
  apply Finset.sum_congr rfl
  intro i hi
  apply Finset.sum_congr rfl
  intro j hj
  by_cases hP : P i <;> by_cases hQ : Q j <;> simp [hP, hQ]

private theorem massPrefix_tail (N : ℕ) (v : Fin N → ℝ)
    (hv : ∑ j : Fin N, v j ^ 2 = 1) (k : ℕ) :
    (∑ j : Fin N, if k < j.val then v j ^ 2 else 0) = 1 - massPrefix N v (k + 1) := by
  have hs : (∑ j : Fin N, if k < j.val then v j ^ 2 else 0) + massPrefix N v (k + 1) = 1 := by
    rw [massPrefix, ← Finset.sum_add_distrib, ← hv]
    apply Finset.sum_congr rfl
    intro j hj
    by_cases hk : j.val < k + 1
    · have hk' : ¬k < j.val := by omega
      simp [hk, hk']
    · have hk' : k < j.val := by omega
      simp [hk, hk']
  linarith

/-- Abel's cumulative-mass identity, proved by counting all cuts between
each pair of indices. This is an exact finite identity, not an approximation. -/
theorem distance_mass_identity (N : ℕ) (v : Fin N → ℝ)
    (hv : ∑ j : Fin N, v j ^ 2 = 1) :
    (∑ p : Fin N × Fin N, |(p.1.val : ℝ) - p.2.val| * (v p.1 ^ 2 * v p.2 ^ 2)) =
      2 * ∑ k ∈ Finset.range N, massPrefix N v (k + 1) * (1 - massPrefix N v (k + 1)) := by
  have hfixed : ∀ k : ℕ, (∑ p : Fin N × Fin N,
      ((if p.1.val ≤ k ∧ k < p.2.val then (1 : ℝ) else 0) +
        (if p.2.val ≤ k ∧ k < p.1.val then 1 else 0)) * (v p.1 ^ 2 * v p.2 ^ 2)) =
          2 * massPrefix N v (k + 1) * (1 - massPrefix N v (k + 1)) := by
    intro k
    have hlow : (∑ j : Fin N, if j.val ≤ k then v j ^ 2 else 0) = massPrefix N v (k + 1) := by
      unfold massPrefix
      apply Finset.sum_congr rfl
      intro j hj
      have hjiff : j.val ≤ k ↔ j.val < k + 1 := by omega
      simp only [hjiff]
    have hprod1 := filtered_mass_product (fun j : Fin N => v j ^ 2)
      (fun j => j.val ≤ k) (fun j => k < j.val)
    have hprod2 := filtered_mass_product (fun j : Fin N => v j ^ 2)
      (fun j => k < j.val) (fun j => j.val ≤ k)
    rw [hlow, massPrefix_tail N v hv k] at hprod1 hprod2
    have heq : (∑ p : Fin N × Fin N,
        ((if p.1.val ≤ k ∧ k < p.2.val then (1 : ℝ) else 0) +
          (if p.2.val ≤ k ∧ k < p.1.val then 1 else 0)) * (v p.1 ^ 2 * v p.2 ^ 2)) =
        (∑ p : Fin N × Fin N, if p.1.val ≤ k ∧ k < p.2.val then v p.1 ^ 2 * v p.2 ^ 2 else 0) +
          (∑ p : Fin N × Fin N, if k < p.1.val ∧ p.2.val ≤ k then v p.1 ^ 2 * v p.2 ^ 2 else 0) := by
      rw [← Finset.sum_add_distrib]
      apply Finset.sum_congr rfl
      intro p hp
      by_cases h1 : p.1.val ≤ k ∧ k < p.2.val <;>
        by_cases h2 : p.2.val ≤ k ∧ k < p.1.val <;> simp [h1, h2, and_comm] <;> ring
    rw [heq, ← hprod1, ← hprod2]
    ring
  simp_rw [distance_eq_cuts, Finset.sum_mul]
  rw [Finset.sum_comm]
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro k hk
  rw [hfixed k]
  ring

/-- The endpoint form of the trapezoid sum equals twice the sum over cuts. -/
theorem massPrefix_trapezoid_sum (N : ℕ) (v : Fin N → ℝ)
    (hv : ∑ j : Fin N, v j ^ 2 = 1) :
    (∑ k ∈ Finset.range N,
      (massPrefix N v k * (1 - massPrefix N v k) +
        massPrefix N v (k + 1) * (1 - massPrefix N v (k + 1)))) =
      2 * ∑ k ∈ Finset.range N, massPrefix N v (k + 1) * (1 - massPrefix N v (k + 1)) := by
  have hs := Finset.sum_range_succ' (fun k => massPrefix N v k * (1 - massPrefix N v k)) N
  rw [Finset.sum_range_succ, massPrefix_zero, massPrefix_total, hv] at hs
  simp only [zero_mul, sub_self, mul_zero, add_zero, zero_add] at hs
  rw [Finset.sum_add_distrib, hs]
  ring

/-- E1 in the exact cumulative-mass form required by P31-E. -/
theorem discreteEnergy_le_cumulative (N : ℕ) (v : Fin N → ℝ)
    (hv : ∑ j : Fin N, v j ^ 2 = 1) :
    discreteEnergy N v ≤ (N : ℝ) - ∑ k ∈ Finset.range N,
      (massPrefix N v k * (1 - massPrefix N v k) +
        massPrefix N v (k + 1) * (1 - massPrefix N v (k + 1))) := by
  have hE := discreteEnergy_le_pairCount N v
  have hB : (∑ p : Fin N × Fin N, (v p.1 * v p.2) ^ 2 * pairCount N p) ≤
      (N : ℝ) - ∑ p : Fin N × Fin N, |(p.1.val : ℝ) - p.2.val| * (v p.1 ^ 2 * v p.2 ^ 2) := by
    calc
      _ ≤ ∑ p : Fin N × Fin N,
          (v p.1 * v p.2) ^ 2 * ((N : ℝ) - |(p.1.val : ℝ) - p.2.val|) := by
        exact Finset.sum_le_sum (fun p hp => mul_le_mul_of_nonneg_left
          (pairCount_le_distance N p) (sq_nonneg _))
      _ = _ := by
        have htotal : (∑ p : Fin N × Fin N, v p.1 ^ 2 * v p.2 ^ 2) = 1 := by
          rw [Fintype.sum_prod_type]
          change (∑ i : Fin N, ∑ j : Fin N, v i ^ 2 * v j ^ 2) = 1
          rw [← Finset.sum_mul_sum, hv, one_mul]
        simp only [mul_pow, mul_sub, Finset.sum_sub_distrib]
        rw [← Finset.sum_mul, htotal, one_mul]
        congr 1
        apply Finset.sum_congr rfl
        intro p hp
        ring
  have hfinal := hE.trans hB
  rwa [distance_mass_identity N v hv, ← massPrefix_trapezoid_sum N v hv] at hfinal

/-- The complete elementary bound for the ordered-pair energy. -/
theorem elementary_discreteEnergy_bound (N : ℕ) (v : Fin N → ℝ)
    (hv0 : ∀ j, 0 ≤ v j) (hv : ∑ j : Fin N, v j ^ 2 = 1) :
    discreteEnergy N v ≤ (811 / 1000 : ℝ) * N + 71 / 300 := by
  let V : ℕ → ℝ := fun n => if hn : n < N then v ⟨n, hn⟩ else 0
  have hsum : (∑ n ∈ Finset.range N, V n) = ∑ j : Fin N, v j := by
    rw [← Fin.sum_univ_eq_sum_range]
    apply Finset.sum_congr rfl
    intro j hj
    simp only [V, dif_pos j.isLt]
  have hsumsq : (∑ n ∈ Finset.range N, V n ^ 2) = 1 := by
    rw [← Fin.sum_univ_eq_sum_range]
    convert hv using 1
    apply Finset.sum_congr rfl
    intro j hj
    simp only [V, dif_pos j.isLt]
  refine elementary_bound_of_two_estimates N V (massPrefix N v) (discreteEnergy N v)
    (massPrefix_zero N v) (by rw [massPrefix_total, hv])
    (fun j hj => massPrefix_bounds N v hv j) ?_ hsumsq
    (discreteEnergy_le_cumulative N v hv) ?_
  · intro j hj
    simpa only [V, dif_pos hj] using massPrefix_step N v ⟨j, hj⟩
  · rw [hsum]
    exact discreteEnergy_le_sum_sq N v hv0 hv

noncomputable def discreteConvolution (N : ℕ) (v : Fin N → ℝ) (k : ℕ) : ℝ :=
  ∑ p : Fin N × Fin N, if p.1.val + p.2.val = k then v p.1 * v p.2 else 0

/-- Exact equivalence with the squared ℓ² norm of the usual coefficient convolution. -/
theorem discreteEnergy_eq_convolution (N : ℕ) (v : Fin N → ℝ) :
    discreteEnergy N v = ∑ k ∈ Finset.range (2 * N - 1), discreteConvolution N v k ^ 2 := by
  classical
  have hsq : ∀ k : ℕ, discreteConvolution N v k ^ 2 =
      ∑ p : Fin N × Fin N, ∑ q : Fin N × Fin N,
        if p.1.val + p.2.val = k ∧ q.1.val + q.2.val = k then
          (v p.1 * v p.2) * (v q.1 * v q.2) else 0 := by
    intro k
    rw [sq, discreteConvolution, Finset.sum_mul_sum]
    apply Finset.sum_congr rfl
    intro p hp
    apply Finset.sum_congr rfl
    intro q hq
    by_cases h1 : p.1.val + p.2.val = k <;>
      by_cases h2 : q.1.val + q.2.val = k <;> simp [h1, h2]
  have hdelta : ∀ p q : Fin N × Fin N,
      (∑ k ∈ Finset.range (2 * N - 1),
        if p.1.val + p.2.val = k ∧ q.1.val + q.2.val = k then
          (v p.1 * v p.2) * (v q.1 * v q.2) else 0) =
        if p.1.val + p.2.val = q.1.val + q.2.val then
          (v p.1 * v p.2) * (v q.1 * v q.2) else 0 := by
    intro p q
    have hp : p.1.val + p.2.val ∈ Finset.range (2 * N - 1) := by
      simp only [Finset.mem_range]
      have h1 := p.1.isLt
      have h2 := p.2.isLt
      omega
    by_cases heq : p.1.val + p.2.val = q.1.val + q.2.val
    · simp only [← heq, and_self, ↓reduceIte]
      simp [hp]
    · rw [if_neg heq]
      apply Finset.sum_eq_zero
      intro k hk
      rw [if_neg (by rintro ⟨h1, h2⟩; exact heq (h1.trans h2.symm))]
  have hsum : (∑ k ∈ Finset.range (2 * N - 1), discreteConvolution N v k ^ 2) =
      ∑ p : Fin N × Fin N, ∑ q : Fin N × Fin N,
        if p.1.val + p.2.val = q.1.val + q.2.val then
          (v p.1 * v p.2) * (v q.1 * v q.2) else 0 := by
    simp_rw [hsq]
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro p hp
    rw [Finset.sum_comm]
    apply Finset.sum_congr rfl
    intro q hq
    exact hdelta p q
  rw [hsum]
  unfold discreteEnergy
  let e : ((Fin N × Fin N) × (Fin N × Fin N)) ≃ ((Fin N × Fin N) × (Fin N × Fin N)) :=
    { toFun := fun r => ((r.1.1, r.2.1), (r.1.2, r.2.2))
      invFun := fun r => ((r.1.1, r.2.1), (r.1.2, r.2.2))
      left_inv := by rintro ⟨⟨a, b⟩, ⟨c, d⟩⟩; rfl
      right_inv := by rintro ⟨⟨a, b⟩, ⟨c, d⟩⟩; rfl }
  let F : ((Fin N × Fin N) × (Fin N × Fin N)) → ℝ := fun r =>
    if r.1.1.val + r.2.1.val = r.1.2.val + r.2.2.val then
      (v r.1.1 * v r.1.2) * (v r.2.1 * v r.2.2) else 0
  have heq : (∑ r : ((Fin N × Fin N) × (Fin N × Fin N)), F (e r)) =
      ∑ r : ((Fin N × Fin N) × (Fin N × Fin N)), F r := e.sum_comp F
  calc
    _ = ∑ r : ((Fin N × Fin N) × (Fin N × Fin N)), F r := by
      conv_rhs => rw [Fintype.sum_prod_type]
    _ = ∑ r : ((Fin N × Fin N) × (Fin N × Fin N)), F (e r) := heq.symm
    _ = _ := by
      rw [Fintype.sum_prod_type]
      apply Finset.sum_congr rfl
      rintro ⟨a, b⟩ hr
      apply Finset.sum_congr rfl
      rintro ⟨c, d⟩ hs
      dsimp only [F, e, Equiv.coe_fn_mk]
      split_ifs <;> ring

/-- T2, exactly: every nonnegative unit vector on `0,...,L`, for every L. -/
theorem elementary_convolution_bound (L : ℕ) (v : Fin (L + 1) → ℝ)
    (hv0 : ∀ j, 0 ≤ v j) (hv : ∑ j : Fin (L + 1), v j ^ 2 = 1) :
    (∑ k ∈ Finset.range (2 * (L + 1) - 1), discreteConvolution (L + 1) v k ^ 2) ≤
      (811 / 1000 : ℝ) * (L + 1) + 71 / 300 := by
  rw [← discreteEnergy_eq_convolution]
  simpa only [Nat.cast_add, Nat.cast_one] using elementary_discreteEnergy_bound (L + 1) v hv0 hv

end ChowlaCosine.P31
