# -*- coding: utf-8 -*-
"""Give six entries their authors' full names.

Six author fields carried surnames only, so the bibliography printed lines like
"Buolamwini and Gebru. 2018. Gender Shades" for one of the most-cited papers in
the field. Every replacement below was read off the source record (arXiv abstract
page, or the PMLR proceedings page for Gender Shades), not recalled.

NIST and the European Parliament stay as they are: those are institutional
authors, and a single token is the correct rendering.
"""
import io
import sys

FILES = [r"C:\Users\rohit\Documents\Research Papers\ResearchPaper7\latex\references.bib",
         r"C:\Users\rohit\Documents\Research Papers\ResearchPaper7\review\references.bib"]

R = [
    ("  author = {Borah and Mihalcea},",
     "  author = {Angana Borah and Rada Mihalcea},"),
    ("  author = {Buolamwini and Gebru},",
     "  author = {Joy Buolamwini and Timnit Gebru},"),
    ("  author = {Chouldechova},",
     "  author = {Alexandra Chouldechova},"),
    ("  author = {Hu and Zhang},",
     "  author = {Yaowei Hu and Lu Zhang},"),
    ("  author = {Kambhampati},",
     "  author = {Subbarao Kambhampati},"),
    ("  author = {Kim and Diaz},",
     "  author = {To Eun Kim and Fernando Diaz},"),
    # the venue field held the preprint status and the venue at once
    ("  journal = {arXiv preprint (ACM SIGIR ICTIR 2025)},",
     "  booktitle = {ICTIR 2025},"),
]


def main():
    for path in FILES:
        s = io.open(path, encoding="utf-8").read()
        for a, b in R:
            n = s.count(a)
            assert n == 1, "%s: anchor %d for %s" % (path, n, a.strip()[:40])
            s = s.replace(a, b)
        # kim2024fair is now a proceedings paper, not a journal article
        s = s.replace("@article{kim2024fair,", "@inproceedings{kim2024fair,")
        io.open(path, "w", encoding="utf-8").write(s)
    print("6 author fields expanded, 1 venue field split, in both lanes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
