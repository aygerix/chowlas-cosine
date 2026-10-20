-- SOURCE ChowlaCosine/BohrTaper.lean
import ChowlaCosine.Star

/-!
# Periodic triangular Bohr tapers (P71.2)

The residue convention is `-q < 2*r ≤ q`. All frequencies are distinct positive
naturals, and the cosine lower bound is assumed at every real angle.
-/

open Finset

namespace ChowlaCosine
namespace BohrTaper

/-- The centred representative, with the positive representative at a half period. -/
def centered (q : ℕ) (a : ℤ) : ℤ :=
  if 2 * (a % (q : ℤ)) ≤ q then a % (q : ℤ) else a % (q : ℤ) - q

/-- The division-free periodic triangular taper. -/
def taper (L q P : ℕ) : Finset ℕ :=
  (Icc 1 (P * q)).filter fun a =>
    (centered q a).natAbs * (P * q) ≤ L * (P * q - a)

@[simp] theorem mem_taper (L q P a : ℕ) : a ∈ taper L q P ↔
    1 ≤ a ∧ a ≤ P * q ∧
      (centered q a).natAbs * (P * q) ≤ L * (P * q - a) := by
  simp [taper, and_assoc]

theorem taper_pos {L q P a : ℕ} (ha : a ∈ taper L q P) : 0 < a := by
  have := (mem_taper L q P a).mp ha
  omega

@[simp] theorem zero_not_mem (L q P : ℕ) : 0 ∉ taper L q P := by
  simp [mem_taper]

theorem centered_mod (q : ℕ) (a : ℤ) :
    centered q a % (q : ℤ) = a % (q : ℤ) := by
  unfold centered
  split_ifs <;> simp

