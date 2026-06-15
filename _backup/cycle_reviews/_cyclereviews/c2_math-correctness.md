main.pdf is restored. The remaining untracked PNG/PPM files (page*, t2pg*, t3pg*, tbl*) were pre-existing (not created by me — I only created files in `raster/` which I removed). I did not modify main.tex. The repo is back to its prior state except for those pre-existing untracked images. My report follows.

---

# Math-Correctness Report: AGENT_FAIRNESS_SURVEY/main.tex

**Compilation status:** `pdflatex -interaction=nonstopmode main` succeeds (exit 0, 70 pages, no `!` errors, no Undefined-control / Missing-`$` errors in the log). The regex inline-math repair did **not** break compilation.

**Verdict on the regex repair:** CLEAN. Every equation the prompt enumerated was rasterized and inspected at 200–300 dpi. No mangled formula, dropped subscript, broken set-literal, or altered operator was introduced. Details below, equation by equation.

## Equations verified correct (rasterized + cross-checked against prose)

- **§2.1 Counterfactual fairness (line 239, p7):** `P(Ŷ_{A←a}(U)=y | X=x, A=a) = P(Ŷ_{A←a'}(U)=y | X=x, A=a)` for all y and a'. CORRECT — standard Kusner et al. (2017) form; both conditioning sides are the factual `X=x, A=a`, intervention subscripts `A←a` / `A←a'` both render with hats and arrows intact. Duplicate at line 938 is identical and correct.
- **§2.7 glossary conduction eq (line 512, p15):** `Δ_τ ≈ Σ_c Δ_c · ∏_{e>c} φ_e`, feedback `Δ^(t+1) = φ_fb·Δ^(t) + Δ_entry`. CORRECT and renders cleanly.
- **§3.0 D1 (line 593):** tuple `⟨π,T,M,R⟩`; trajectory `τ=(s_0,a_0,o_0,…,a_T)`. CORRECT.
- **§3.0 D2 (lines 606–612, 960–964, p39):** `Δ_τ = d(O(τ(x)),O(τ(x')))`; `Δ_c = E[d(c(z_c(x)),c(z_c(x')))]`; full form `Δ_c(A;X,σ)=E_{x~X}[d_c(z_c(τ_A(x)),z_c(τ_A(σ(x))))]`. CORRECT.
- **§3.0 D3 (line 618):** `φ_e = Δ_out/Δ_in`; modes φ<1 / φ≈1 / φ>1 / (Δ_out>0 on Δ_in=0). CORRECT and matches prose.
- **§3.0 conduction eq (line 645, p19):** `Δ_τ ≈ Σ_c Δ_c · ∏_{e∈path(c→O)} φ_e`. CORRECT — product index renders fully.
- **§3.0 feedback recurrence + steady state (lines 649–651, p19):** `Δ^(t+1)=φ_fb·Δ^(t)+Δ_entry`; steady state `Δ_entry/(1−φ_fb)` for φ_fb<1, unbounded for φ_fb≥1. CORRECT — the fixed point of the recurrence is exactly Δ_entry/(1−φ_fb).
- **§4.2 Def 4.1 CFR (line 971, p39):** `CFR_c=(1/N)Σ 1[z_c(τ_A(x_i))≠z_c(τ_A(σ(x_i)))]`. CORRECT — indicator and ≠ render.
- **§4.2 Def 4.2 MASD (line 979, p39):** `MASD_c=(1/N)Σ|s_c(τ_A(x_i))−s_c(τ_A(σ(x_i)))|`. CORRECT.
- **§4.2 Def 4.2b MSD signed (line 984):** `E_{x~X}[s_c(τ_A(σ(x)))−s_c(τ_A(x))]` (swapped minus factual). CORRECT directional definition.
- **§4.2 disparity-ratio estimator (line 989, p39):** `φ̂_e = Δ_{c'}(A;X,σ)/Δ_c(A;X,σ)`, condition `(Δ_c>0)`. CORRECT — downstream over upstream = conduction factor.
- **§4.3 Def 4.3 TID (line 1003, p40):** `TID_cf=E[½ Σ_{t∈T}|p_{τ(x)}(t)−p_{τ(σ(x))}(t)|]`; group form ½-TV gap. CORRECT — ½ factor matches total-variation distance.
- **§4.3 Def 4.4 ESD (lines 1011–1016, p40):** `ESD_grp=|Pr(e=1|a=1)−Pr(e=1|a=0)|`; `ESD_ratio=min_a Pr/ max_a Pr` (four-fifths); cf flip rate. CORRECT.
- **§4.3 Def 4.5 PAD (lines 1021–1022, p41):** `PAD_cf=E[‖r(τ(x))−r(τ(σ(x)))‖_{1,w}]`, `‖v‖_{1,w}=Σ_{j=1}^m w_j|v_j|`; `PAD_alloc=max_ρ|...|`. CORRECT weighted ℓ1.
- **§8.4 intersectional (line 1507):** `Δ_c^{A×B}` = joint-swap Δ_c − sum of marginal Δ_c (interaction term). CORRECT definition; LaTeX `\Delta_c^{A \times B}` well-formed.
- **Abstract / Contribution 1 text-mode (lines 87, 141, p3):** inline `$\Delta_\tau$ $\approx$ $\Sigma_c$ $\Delta_c$ $\cdot$ $\Pi$ $\varphi_e$` and `$\Delta^{(t+1)}$ = $\varphi_{\mathrm{fb}}$ $\cdot$ $\Delta^{(t)}$ + $\Delta_{\mathrm{entry}}$`. CORRECT — no double-escape artifacts.

## §3.8 worked numerical example — arithmetic all CORRECT

- **Config (a) masking (lines 877, 887–889):** prompt +0.20×1.0 = +0.20; retrieval −0.24×0.83 = −0.1992 ≈ −0.20; endpoint +0.20−0.20 ≈ 0.00; Σ|Δ_c| = |+0.20|+|−0.24| = **0.44**. All correct. Note Σ|Δ_c| sums the raw component disparities (0.20+0.24), not the post-edge contributions — internally consistent and correctly labeled.
- **Config (b) super-additivity (lines 897, 907–908):** +0.15×1.6 = **0.24** > Σ|Δ_c| = 0.15. Correct.

All values match the tables (lines 887–889, 907–908) and the prose. No arithmetic error.

## Findings (no math errors; two cosmetic-notation items)

1. **SHOULD — φ vs φ glyph inconsistency (notation, not correctness).** The glossary entries at **lines 504 and 512** use `\phi` (e.g. `$\phi < 1$`, `$\prod_{e > c} \phi_e$`, `$\phi_{\text{fb}}$`), rendering the closed-loop φ glyph, whereas all 64 other occurrences throughout §3.0/§3.8/§4 use `\varphi` (open φ). Both are mathematically the same symbol, so this is purely typographic, but a reader sees two different phi shapes for the same "conduction operator." Fix: replace `\phi` with `\varphi` on lines 504 and 512 (4 occurrences of `\phi`, plus `\phi_{\text{fb}}` → `\varphi_{\mathrm{fb}}`) for consistency with the rest of the paper.

2. **SHOULD — subagent-set notation rendered in text mode at line 780.** The C3 conduction signature writes `\{A\_i\}` (literal text-mode braces with an escaped underscore), which renders as a flat "{A_i}" with a non-subscripted, literal-underscore "i" — inconsistent with D1 (line 602) and §3.3 elsewhere, which write `$\{A_i\}$` in math mode, rendering the set {A_i} with i properly subscripted. Not a math error (it is plain prose), but it is a visible inconsistency in the same notation. Fix at line 780: change `\{A\_i\}` to `$\{A_i\}$`. (The `$\pi_{\mathrm{ctrl}}$` immediately before it is already correct; only the set literal is in text mode.)

3. **NICE — glossary conduction-equation index `\prod_{e > c}` (line 512) vs. §3.0 `\prod_{e ∈ path(c→O)}` (line 645).** Both are correct and semantically equivalent (edges downstream of c on the path to the output), but the two forms differ. Optional: harmonize the glossary to `\prod_{e \in \mathrm{path}(c \to O)}` to match the formal statement. Not required.

No `must`-level issues. Nothing is broken; the recently-repaired inline math is mathematically correct everywhere I checked, and the two `should` items are pre-existing typographic inconsistencies (text-mode vs math-mode φ and {A_i}), not regex damage.