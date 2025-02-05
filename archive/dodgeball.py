import argparse
import functools
import json
import time
from pathlib import Path


def timeit(func) -> callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.2f}s")
        return result

    return wrapper


@timeit
def solve_game(players, startingDirection, startingPlayer):
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    direction_map = {"N": (0, 1), "NE": (1, 1), "E": (1, 0), "SE": (1, -1), "S": (0, -1), "SW": (-1, -1), "W": (-1, 0), "NW": (-1, 1)}

    current_player = startingPlayer - 1  # 0-based idx
    incoming_dir = startingDirection
    active_players = set(range(len(players)))
    throws = 0
    last_player = current_player + 1  # 1-based idx

    while True:
        cx, cy = players[current_player]
        dir_index = directions.index(incoming_dir)
        start_index = (dir_index + 1) % 8
        found = False

        for i in range(8):
            check_dir = directions[(start_index + i) % 8]
            dx, dy = direction_map[check_dir]
            candidates = []

            for p in active_players:
                if p == current_player:
                    continue
                px, py = players[p]

                # check if (px, py) is in the direction (dx, dy) from (cx, cy)
                if dx == 0:
                    if px != cx:
                        continue
                    if dy == 1 and py > cy:
                        t = py - cy
                        candidates.append((t, p))
                    elif dy == -1 and py < cy:
                        t = cy - py
                        candidates.append((t, p))
                elif dy == 0:
                    if py != cy:
                        continue
                    if dx == 1 and px > cx:
                        t = px - cx
                        candidates.append((t, p))
                    elif dx == -1 and px < cx:
                        t = cx - px
                        candidates.append((t, p))
                else:
                    # check colinear and direction sign
                    lhs = (px - cx) * dy
                    rhs = (py - cy) * dx
                    if lhs != rhs:
                        continue
                    # check direction sign
                    if dx != 0 and (px - cx) * dx < 0:
                        continue
                    if dy != 0 and (py - cy) * dy < 0:
                        continue
                    # compute t (using dx and dy which are +/-1)
                    if dx != 0:
                        t = (px - cx) // dx
                    else:
                        t = (py - cy) // dy
                    if t <= 0:
                        continue
                    candidates.append((t, p))

            if candidates:
                # find the closest (smallest t)
                candidates.sort()
                selected = candidates[0][1]
                throws += 1
                active_players.remove(current_player)
                current_player = selected
                check_dir_index = directions.index(check_dir)
                incoming_dir = directions[(check_dir_index + 4) % 8]
                last_player = selected + 1  # 1-based
                found = True
                break

        if not found:
            break

    return throws, last_player


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str)
    input_path = parser.parse_args().input
    if input_path:
        # parse any file
        input_path = Path(input_path)
        assert input_path.exists(), "input file not found"
        assert input_path.suffix == ".json", "input file must be a txt file"
        test_cases = json.loads(input_path.read_text())
        assert isinstance(test_cases, list), "input file must contain an array of test cases"
    else:
        # quick demo
        test_cases = [{"players": [[-10, -10], [-10, 10], [0, -10], [0, 10], [10, -10], [10, 10], [-9, -10], [-9, 0]], "startingDirection": "NW", "startingPlayer": 5}, {"players": [[-1000000, -1000000], [-1000000, 1000000], [0, -1000000], [0, 1000000], [1000000, -1000000], [1000000, 1000000], [-999999, -1000000], [-999999, 0]], "startingDirection": "SE", "startingPlayer": 4}]

    solution = []
    for case in test_cases:
        throws, last_player = solve_game(case["players"], case["startingDirection"], case["startingPlayer"])
        solution.append([throws, last_player])
        print(f"{throws} {last_player}")
