# -*- coding: utf-8 -*-
"""Make the venue field print.

Ninety-three entries are @article carrying a booktitle and no journal. BibTeX's
article style ignores booktitle, so those ninety-three references render with
author, title and year and no venue at all -- including ones with a DOI to a
named journal. For a survey that argues about the refereed share of its own
corpus, a bibliography that hides where the work appeared is the wrong artifact.

Two repairs, by what the venue string actually names:

  a journal      -> rename booktitle to journal, entry stays @article
  anything else  -> change the entry type to @inproceedings, booktitle prints

Decoration inside the venue string ("(Oral)", "(spotlight)", "(Outstanding
Paper)") is dropped: it is not part of the venue's name. A venue string that
says a paper was *submitted* somewhere is not a venue, and is reported rather
than rewritten, since only the authors can say where that work now stands.
"""
import io
import re
import sys

FILES = [r"C:\Users\rohit\Documents\Research Papers\ResearchPaper7\latex\references.bib",
         r"C:\Users\rohit\Documents\Research Papers\ResearchPaper7\review\references.bib"]

# a venue is a journal if its name says so; conference proceedings are everything else
JOURNAL = re.compile(
    r"\b(journal|transactions|TACL|TMLR|Computing Surveys|PNAS|Science|Nature|PLoS"
    r"|Communications of the ACM|Annals|Frontiers of Computer Science|Big Data"
    r"|Computational Linguistics|Explorations Newsletter|TIST|Patterns|Minds and Machines"
    r"|Artificial Intelligence Review|Information Fusion|IEEE Access|npj)\b", re.I)

DECOR = re.compile(r"\s*\((?:oral|spotlight|outstanding paper|poster|to appear|long paper"
                   r"|short paper|best paper)\)", re.I)


def main():
    to_journal = to_proc = decor = 0
    flagged = []

    for path in FILES:
        s = io.open(path, encoding="utf-8").read()
        out = []
        pos = 0
        for m in re.finditer(r"@(\w+)\{([^,]+),(.*?)\n\}", s, re.S):
            typ, key, body = m.group(1), m.group(2), m.group(3)
            out.append(s[pos:m.start()])
            pos = m.end()
            new = m.group(0)

            if typ.lower() == "article" and not re.search(r"\n\s*journal\s*=", body):
                bm = re.search(r"(\n\s*)booktitle(\s*=\s*\{)(.*?)(\}\s*,?)", body, re.S)
                if bm:
                    venue = re.sub(r"\s+", " ", bm.group(3)).strip()

                    if re.search(r"\bsubmitted\b", venue, re.I):
                        flagged.append((key, venue))

                    clean = DECOR.sub("", venue)
                    if clean != venue:
                        decor += 1

                    if JOURNAL.search(clean):
                        field, newtyp = "journal", "article"
                        to_journal += 1
                    else:
                        field, newtyp = "booktitle", "inproceedings"
                        to_proc += 1

                    nb = (body[:bm.start()] + bm.group(1) + field + bm.group(2)
                          + clean + bm.group(4) + body[bm.end():])
                    new = "@%s{%s,%s\n}" % (newtyp, key, nb)

            out.append(new)
        out.append(s[pos:])
        io.open(path, "w", encoding="utf-8").write("".join(out))

    print("renamed booktitle -> journal : %d" % to_journal)
    print("retyped to @inproceedings    : %d" % to_proc)
    print("decoration stripped          : %d" % decor)
    if flagged:
        print("\nvenue strings that name a submission, not a publication:")
        for k, v in flagged:
            print("   %-28s %s" % (k, v))
        print("   These need a real venue or none. Left unchanged.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
