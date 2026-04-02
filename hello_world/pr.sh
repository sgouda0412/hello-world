#!/bin/bash

# Usage: ./review-pr.sh <PR_NUMBER> [BASE_BRANCH]
# Example: ./review-pr.sh 123 main

PR_NUMBER=$1
BASE_BRANCH=${2:-main}
REMOTE=origin
BRANCH_NAME="pr-$PR_NUMBER"

if [ -z "$PR_NUMBER" ]; then
  echo "❌ Please provide a PR number"
  echo "Usage: ./review-pr.sh <PR_NUMBER> [BASE_BRANCH]"
  exit 1
fi

echo "📥 Fetching PR #$PR_NUMBER..."
git fetch $REMOTE pull/$PR_NUMBER/head:$BRANCH_NAME

echo "🔀 Checking out branch $BRANCH_NAME..."
git checkout $BRANCH_NAME || exit 1

echo "🔄 Fetching latest base branch ($BASE_BRANCH)..."
git fetch $REMOTE $BASE_BRANCH

echo "📂 Changed files:"
git diff --name-only $REMOTE/$BASE_BRANCH...$BRANCH_NAME

echo ""
echo "🔍 Summary of changes:"
git diff --stat $REMOTE/$BASE_BRANCH...$BRANCH_NAME

echo ""
echo "🧠 Commits in this PR:"
git log --oneline $REMOTE/$BASE_BRANCH..$BRANCH_NAME

echo ""
echo "🧾 Full diff (press q to exit):"
git diff $REMOTE/$BASE_BRANCH...$BRANCH_NAME | less


# Optional: grep for common issues
echo ""
echo "🔎 Checking for TODOs and debug logs..."
grep -r "TODO" . || true
grep -r "console.log" . || true

echo ""
echo "⚠️ Checking for merge conflicts with $BASE_BRANCH..."
git merge --no-commit --no-ff $REMOTE/$BASE_BRANCH > /dev/null 2>&1

if [ $? -ne 0 ]; then
  echo "❗ Merge conflicts detected!"
  git merge --abort
else
  echo "✅ No merge conflicts"
  git merge --abort > /dev/null 2>&1
fi

echo ""
echo "✅ PR review setup complete!"
echo "👉 Next: analyze code and leave feedback."
