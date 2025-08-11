# Instructions for Creating Pull Request to site-scanning-documentation

## Overview
This proofreading experiment identified 16 spelling and typographical errors across 8 files in the GSA/site-scanning-documentation repository. All corrected files are available in the `site-scanning-documentation-fixes/` directory.

## Files to Update in the PR

### 1. README.md
**Change**: Line 58
```diff
- * [Index of Technical Docoumentation](https://digital.gov/guides/site-scanning/technical-details/#content-start) (**Recommended**)
+ * [Index of Technical Documentation](https://digital.gov/guides/site-scanning/technical-details/#content-start) (**Recommended**)
```

### 2. about/10-minute-walkthrough.md
**Changes**: Lines 3, 11, 29
```diff
- The Site Scanning program serves to make available an increasing range useful data about those websites.
+ The Site Scanning program serves to make available an increasing range of useful data about those websites.

- This involves gathering numerous public datasets and combining then filtering them.
+ This involves gathering numerous public datasets and combining them and filtering them.

- remains in use to decide which prioritize which scans to build
+ remains in use to decide which to prioritize when building scans
```

### 3. about/stakeholder-experience.md
**Changes**: Lines 30, 39
```diff
- The focus is on quickest path to a partial or full implementation
+ The focus is on the quickest path to a partial or full implementation

- work on the prototype that attempt to address all of the changes requested
+ work on the prototype that attempts to address all of the changes requested
```

### 4. pages/candidate-scans.md
**Changes**: Lines 3, 27, 29, 77, 161, 191
```diff
- The list of scans that have alreadby been built and are active
+ The list of scans that have already been built and are active

- Analyze the source code of eage page that loads
+ Analyze the source code of each page that loads

- validate or authenticate offical government social media accounts
+ validate or authenticate official government social media accounts

- page titles, page desciptions, keywords
+ page titles, page descriptions, keywords

- take ever link found in a page
+ take every link found in a page

- details, examples, and a metholodgy here
+ details, examples, and a methodology here
```

### 5. about/project-management/project-history.md
**Change**: Line 9
```diff
- Between 2015 - 2017, DHS builts scans for [HTTPS]
+ Between 2015 - 2017, DHS built scans for [HTTPS]
```

### 6. about/project-management/engineering-handbook.md
**Changes**: Lines 3, 35
```diff
- [[Note linke to June, 2025 version]
+ [[Note link to June, 2025 version]

- app is bootstraped and started along with the API
+ app is bootstrapped and started along with the API
```

### 7. pages/schedule.md
**Change**: Line 31
```diff
- from a publically hosted [CSV file]
+ from a publicly hosted [CSV file]
```

## PR Title
**Suggested Title**: "Fix spelling and typographical errors in documentation"

## PR Description
```
This PR fixes 16 spelling and typographical errors found during a comprehensive proofreading review of the documentation.

## Changes Made
- Fixed "Docoumentation" → "Documentation" in README.md
- Fixed "alreadby" → "already" in candidate-scans.md
- Fixed "offical" → "official" in candidate-scans.md
- Fixed "builts" → "built" in project-history.md
- Fixed "publically" → "publicly" in schedule.md
- And 11 other minor spelling/grammar corrections

## Files Modified
- README.md
- about/10-minute-walkthrough.md
- about/stakeholder-experience.md
- pages/candidate-scans.md
- about/project-management/project-history.md
- about/project-management/engineering-handbook.md
- pages/schedule.md

All changes are minimal corrections that preserve original meaning while improving readability and professionalism of the documentation.
```

## How to Create the PR

1. Clone the GSA/site-scanning-documentation repository
2. Create a new branch: `git checkout -b fix/spelling-errors`
3. Apply the changes listed above to each file
4. Commit with message: "Fix spelling and typographical errors in documentation"
5. Push branch and create pull request with the suggested title and description

The corrected files in this directory can be used as reference for the exact changes needed.