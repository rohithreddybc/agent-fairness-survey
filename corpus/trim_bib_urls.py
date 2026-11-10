# -*- coding: utf-8 -*-
"""Drop the arXiv URL from entries that already carry the arXiv identifier.

One hundred and twenty-five entries print both "arXiv:2509.02007" and
"https://arxiv.org/abs/2509.02007". The second is the first with a prefix, and
it costs a wrapped line in most entries. The identifier is the citable form and
is what the ACM style renders as a link, so the URL field is removed wherever an
eprint field is present and the URL points at the same record.

Entries whose URL points somewhere else -- a project page, a DOI resolver, a
government document -- keep it.
"""
import io
import re
import sys

FILES = [r"C:\Users\rohit\Documents\Research Papers\ResearchPaper7\latex\references.bib",
         r"C:\Users\rohit\Documents\Research Papers\ResearchPaper7\review\references.bib"]


def main():
    total = 0
    for path in FILES:
        s = io.open(path, encoding="utf-8").read()
        out, pos, n = [], 0, 0
        for m in re.finditer(r"@(\w+)\{([^,]+),(.*?)\n\}", s, re.S):
            body = m.group(3)
            out.append(s[pos:m.start()])
            pos = m.end()
            new = m.group(0)
            if re.search(r"\n\s*eprint\s*=", body):
                um = re.search(r"\n\s*url\s*=\s*\{https://arxiv\.org/abs/[^}]*\}\s*,?", body)
                if um:
                    nb = body[:um.start()] + body[um.end():]
                    nb = re.sub(r",(\s*)$", r"\1", nb)
                    new = "@%s{%s,%s\n}" % (m.group(1), m.group(2), nb)
                    n += 1
            out.append(new)
        out.append(s[pos:])
        io.open(path, "w", encoding="utf-8").write("".join(out))
        print("%-14s %d url fields removed" % (path.split("\\")[-2], n))
        total += n
    return 0


if __name__ == "__main__":
    sys.exit(main())
