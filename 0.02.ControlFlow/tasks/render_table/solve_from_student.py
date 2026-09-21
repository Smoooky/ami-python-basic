def render_table(rows: list[list[str]], alignments: str) -> list[str]:
    if len(rows) == 0:
        return []

    count: list[int] = []
    for i in rows:
        if not count:
            for j in range(len(i)):
                count.append(len(i[j]))
        else:
            for j in range(len(i)):
                count[j] = max(count[j], len(i[j]))

    alignments_end: list[str] = []
    if len(alignments) > 1:
        for al in alignments:
            alignments_end.append(al)
    else:
        for _al2 in range(len(count)):
            alignments_end.append(alignments)
    otv = []
    if len(count) > 1:
        hate_ruff = ""
        zag = ""
        for first in range(len(count) - 1):
            hate_ruff += f"{rows[0][first]:{alignments_end[first]}{count[first]}}" + " | "
            zag += count[first] * "-" + "-+-"
        hate_ruff += f"{rows[0][-1]:{alignments_end[-1]}{count[-1]}}"
        hate_ruff = hate_ruff.rstrip()
        zag += count[-1] * "-"
    else:
        hate_ruff = f"{rows[0][0]:{alignments_end[0]}{count[0]}}".rstrip()
        zag = count[-1] * "-"
    otv.append(hate_ruff)
    otv.append(zag)
    if len(rows) > 1:
        for x in range(1, len(rows)):
            if len(count) > 1:
                hate_ruff_rep = ""
                for second in range(len(count) - 1):
                    hate_ruff_rep += f"{rows[x][second]:{alignments_end[second]}{count[second]}}"
                    hate_ruff_rep += " | "
                hate_ruff_rep += f"{rows[x][-1]:{alignments_end[-1]}{count[-1]}}"
                hate_ruff_rep = hate_ruff_rep.rstrip()
            else:
                hate_ruff_rep = f"{rows[x][0]:{alignments_end[0]}{count[0]}}".rstrip()
            otv.append(hate_ruff_rep)
    return otv
