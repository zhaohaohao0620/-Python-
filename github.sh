#!/bin/bash

git commit -m $1
git push -f origin main
git pull --rebase origin main
