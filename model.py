"""
Market-Making & Betting-Game Simulator

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - expected_value
import numpy as np
def expected_value(values, probabilities):
    # TODO: return the expected value of the discrete distribution (values, probabilities).
    values_array=np.array(values)
    probabilities_array=np.array(probabilities)
    return values_array.T @ probabilities_array

# Step 2 - one_reroll_die_value
def one_reroll_die_value(sides):
    # TODO: return {'value': expected winnings under optimal reroll policy, 'reroll_faces': sorted faces to reroll}
    faces=np.arange(1,sides+1,1)
    prob=np.ones(faces.shape[0]) *  (1/faces.shape[0])  
    mu=expected_value(faces,prob)
    v=np.maximum(faces,mu)
    value=expected_value(v,prob)
    reroll_faces = sorted(int(f) for f in faces[faces < mu])
    return {'value': float(value), 'reroll_faces': reroll_faces}

# Step 3 - pay_per_reroll_die_game (not yet solved)
# TODO: implement

# Step 4 - red_black_card_game_value (not yet solved)
# TODO: implement

# Step 5 - make_quotes (not yet solved)
# TODO: implement

# Step 6 - execute_trade (not yet solved)
# TODO: implement

# Step 7 - mark_to_market_pnl (not yet solved)
# TODO: implement

# Step 8 - adverse_selection_loss (not yet solved)
# TODO: implement

# Step 9 - uncertainty_spread (not yet solved)
# TODO: implement

# Step 10 - inventory_skewed_quotes (not yet solved)
# TODO: implement

# Step 11 - update_fair_value_from_trade (not yet solved)
# TODO: implement

# Step 12 - update_remaining_card_value (not yet solved)
# TODO: implement

# Step 13 - run_market_making_episode (not yet solved)
# TODO: implement

# Step 14 - summarize_episode_pnls (not yet solved)
# TODO: implement

