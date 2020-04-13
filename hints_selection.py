import re
from kittens.hints.main import functions_for, regex_finditer
from kitty.fast_data_types import wcswidth


def calc_xy(text, pos, end=False):
    _, _, line_before_pos = text[:pos].rpartition("\n")
    x = wcswidth(line_before_pos) - (1 if end else 0)
    y = text.count("\n", 0, pos)
    return {"pos": pos, "x": x, "y": y}


def mark(text, args, Mark, extra_cli_args, *a):
    pattern, _ = functions_for(args)
    regex = re.compile(pattern)
    for idx, (s, e, _) in enumerate(
        regex_finditer(regex, args.minimum_match_length, text)
    ):
        mark_text = text[s:e].replace("\n", "").replace("\0", "")
        groupdict = {"start": calc_xy(text, s), "end": calc_xy(text, e, end=True)}
        yield Mark(idx, s, e, mark_text, groupdict)


def create_action_on_removal(boss, matches):
    def action_on_removal(overlay_window):
        w = boss.active_window
        w.screen.start_selection(matches[0]["start"]["x"], matches[0]["start"]["y"])
        for i, coords in enumerate(matches):
            last_match = i == len(matches) - 1
            w.screen.update_selection(
                coords["end"]["x"], coords["end"]["y"], False, last_match
            )

    return action_on_removal


def handle_result(args, data, target_window_id, boss, extra_cli_args, *a):
    matches = sorted(data["groupdicts"], key=lambda x: x["start"]["pos"])
    boss.active_window.action_on_removal = create_action_on_removal(boss, matches)
