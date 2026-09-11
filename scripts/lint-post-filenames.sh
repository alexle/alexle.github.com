#!/bin/bash

set -e

POSTS_DIR="_posts"
EXIT_CODE=0

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

VALID_PATTERN='^[0-9]{4}-[0-9]{2}-[0-9]{2}-[a-z0-9]+(-[a-z0-9]+)*\.(markdown|md)$'

echo "Checking post filenames for kebab-case compliance..."
echo ""

while IFS= read -r -d '' file; do
    filename=$(basename "$file")

    if [[ ! $filename =~ $VALID_PATTERN ]]; then
        echo -e "${RED}FAIL:${NC} $file"
        echo "      Filename must match: YYYY-MM-DD-kebab-case-title.markdown"
        echo "      - Use lowercase letters only"
        echo "      - Separate words with hyphens"
        echo "      - No underscores, spaces, or special characters"
        echo ""
        EXIT_CODE=1
    fi
done < <(find "$POSTS_DIR" -type f \( -name "*.markdown" -o -name "*.md" \) -print0)

if [ $EXIT_CODE -eq 0 ]; then
    echo -e "${GREEN}All post filenames are valid kebab-case!${NC}"
fi

exit $EXIT_CODE
