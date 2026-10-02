# Contributing

Thanks for helping keep this list accurate and up to date! We welcome new papers, corrected venues, better paper or code links, and fixes to the categorization.

## Suggest a paper (no coding needed)

[Open an issue](https://github.com/ZizhuoLi/awesome-image-matching-survey/issues/new/choose) using the **Add a paper** template, with the title, a link (arXiv preferred), the venue, the official code (if any), and the category you think it belongs to.

## Send a pull request

The README is generated from [`data/papers.yaml`](data/papers.yaml), so please edit that file rather than `README.md`.

1. Add an entry to `data/papers.yaml` (anywhere in the `papers` list; the README sorts entries by year automatically):

   ```yaml
   - name: LightGlue                       # short method name shown in the table
     title: 'LightGlue: Local Feature Matching at Light Speed'
     venue: ICCV                           # short venue name: CVPR, ICCV, ECCV, NeurIPS, ICLR, TPAMI, IJCV, TIP, arXiv, ...
     year: 2023
     section: sparse                       # id of a section in the `sections` list at the top of the file
     paper: https://arxiv.org/abs/2306.13643
     code: https://github.com/cvg/LightGlue  # official implementation only; omit if none
   ```

2. Regenerate the README and check that everything is consistent:

   ```bash
   pip install pyyaml
   python scripts/build_readme.py
   python scripts/build_readme.py --check
   ```

3. Commit both `data/papers.yaml` and `README.md`, and open a pull request.

## Guidelines

- **Placement:** follow the taxonomy of the survey. If a method fits several sections, choose the one that matches its main contribution.
- **Paper links:** prefer the arXiv abstract page (`https://arxiv.org/abs/...`); otherwise use the DOI or the official proceedings page.
- **Code links:** link only official implementations released by the authors. Leave `code` empty if there is none.
- **Venue:** use the venue where the paper was published; use `arXiv` for preprints and update it once the paper is accepted.
- **No duplicates:** search the README before adding an entry. Journal extensions of conference papers are listed as separate entries.
