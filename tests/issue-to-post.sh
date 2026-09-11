#!/usr/bin/env bash

set -euo pipefail

repo_root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
fixture_dir="$repo_root/tests/fixtures/issue-to-post"
test_dir=$(mktemp -d)
trap 'rm -rf "$test_dir"' EXIT

body=$(cat "$fixture_dir/body.md")

filename=$(
  ISSUE_TITLE='My Test: Post!' \
  ISSUE_BODY="$body" \
  POST_DATE='2026-09-11' \
  POST_TIMESTAMP='2026-09-11 12:34:56' \
  POST_DIRECTORY="$test_dir/posts" \
  "$repo_root/scripts/issue-to-post.sh"
)

test "$filename" = '2026-09-11-my-test-post.markdown'
diff -u "$fixture_dir/post.markdown" "$test_dir/posts/$filename"

filename=$(
  ISSUE_TITLE='My Test: Post!' \
  ISSUE_BODY="$body" \
  ISSUE_NUMBER='123' \
  POST_DATE='2026-09-11' \
  POST_TIMESTAMP='2026-09-11 12:34:56' \
  POST_DIRECTORY="$test_dir/drafts" \
  "$repo_root/scripts/issue-to-post.sh"
)

test "$filename" = '2026-09-11-my-test-post.markdown'
diff -u "$fixture_dir/draft.markdown" "$test_dir/drafts/$filename"

echo "issue-to-post fixtures passed"
