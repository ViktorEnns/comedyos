---
id: ROAST-ELO-003
title: Competitive ELO Rating, Matchmaking & Leaderboards
parent: "[[00_Roast_With_Friends_Master]]"
tags: [roast, elo, ranking, matchmaking, social]
---

# 🏆 Competitive ELO Rating, Matchmaking & Leaderboards

Unlike solo stand-up (which is non-adversarial), Roast Battles fit standard competitive rating mathematics with mathematical elegance.

---

## 📈 ELO Mathematical Model

The expected score $E_A$ for Comic A competing against Comic B is calculated as:

$$E_A = \frac{1}{1 + 10^{(R_B - R_A)/400}}$$

Upon completion of the battle, ratings are updated:

$$R_A' = R_A + K \cdot (S_A - E_A)$$

Where:
* $R_A, R_B$ = Pre-match ELO ratings.
* $S_A$ = Match outcome: $1.0$ (Win), $0.5$ (Draw), $0.0$ (Loss).
* $K$ = Volatility factor:
  - $K = 32$ for unranked / new accounts (< 10 battles).
  - $K = 16$ for seasoned veterans (> 25 battles).

---

## 🥇 Rank Tiers

| Rank Tier | ELO Range | Title Badge | Perks & Unlocks |
| :--- | :--- | :--- | :--- |
| **Bronze** | $800 - 1199$ | **Open Mic Heckler** | Basic 1v1 Battle Mode, Local Matchmaking |
| **Silver** | $1200 - 1499$ | **Club Regular** | Unlock Cypher Mode & Topic Sprint |
| **Gold** | $1500 - 1799$ | **Feature Act** | Host Private Tournaments, Green Room Invites |
| **Platinum**| $1800 - 2099$ | **Headliner** | Verified Comic Badge, Public Leaderboard |
| **Diamond** | $2100+$ | **Roastmaster General** | Seasonal Invitational Showcases |

---

## 👥 Two Ladder Tracks: Social vs. Global

1. **Private Circle / Crew Leaderboards:**
   - Designed for local friend groups, writers' rooms, or specific comedy club cliques (e.g., *"Austin Green Room Crew"*).
   - Keeps competition private, fun, and non-intimidating.
2. **Global Verified Circuit:**
   - Optional competitive league for registered comedians with video-verified acoustic sets.