theorem centered_bounds {q : ℕ} (hq : 0 < q) (a : ℤ) :
    -(q : ℤ) < 2 * centered q a ∧ 2 * centered q a ≤ q := by
  have hq' : (0 : ℤ) < q := by exact_mod_cast hq
  have hlo := Int.emod_nonneg a (ne_of_gt hq')
  have hhi := Int.emod_lt_of_pos a hq'
  unfold centered
  split_ifs <;> omega

theorem centered_repr {q : ℕ} (hq : 0 < q) (k r : ℤ)
    (hr : -(q : ℤ) < 2 * r ∧ 2 * r ≤ q) :
    centered q (k * q + r) = r := by
  have hq' : (0 : ℤ) < q := by exact_mod_cast hq
  have he : (k * (q : ℤ) + r) % q = r % q := by simp [Int.add_emod]
  unfold centered
  rw [he]
  by_cases hr0 : 0 ≤ r
  · have hlt : r < q := by omega
    rw [Int.emod_eq_of_lt hr0 hlt, if_pos hr.2]
  · have hrq0 : 0 ≤ r + q := by omega
    have hrqlt : r + q < q := by omega
    have he' : r % (q : ℤ) = r + q := by
      have := Int.emod_eq_of_lt hrq0 hrqlt
      simpa [Int.add_emod] using this
    rw [he', if_neg (by omega)]
    omega

/-- Uniqueness of the chosen residue in the specified half-open interval. -/
theorem centered_unique {q : ℕ} (hq : 0 < q) (a r : ℤ)
    (hmod : r % (q : ℤ) = a % (q : ℤ))
    (hr : -(q : ℤ) < 2 * r ∧ 2 * r ≤ q) : centered q a = r := by
  have he := centered_repr hq 0 r hr
  simpa [centered, hmod] using he

/-- A packet with residue interval `[b*h,(b+2)*h)`. -/
noncomputable def packet (q h J : ℕ) (b : ℤ) : Finset ℤ :=
  ((Icc (1 : ℤ) J) ×ˢ (Ico (b * h) ((b + 2) * h))).image
    (fun p : ℤ × ℤ => p.1 * q + p.2)

@[simp] theorem mem_packet (q h J : ℕ) (b a : ℤ) :
    a ∈ packet q h J b ↔ ∃ j r : ℤ,
      (1 ≤ j ∧ j ≤ J) ∧ (b * h ≤ r ∧ r < (b + 2) * h) ∧ a = j * q + r := by
  simp only [packet, mem_image, mem_product, mem_Icc, mem_Ico]
  constructor
  · rintro ⟨⟨j, r⟩, hjr, he⟩
    exact ⟨j, r, hjr.1, hjr.2, he.symm⟩
  · rintro ⟨j, r, hj, hr, he⟩
    exact ⟨(j, r), ⟨hj, hr⟩, he.symm⟩

theorem centered_natAbs_repr {q : ℕ} (hq : 0 < q) (k r : ℤ)
    (hr : 2 * |r| < q) :
    (centered q ((k * q + r).natAbs : ℕ)).natAbs = r.natAbs := by
  have hb : -(q : ℤ) < 2 * r ∧ 2 * r ≤ q := by
    have := le_abs_self r
    have := neg_abs_le r
    omega
  have hbn : -(q : ℤ) < 2 * (-r) ∧ 2 * (-r) ≤ q := by
    have := le_abs_self r
    have := neg_abs_le r
    omega
  rw [Int.natCast_natAbs]
  by_cases hd : 0 ≤ k * (q : ℤ) + r
  · rw [abs_of_nonneg hd, centered_repr hq k r hb]
  · rw [abs_of_neg (by omega)]
    have he : -(k * (q : ℤ) + r) = (-k) * q + (-r) := by ring
    rw [he, centered_repr hq (-k) (-r) hbn, Int.natAbs_neg]

/-- Uniqueness of short representatives, including the packet coordinate. -/
theorem repr_inj {q : ℕ} (hq : 0 < q) {j k r s : ℤ}
    (hr : 2 * |r| < q) (hs : 2 * |s| < q)
    (he : j * q + r = k * q + s) : j = k ∧ r = s := by
  have hb (t : ℤ) (ht : 2 * |t| < q) : -(q : ℤ) < 2 * t ∧ 2 * t ≤ q := by
    have := le_abs_self t
    have := neg_abs_le t
    omega
  have hres := congrArg (centered q) he
  rw [centered_repr hq j r (hb r hr), centered_repr hq k s (hb s hs)] at hres
  have hq' : (q : ℤ) ≠ 0 := by exact_mod_cast ne_of_gt hq
  exact ⟨mul_right_cancel₀ hq' (by linarith [he]), hres⟩

/-- Exact integer substitute for the decimal longitudinal estimates in the paper proof. -/
theorem short_longitudinal {h q P J : ℕ} (hP : 100 ≤ P) (hq : 80 * h + 1 ≤ q)
    (hJ : 8 * J ≤ P) {j r : ℤ} (hj : |j| ≤ J) (hr : |r| ≤ 32 * h) :
    20 * |j * q + r| ≤ 3 * (P : ℤ) * q := by
  have hP' : (100 : ℤ) ≤ P := by exact_mod_cast hP
  have hq' : 80 * (h : ℤ) + 1 ≤ q := by exact_mod_cast hq
  have hJ' : 8 * (J : ℤ) ≤ P := by exact_mod_cast hJ
  have hab : |j * (q : ℤ) + r| ≤ (J : ℤ) * q + 32 * h := by
    calc
      _ ≤ |j * (q : ℤ)| + |r| := abs_add_le _ _
      _ = |j| * (q : ℤ) + |r| := by rw [abs_mul, abs_of_nonneg (Int.natCast_nonneg q)]
      _ ≤ (J : ℤ) * q + 32 * h := add_le_add
        (mul_le_mul_of_nonneg_right hj (Int.natCast_nonneg q)) hr
  have hprod : 1280 * (h : ℤ) ≤ (P : ℤ) * q := by nlinarith
  have hJq := mul_le_mul_of_nonneg_right hJ' (Int.natCast_nonneg q)
  nlinarith only [hab, hprod, hJq]

/-- Every nonzero short representative with transverse radius at most `17h` lies in the taper. -/
theorem short_mem {h q P J : ℕ} (hP : 100 ≤ P) (hq : 80 * h + 1 ≤ q)
    (hJ : 8 * J ≤ P) (j r : ℤ) (hne : j * q + r ≠ 0)
    (hj : |j| ≤ J) (hr : |r| ≤ 17 * h) :
    (j * q + r).natAbs ∈ taper (20 * h) q P := by
  have hq0 : 0 < q := by omega
  have hq' : 80 * (h : ℤ) + 1 ≤ q := by exact_mod_cast hq
  have ht := short_longitudinal hP hq hJ hj (show |r| ≤ 32 * h by omega)
  have hres := centered_natAbs_repr hq0 j r (show 2 * |r| < q by omega)
  have hpos : 1 ≤ (j * (q : ℤ) + r).natAbs := by
    have := Int.natAbs_pos.mpr hne
    omega
  have hle : (j * (q : ℤ) + r).natAbs ≤ P * q := by
    have hle' : ((j * (q : ℤ) + r).natAbs : ℤ) ≤ ((P * q : ℕ) : ℤ) := by
      simp only [Int.natCast_natAbs, Nat.cast_mul]
      nlinarith [abs_nonneg (j * (q : ℤ) + r)]
    exact_mod_cast hle'
  rw [mem_taper]
  refine ⟨hpos, hle, ?_⟩
  rw [hres]
  have hr' : (r.natAbs : ℤ) ≤ 17 * h := by simpa only [Int.natCast_natAbs] using hr
  have hrad := mul_le_mul_of_nonneg_right hr' (show (0 : ℤ) ≤ (P : ℤ) * q by positivity)
  have ht' := mul_le_mul_of_nonneg_left ht (Int.natCast_nonneg h)
  have hh : (h : ℤ) * (P : ℤ) * q ≥ 0 := by positivity
  have hfinal : (r.natAbs : ℤ) * ((P : ℤ) * q) ≤
      (20 * (h : ℤ)) * ((P : ℤ) * q - (j * (q : ℤ) + r).natAbs) := by
    simp only [Int.natCast_natAbs] at hrad ⊢
    nlinarith
  exact_mod_cast hfinal

/-- Each packet has exactly `2hJ` distinct integer vertices. -/
theorem packet_card {h q J : ℕ} (hq : 80 * h + 1 ≤ q) (b : ℤ) :
    (packet q h J b).card = 2 * h * J := by
  have hq0 : 0 < q := by omega
  have hq' : 80 * (h : ℤ) + 1 ≤ q := by exact_mod_cast hq
  have hinj : Set.InjOn (fun p : ℤ × ℤ => p.1 * (q : ℤ) + p.2)
      ↑((Icc (1 : ℤ) J) ×ˢ Ico (b * h) ((b + 2) * h)) := by
    intro x hx y hy he
    simp only [mem_coe, mem_product, mem_Icc, mem_Ico] at hx hy
    have hxx : 2 * |x.2 - b * h| < q := by
      rw [abs_of_nonneg (by omega)]
      nlinarith
    have hyy : 2 * |y.2 - b * h| < q := by
      rw [abs_of_nonneg (by omega)]
      nlinarith
    have hi := repr_inj hq0 hxx hyy
      (show x.1 * (q : ℤ) + (x.2 - b * h) = y.1 * q + (y.2 - b * h) by linarith)
    exact Prod.ext hi.1 (by linarith [hi.2])
  rw [packet, card_image_of_injOn hinj, card_product, Int.card_Icc, Int.card_Ico]
  have he : (b + 2) * (h : ℤ) - b * h = (2 * h : ℕ) := by push_cast; ring
  rw [he]
  simp only [add_sub_cancel_right, Int.toNat_natCast]
  ring

/-- Coordinate bounds shared by the three packets. -/
theorem packet_coordinates {h q J : ℕ} {b a : ℤ} (hb : -16 ≤ b ∧ b ≤ 14)
    (ha : a ∈ packet q h J b) : ∃ j r : ℤ,
    (1 ≤ j ∧ j ≤ J) ∧ (-16 * h ≤ r ∧ r < 16 * h) ∧
      (b * h ≤ r ∧ r < (b + 2) * h) ∧ a = j * q + r := by
  obtain ⟨j, r, hj, hr, he⟩ := (mem_packet q h J b a).mp ha
  refine ⟨j, r, hj, ?_, hr, he⟩
  constructor <;> nlinarith [Int.natCast_nonneg h]

theorem packets_disjoint {h q J : ℕ} (hh : 0 < h) (hq : 80 * h + 1 ≤ q)
    {b c : ℤ} (hb : -16 ≤ b ∧ b ≤ 14) (hc : -16 ≤ c ∧ c ≤ 14)
    (hbc : b + 2 ≤ c) : Disjoint (packet q h J b) (packet q h J c) := by
  apply disjoint_left.mpr
  intro a ha hac
  obtain ⟨j, r, _, hr, hbr, he⟩ := packet_coordinates hb ha
  obtain ⟨k, s, _, hs, hcs, he'⟩ := packet_coordinates hc hac
  have hq' : 80 * (h : ℤ) + 1 ≤ q := by exact_mod_cast hq
  have hrabs : |r| ≤ 16 * (h : ℤ) := by rw [abs_le]; omega
  have hsabs : |s| ≤ 16 * (h : ℤ) := by rw [abs_le]; omega
  have hres := repr_inj (show 0 < q by omega)
    (show 2 * |r| < q by omega) (show 2 * |s| < q by omega) (he.symm.trans he')
  have hh' : (0 : ℤ) < h := by exact_mod_cast hh
  nlinarith [hres.2]

/-- The three packets themselves consist of admissible positive frequencies. -/
theorem packet_subset_taper {h q P J : ℕ} (hP : 100 ≤ P)
    (hq : 80 * h + 1 ≤ q) (hJ : 8 * J ≤ P) {b a : ℤ}
    (hb : -16 ≤ b ∧ b ≤ 14) (ha : a ∈ packet q h J b) :
    0 < a ∧ a.natAbs ∈ taper (20 * h) q P := by
  obtain ⟨j, r, hj, hr, _, rfl⟩ := packet_coordinates hb ha
  have hq' : 80 * (h : ℤ) + 1 ≤ q := by exact_mod_cast hq
  have hpos : 0 < j * (q : ℤ) + r := by nlinarith [Int.natCast_nonneg h]
  exact ⟨hpos, short_mem hP hq hJ j r (ne_of_gt hpos)
    (by rw [abs_of_nonneg (by omega)]; omega) (by rw [abs_le]; omega)⟩

/-- All distinct pairs within a packet or between adjacent packets are edges. -/
theorem packet_edge {h q P J : ℕ} (hP : 100 ≤ P)
    (hq : 80 * h + 1 ≤ q) (hJ : 8 * J ≤ P) {b c u v : ℤ}
    (hu : u ∈ packet q h J b) (hv : v ∈ packet q h J c)
    (hbc : |b - c| ≤ 15) (hne : u ≠ v) :
    (u - v).natAbs ∈ taper (20 * h) q P := by
  obtain ⟨j, r, hj, hr, rfl⟩ := (mem_packet q h J b u).mp hu
  obtain ⟨k, s, hk, hs, rfl⟩ := (mem_packet q h J c v).mp hv
  have he : j * (q : ℤ) + r - (k * q + s) = (j - k) * q + (r - s) := by ring
  rw [he]
  apply short_mem hP hq hJ (j - k) (r - s)
  · rw [← he]
    exact sub_ne_zero.mpr hne
  · rw [abs_le]
    omega
  · rw [abs_le] at hbc ⊢
    constructor <;> nlinarith [Int.natCast_nonneg h]

/-- The outer packets have no connecting edges. -/
theorem packet_nonedge {h q P J : ℕ} (hh : 0 < h) (hP : 100 ≤ P)
    (hq : 80 * h + 1 ≤ q) {u v : ℤ}
    (hu : u ∈ packet q h J (-16)) (hv : v ∈ packet q h J 14) :
    (u - v).natAbs ∉ taper (20 * h) q P := by
  obtain ⟨j, r, hj, hr, rfl⟩ := (mem_packet q h J (-16) u).mp hu
  obtain ⟨k, s, hk, hs, rfl⟩ := (mem_packet q h J 14 v).mp hv
  intro ha
  have hq' : 80 * (h : ℤ) + 1 ≤ q := by exact_mod_cast hq
  have hh' : (0 : ℤ) < h := by exact_mod_cast hh
  have he : j * (q : ℤ) + r - (k * q + s) = (j - k) * q + (r - s) := by ring
  rw [he] at ha
  have hres := centered_natAbs_repr (show 0 < q by omega) (j - k) (r - s)
    (show 2 * |r - s| < q by rw [abs_of_neg (by nlinarith)]; nlinarith)
  have ha' := (mem_taper (20 * h) q P _).mp ha
  rw [hres] at ha'
  have hrad : (r - s).natAbs ≤ 20 * h := by
    have hPq : 0 < P * q := Nat.mul_pos (by omega) (by omega)
    nlinarith [Nat.mul_le_mul_left (20 * h) (show P * q - ((j - k) * (q : ℤ) + (r - s)).natAbs ≤ P * q by omega)]
  have hrad' : ((r - s).natAbs : ℤ) ≤ 20 * (h : ℤ) := by exact_mod_cast hrad
  rw [Int.natCast_natAbs] at hrad'
  rw [abs_of_neg (by nlinarith)] at hrad'
  nlinarith

/-- The weighted adjacency form with separately specified row and column sets. -/
noncomputable def form (A : Finset ℕ) (S T : Finset ℤ) (v : ℤ → ℝ) : ℝ :=
  ∑ u ∈ S, ∑ w ∈ T, v u * v w * (if (u - w).natAbs ∈ A then 1 else 0)

theorem form_clique {A : Finset ℕ} (h0 : 0 ∉ A) (S : Finset ℤ)
    (v : ℤ → ℝ) (c : ℝ) (hv : ∀ u ∈ S, v u = c)
    (he : ∀ u ∈ S, ∀ w ∈ S, u ≠ w → (u - w).natAbs ∈ A) :
    form A S S v = c ^ 2 * ((S.card : ℝ) ^ 2 - S.card) := by
  have hrow : ∀ u ∈ S, ∑ w ∈ S, v u * v w *
      (if (u - w).natAbs ∈ A then 1 else 0) = (S.card : ℝ) * (c * c) - c * c := by
    intro u hu
    have ht : ∀ w ∈ S, v u * v w * (if (u - w).natAbs ∈ A then 1 else 0) =
        c * c - (if u = w then c * c else 0) := by
      intro w hw
      rw [hv u hu, hv w hw]
      by_cases huw : u = w
      · subst w
        simp [h0]
      · simp [huw, he u hu w hw huw]
    rw [sum_congr rfl ht, sum_sub_distrib, sum_ite_eq, if_pos hu]
    simp
  rw [form, sum_congr rfl hrow]
  simp only [sum_const, nsmul_eq_mul]
  ring

theorem form_complete {A : Finset ℕ} (S T : Finset ℤ)
    (v : ℤ → ℝ) (c d : ℝ) (hv : ∀ u ∈ S, v u = c) (hvw : ∀ w ∈ T, v w = d)
    (he : ∀ u ∈ S, ∀ w ∈ T, (u - w).natAbs ∈ A) :
    form A S T v = (S.card : ℝ) * T.card * c * d := by
  unfold form
  have ht : ∀ u ∈ S, ∀ w ∈ T,
      v u * v w * (if (u - w).natAbs ∈ A then 1 else 0) = c * d := by
    intro u hu w hw
    rw [hv u hu, hvw w hw, if_pos (he u hu w hw), mul_one]
  simp_rw [sum_congr rfl (fun u hu => sum_congr rfl (ht u hu))]
  simp only [sum_const, nsmul_eq_mul]
  ring

theorem form_empty {A : Finset ℕ} (S T : Finset ℤ) (v : ℤ → ℝ)
    (he : ∀ u ∈ S, ∀ w ∈ T, (u - w).natAbs ∉ A) : form A S T v = 0 := by
  unfold form
  apply sum_eq_zero
  intro u hu
  apply sum_eq_zero
  intro w hw
  simp [he u hu w hw]

/-- The exact induced three-clique certificate used in P71.2. -/
theorem three_clique_bound (A : Finset ℕ) (hA : ∀ a ∈ A, 0 < a) (M : ℝ)
    (hM : ∀ x : ℝ, -M ≤ cosSum A x) (U V W : Finset ℤ) (m : ℕ)
    (hm : 0 < m) (hU : U.card = m) (hV : V.card = m) (hW : W.card = m)
    (hUV : Disjoint U V) (hUW : Disjoint U W) (hVW : Disjoint V W)
    (hUU : ∀ u ∈ U, ∀ w ∈ U, u ≠ w → (u - w).natAbs ∈ A)
    (hVV : ∀ u ∈ V, ∀ w ∈ V, u ≠ w → (u - w).natAbs ∈ A)
    (hWW : ∀ u ∈ W, ∀ w ∈ W, u ≠ w → (u - w).natAbs ∈ A)
    (heUV : ∀ u ∈ U, ∀ w ∈ V, (u - w).natAbs ∈ A)
    (heVW : ∀ u ∈ V, ∀ w ∈ W, (u - w).natAbs ∈ A)
    (hnUW : ∀ u ∈ U, ∀ w ∈ W, (u - w).natAbs ∉ A) :
    7 * (m : ℝ) / 34 + 1 / 2 ≤ M := by
  have h0 : 0 ∉ A := fun h => by have := hA 0 h; omega
  let v : ℤ → ℝ := fun u => if u ∈ V then -3 else 2
  have hvU : ∀ u ∈ U, v u = 2 := by
    intro u hu
    exact if_neg (fun hv => disjoint_left.mp hUV hu hv)
  have hvV : ∀ u ∈ V, v u = -3 := by intro u hu; exact if_pos hu
  have hvW : ∀ u ∈ W, v u = 2 := by
    intro u hu
    exact if_neg (fun hv => disjoint_left.mp hVW hv hu)
  have hflip (u w : ℤ) : (u - w).natAbs = (w - u).natAbs := by rw [← Int.natAbs_neg (u - w), neg_sub]
  have hfUU := form_clique h0 U v 2 hvU hUU
  have hfVV := form_clique h0 V v (-3) hvV hVV
  have hfWW := form_clique h0 W v 2 hvW hWW
  have hfUV := form_complete U V v 2 (-3) hvU hvV heUV
  have hfVU := form_complete V U v (-3) 2 hvV hvU
    (fun u hu w hw => by rw [hflip]; exact heUV w hw u hu)
  have hfVW := form_complete V W v (-3) 2 hvV hvW heVW
  have hfWV := form_complete W V v 2 (-3) hvW hvV
    (fun u hu w hw => by rw [hflip]; exact heVW w hw u hu)
  have hfUW := form_empty U W v hnUW
  have hfWU := form_empty W U v
    (fun u hu w hw => by rw [hflip]; exact hnUW w hw u hu)
  have hUVW : Disjoint (U ∪ V) W := disjoint_union_left.mpr ⟨hUW, hVW⟩
  have hform : form A (U ∪ V ∪ W) (U ∪ V ∪ W) v =
      -7 * (m : ℝ) ^ 2 - 17 * m := by
    have hexpand : form A (U ∪ V ∪ W) (U ∪ V ∪ W) v =
        (form A U U v + form A U V v + form A U W v) +
        (form A V U v + form A V V v + form A V W v) +
        (form A W U v + form A W V v + form A W W v) := by
      simp only [form, sum_union hUVW, sum_union hUV, sum_add_distrib]
    rw [hexpand, hfUU, hfVV, hfWW, hfUV, hfVU, hfVW, hfWV, hfUW, hfWU, hU, hV, hW]
    ring
  have hnorm : ∑ u ∈ U ∪ V ∪ W, (v u) ^ 2 = 17 * (m : ℝ) := by
    rw [sum_union hUVW, sum_union hUV,
      sum_congr rfl (fun u hu => congrArg (fun t : ℝ => t ^ 2) (hvU u hu)),
      sum_congr rfl (fun u hu => congrArg (fun t : ℝ => t ^ 2) (hvV u hu)),
      sum_congr rfl (fun u hu => congrArg (fun t : ℝ => t ^ 2) (hvW u hu))]
    simp only [sum_const, nsmul_eq_mul, hU, hV, hW]
    ring
  have hs := star_lemma A hA M hM (U ∪ V ∪ W) v
  change form A (U ∪ V ∪ W) (U ∪ V ∪ W) v ≥ _ at hs
  rw [hform, hnorm] at hs
  have hm' : (0 : ℝ) < m := by exact_mod_cast hm
  nlinarith

/-- P71.2 in the equivalent parametrization `L = 20h`. -/
theorem lower_bound_mul_twenty {h q P : ℕ} (hh : 0 < h) (hP : 100 ≤ P)
    (hq : 80 * h + 1 ≤ q) (M : ℝ)
    (hM : ∀ x : ℝ, -M ≤ cosSum (taper (20 * h) q P) x) :
    7 * (2 * h * (P / 8) : ℕ) / 34 + 1 / 2 ≤ M := by
  have hJ : 8 * (P / 8) ≤ P := Nat.mul_div_le P 8
  have hJ0 : 0 < P / 8 := by omega
  have hUV := packets_disjoint (J := P / 8) hh hq
    (b := -16) (c := -1) (by norm_num) (by norm_num) (by norm_num)
  have hUW := packets_disjoint (J := P / 8) hh hq
    (b := -16) (c := 14) (by norm_num) (by norm_num) (by norm_num)
  have hVW := packets_disjoint (J := P / 8) hh hq
    (b := -1) (c := 14) (by norm_num) (by norm_num) (by norm_num)
  apply three_clique_bound (taper (20 * h) q P) (fun _ ha => taper_pos ha) M hM
    (packet q h (P / 8) (-16)) (packet q h (P / 8) (-1)) (packet q h (P / 8) 14)
    (2 * h * (P / 8)) (by positivity)
    (packet_card hq _) (packet_card hq _) (packet_card hq _) hUV hUW hVW
  · intro u hu v hv hne
    exact packet_edge hP hq hJ hu hv (by norm_num) hne
  · intro u hu v hv hne
    exact packet_edge hP hq hJ hu hv (by norm_num) hne
  · intro u hu v hv hne
    exact packet_edge hP hq hJ hu hv (by norm_num) hne
  · intro u hu v hv
    exact packet_edge hP hq hJ hu hv (by norm_num)
      (fun he => disjoint_left.mp hUV hu (he ▸ hv))
  · intro u hu v hv
    exact packet_edge hP hq hJ hu hv (by norm_num)
      (fun he => disjoint_left.mp hVW hu (he ▸ hv))
  · exact fun u hu v hv => packet_nonedge hh hP hq hu hv

/-- **P71.2 (main):** the exact linear lower bound for all admissible parameters. -/
theorem lower_bound {L q P : ℕ} (hL : 20 ∣ L) (hL0 : 20 ≤ L)
    (hP : 100 ≤ P) (hq : 4 * L + 1 ≤ q) (M : ℝ)
    (hM : ∀ x : ℝ, -M ≤ cosSum (taper L q P) x) :
    7 * (2 * (L / 20) * (P / 8) : ℕ) / 34 + 1 / 2 ≤ M := by
  have hLdiv : 20 * (L / 20) = L := Nat.mul_div_cancel' hL
  have hh : 0 < L / 20 := by omega
  have hq' : 80 * (L / 20) + 1 ≤ q := by omega
  have hs := lower_bound_mul_twenty hh hP hq' M (by simpa only [hLdiv] using hM)
  exact hs

/-- There are at most `P` admissible frequencies for each of the `2L+1` residues. -/
theorem card_taper_le (L q P : ℕ) (hq : 0 < q) (hP : 0 < P) :
    (taper L q P).card ≤ (2 * L + 1) * P := by
  let f : ℕ → ℕ × ℤ := fun a => ((a - 1) / q, centered q a)
  have hPq : 0 < P * q := Nat.mul_pos hP hq
  have hres : ∀ a ∈ taper L q P, (centered q a).natAbs ≤ L := by
    intro a ha
    have ha' := (mem_taper L q P a).mp ha
    have hsub : P * q - a ≤ P * q := Nat.sub_le _ _
    have := Nat.mul_le_mul_left L hsub
    nlinarith
  have hf : Set.MapsTo f ↑(taper L q P)
      ↑((range P) ×ˢ Icc (-(L : ℤ)) L) := by
    intro a ha
    have ha' := (mem_taper L q P a).mp ha
    simp only [mem_coe, mem_product, mem_range, mem_Icc, f]
    constructor
    · apply (Nat.div_lt_iff_lt_mul hq).mpr
      omega
    · have hr : ((centered q a).natAbs : ℤ) ≤ L := by exact_mod_cast hres a ha
      rw [Int.natCast_natAbs, abs_le] at hr
      exact hr
  have hinj : Set.InjOn f ↑(taper L q P) := by
    intro a ha b hb he
    have ha1 := ((mem_taper L q P a).mp ha).1
    have hb1 := ((mem_taper L q P b).mp hb).1
    have he1 : (a - 1) / q = (b - 1) / q := congrArg Prod.fst he
    have he2 : centered q a = centered q b := congrArg Prod.snd he
    have hm : (a : ℤ) % (q : ℤ) = (b : ℤ) % (q : ℤ) := by
      rw [← centered_mod q a, ← centered_mod q b, he2]
    have hm' : ((a - 1 : ℕ) : ℤ) % (q : ℤ) = ((b - 1 : ℕ) : ℤ) % (q : ℤ) := by
      rw [Nat.cast_sub ha1, Nat.cast_sub hb1, Nat.cast_one]
      exact Int.ModEq.sub hm (Int.ModEq.refl 1)
    have hmnat : (a - 1) % q = (b - 1) % q := by exact_mod_cast hm'
    have hab : a - 1 = b - 1 := by
      calc
        a - 1 = (a - 1) % q + q * ((a - 1) / q) := (Nat.mod_add_div _ _).symm
        _ = (b - 1) % q + q * ((b - 1) / q) := by rw [hmnat, he1]
        _ = b - 1 := Nat.mod_add_div _ _
    omega
  have hc := card_le_card_of_injOn f hf hinj
  rw [card_product, card_range, Int.card_Icc] at hc
  have he : ((L : ℤ) + 1 - -(L : ℤ)) = ((2 * L + 1 : ℕ) : ℤ) := by push_cast; ring
  rw [he, Int.toNat_natCast] at hc
  simpa only [Nat.mul_comm] using hc

/-- The common packet size is at least `LP/90`. -/
theorem packet_size_lower {L P : ℕ} (hL : 20 ∣ L) (hP : 100 ≤ P) :
    (L : ℝ) * P / 90 ≤ (2 * (L / 20) * (P / 8) : ℕ) := by
  have hLdiv : 20 * (L / 20) = L := Nat.mul_div_cancel' hL
  have hJ : P ≤ 9 * (P / 8) := by omega
  have hLdiv' : (20 : ℝ) * (L / 20 : ℕ) = L := by exact_mod_cast hLdiv
  have hJ' : (P : ℝ) ≤ 9 * (P / 8 : ℕ) := by exact_mod_cast hJ
  have hp := mul_le_mul_of_nonneg_left hJ' (Nat.cast_nonneg (L / 20) : (0 : ℝ) ≤ (L / 20 : ℕ))
  push_cast
  nlinarith

/-- **P71.2 (cardinality corollary):** `M ≥ 7|A|/6290 + 1/2`. -/
theorem lower_bound_card {L q P : ℕ} (hL : 20 ∣ L) (hL0 : 20 ≤ L)
    (hP : 100 ≤ P) (hq : 4 * L + 1 ≤ q) (M : ℝ)
    (hM : ∀ x : ℝ, -M ≤ cosSum (taper L q P) x) :
    7 * ((taper L q P).card : ℝ) / 6290 + 1 / 2 ≤ M := by
  have hs := lower_bound hL hL0 hP hq M hM
  have hm := packet_size_lower hL hP
  have hc := card_taper_le L q P (by omega) (by omega)
  have hc' : ((taper L q P).card : ℝ) ≤ (2 * (L : ℝ) + 1) * P := by exact_mod_cast hc
  have hL' : (20 : ℝ) ≤ L := by exact_mod_cast hL0
  have hcomp : (2 * (L : ℝ) + 1) * P ≤ 41 / 20 * L * P := by
    have hp : (0 : ℝ) ≤ P := Nat.cast_nonneg _
    nlinarith
  nlinarith

end BohrTaper
end ChowlaCosine
