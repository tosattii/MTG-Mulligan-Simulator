# Mulligan Heuristic Simulator

This project simulates mulligan decisions in a simplified card game to test how well simple land-count heuristics identify hands that can actually produce a playable game.

## Model

The simulation uses a synthetic 60-card deck represented only by mana costs:

* 24 lands (cost 0)
* 12 one-mana spells
* 12 two-mana spells
* 8 three-mana spells
* 4 four-mana spells

Each simulation starts with a 7-card opening hand. The player is assumed to be on the play and draws one card at the start of turns 2 and 3. On each turn, the player plays at most one land and then casts the cheapest spell that can be afforded with the available mana.

For this project, a hand is considered **playable** if the simulation successfully casts at least one spell on **turns 1, 2, and 3**.

The heuristic being tested is a simple land-count rule: keep the hand when the number of lands falls within a chosen minimum-to-maximum range.

## Method

For each of the 12 land-count ranges, the simulation evaluates **10,000 random opening hands**. A fixed random seed is used so that the table below is exactly reproducible.

| Range | False positives | False negatives | Total error |
| ----- | --------------: | --------------: | ----------: |
| 1–3   |          12.36% |          15.24% |      27.60% |
| 1–4   |          20.01% |           2.69% |      22.70% |
| 1–5   |          24.57% |           0.02% |      24.59% |
| 1–6   |          25.95% |           0.00% |      25.95% |
| 2–3   |           9.54% |          24.58% |      34.12% |
| 2–4   |          16.86% |          11.46% |      28.32% |
| 2–5   |          21.25% |           9.50% |      30.75% |
| 2–6   |          22.39% |           9.37% |      31.76% |
| 3–3   |           6.41% |          47.60% |      54.01% |
| 3–4   |          13.73% |          35.05% |      48.78% |
| 3–5   |          18.75% |          32.46% |      51.21% |
| 3–6   |          19.13% |          33.10% |      52.23% |

A **false positive** is a hand that the heuristic recommends keeping even though the simulation cannot play a spell on all three turns.

A **false negative** is a hand that the heuristic recommends throwing away even though the simulation considers it playable.

## Results

The usual **2–5 land rule** has an error rate of approximately **31%** in this simulation.

The best-performing range is **1–4 lands**, at **22.7%**.

The most striking result is that keeping one-land hands improves performance — a decision no experienced player would make at the table. Under this model, many one-land hands still develop correctly, because the two draws on turns 2 and 3 frequently supply the missing land.

The results also suggest that the **minimum land count matters far more than the maximum**. Raising the maximum from four to six changes the total error by roughly one percentage point, while raising the minimum from one to three more than doubles it. One possible explanation is that high-land hands are uncommon enough that the maximum rarely binds, but this simulation does not measure their frequency directly.

These results apply only to the model defined above and should not be interpreted as a general evaluation of mulligan strategy.

## Limitations

This simulation is intentionally simplified.

It stops after **turn 3**, so it does not measure longer-term game outcomes.

The deck is **synthetic** and is represented only by mana costs. It does not model card types, effects, interaction, card advantage, or actual deck construction.

The simulation assumes the player is **always on the play**.

It also **ignores mana colors**, so every spell can be cast as long as its numerical mana cost can be paid.

Most importantly, a "playable" hand here means only that the model successfully casts a spell on turns 1, 2, and 3. That is a narrow proxy for hand quality, not a measurement of whether a hand is actually good in a real game.

This project is an experiment in simulation and heuristic evaluation, **not gameplay advice**.

## Running it

The simulation requires only **Python 3** and has no external dependencies.

```bash
python mulligan.py
```

## Future work

Replace the synthetic deck with real tournament decklists, extend the simulation through turn 5, and model mana colors.

## Author

Davi Tosatti
