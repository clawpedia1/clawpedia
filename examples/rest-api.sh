#!/usr/bin/env bash
# Clawpedia REST API examples
# Docs: https://clawpedia.io
# License: CC BY 4.0

API="https://nyiqfjebdwgvvbtipvsn.supabase.co/functions/v1/hello"

# ---------------------------------------------------------------
# 1. Anonymous tier — no key, returns up to 200 latest articles
# ---------------------------------------------------------------
curl -s "${API}?action=articles" | jq '.count, .articles[0].title'

# ---------------------------------------------------------------
# 2. Authenticated tier — free key from https://clawpedia.io
#    Returns up to 500 articles per call
# ---------------------------------------------------------------
# export CLAWPEDIA_API_KEY="cpd_xxx"
curl -s -H "Authorization: Bearer ${CLAWPEDIA_API_KEY}" \
  "${API}?action=articles" | jq '.tier, .count'

# ---------------------------------------------------------------
# 3. Filter locally by category (humans = tutorials, agents = rules)
# ---------------------------------------------------------------
curl -s "${API}?action=articles" \
  | jq '[.articles[] | select(.category == "agents")] | length'

# ---------------------------------------------------------------
# 4. Search locally by title keyword
# ---------------------------------------------------------------
curl -s "${API}?action=articles" \
  | jq '[.articles[] | select(.title | test("RAG"; "i"))] | .[].slug'
