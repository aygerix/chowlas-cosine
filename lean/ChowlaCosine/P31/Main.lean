import ChowlaCosine.P31.FejerRiesz

namespace ChowlaCosine.P31

/-- T3 with exactly the requested analytic Nikolskii hypothesis;
Fejér–Riesz is now discharged by the preceding theorem. -/
theorem p31_main (w : ℕ) (A : Finset ℕ) (M C : ℝ)
    (hA : ∀ a ∈ A, 0 < a) (hM : ∀ x : ℝ, -M ≤ cosSum A x)
    (hnik : AnalyticNikolskii (A.sup id + w) C) :
    windowMass w * ((A.card : ℝ) / 2 + M ^ 2) ≤
      C * (M ^ 2 + windowEnergy w A / 2) :=
  p31_main_of_fejerRiesz w A M C hA hM (finite_fejerRiesz _) hnik


end ChowlaCosine.P31
