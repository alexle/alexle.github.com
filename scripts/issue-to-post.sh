#!/usr/bin/env bash

set -euo pipefail

: "${ISSUE_TITLE:?ISSUE_TITLE is required}"
: "${ISSUE_BODY:?ISSUE_BODY is required}"
: "${POST_DATE:?POST_DATE is required}"
: "${POST_DIRECTORY:?POST_DIRECTORY is required}"

body=$ISSUE_BODY
tags=""

if echo "$body" | grep -q "Tags:"; then
  tags=$(echo "$body" | grep "Tags:" | sed 's/Tags://' | tr -d '\r' | xargs)
  body=$(echo "$body" | grep -v "Tags:")
fi

slug=$(echo "$ISSUE_TITLE" | tr '[:upper:]' '[:lower:]' | tr ' ' '-' | tr -dc 'a-z0-9-')
filename="$POST_DATE-$slug.markdown"

mkdir -p "$POST_DIRECTORY"
timestamp=${POST_TIMESTAMP:-$(date +"%Y-%m-%d %H:%M:%S")}

{
  printf '%s\n' '---'
  printf 'title: "%s"\n' "$ISSUE_TITLE"
  printf 'date: %s\n' "$timestamp"
  if [[ -n "$tags" ]]; then
    printf 'tags: %s\n' "$tags"
  fi
  if [[ -n "${ISSUE_NUMBER:-}" ]]; then
    printf 'issue: %s\n' "$ISSUE_NUMBER"
  fi
  printf '%s\n\n' '---'
  printf '%s\n' "$body"
} > "$POST_DIRECTORY/$filename"

printf '%s\n' "$filename"
