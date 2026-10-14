import random

def player(prev_play, opponent_history=[]):
    if prev_play == "":
        opponent_history.clear()
        
    opponent_history.append(prev_play)
    
    
    if len(opponent_history) < 5:
        return random.choice(["R", "P", "S"])
    
    
    n = 5
    if len(opponent_history) > n:

        last_sequence = "".join(opponent_history[-n:])
        

        options = {}
        for i in range(len(opponent_history) - n):
            seq = "".join(opponent_history[i:i+n])
            nxt = opponent_history[i+n]
            if seq == last_sequence:
                options[nxt] = options.get(nxt, 0) + 1
                
        if options:

            predicted_opponent_move = max(options, key=options.get)
        else:
            predicted_opponent_move = opponent_history[-1]
    else:
        predicted_opponent_move = opponent_history[-1]

    counter_moves = {"R": "P", "P": "S", "S": "R"}
    
    return counter_moves[predicted_opponent_move]