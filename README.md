## ICC Mise à Niveau
Collection of the class notes and exercices of the ICC Class for EPFL MAN 2025\
There are some extra exercices in `./scripts`, related to other classes

Give the repo a star if it helps you out!

## Git usage guide

In the repository's root folder (where the .git folder is)

  1. `git pull` : *mettre à jour les modification des autres localement*
  2. ✨ Coding time ✨
  3. `git add modified_file` or `git add .` in the root : *ajoute les fichiers modifiés au working tree*
  4. `git commit -m "changes description"` : *ajoute les modifications à l'historique locale*
  5. `git push` : *synchronise à la repo sur github*

If `git push` fails (i.e. qqun à modifié la repo en ligne entre temps):
  1. `git pull --rebase` : *combine les nouvelles modifications avec les tiennes*
  2. `git push` : *synchroniser*
