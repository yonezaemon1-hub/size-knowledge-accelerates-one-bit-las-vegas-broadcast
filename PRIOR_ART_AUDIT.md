# Scoped prior-art audit (Pass 2)

Status: `PASS_PRIOR_ART_PASS2_NO_DIRECT_COLLISION_FOUND`.

This status means no direct collision was found in the targeted close literature below. It is not a universal proof that no related result exists anywhere.

## Closest literature checked

1. Garrett Parzych and Joshua J. Daymude, *Memory Lower Bounds and Impossibility Results for Anonymous Dynamic Broadcast*, DISC 2024, DOI 10.4230/LIPIcs.DISC.2024.35. Same anonymous synchronous 1-interval-connected broadcast setting; deterministic idle-start stabilizing termination has an omega(1) memory lower bound and Countdown uses O(log n) memory. No known-size two-state randomized fixed-bias runtime theorem of the present form.

2. Volker Turau, *Broadcasts in Anonymous, Dynamic Networks: A New Algorithm and Impossibility Results*, SAND 2026, DOI 10.4230/LIPIcs.SAND.2026.6. Randomized O(log log n) storage with known n and high-probability stabilization, but explicitly non-idle-start. No collision with the idle-start two-state BRF family result.

3. Henry Austin, Maximilien Gadouleau, George B. Mertzios, and Amitabh Trehan, *Amnesiac Flooding: Easy to Break, Hard to Escape*, DISC 2025, DOI 10.4230/LIPIcs.DISC.2025.10. Includes Random Flooding in a fixed, per-neighbor/port-aware graph model. This prevents any generic novelty claim for randomized flooding, but does not supply the present adversarial dynamic one-frontier Bellman/minimax result.

4. Thibaut Blanc, Giuseppe Antonio Di Luna, and Giovanni Viglietta, *Computing in Anonymous Dynamic Networks with One-Bit Communications*, arXiv:2607.08358 (2026). Their one-bit resource is message width and their algorithms are deterministic general computation; it is distinct from persistent local protocol state.

5. Ryutaro Yonezu, *Randomization Collapses the Idle-Start Memory Barrier for Anonymous Dynamic Broadcast*, Zenodo DOI 10.5281/zenodo.22643897. Direct predecessor: fair-coin BRF and its `2^{Theta(n^2)}` causal state-adaptive worst-case runtime.

## Safe novelty wording

The narrow contribution is the size-aware runtime improvement and the fixed-bias BRF-family minimax characterization in the anonymous, port-indistinguishable, adversarially dynamic idle-start stabilizing-broadcast model.

Do not claim generic novelty for randomized flooding, an exact randomized one-bit minimum, or optimality over all two-state randomized protocols.
