---
title: Splunk Advanced User Search Restrictions
date: 2017-06-28
tags: [splunk]
published: false
---

# Splunk Advanced User Search Restrictions

Splunk's role based access control (RBAC) allows for role specific search term
restrictions to be applied to a user's search. What this means if that a user's
role has a restriction, such as `host=google.com`, a  search for `host=*` or
a generic `*` search would return only events where the `host` field was
`google.com`, while a search for `host=bing.com` would return 0 results.

screenshot

The [search filter
documentation](http://docs.splunk.com/Documentation/Splunk/6.6.0/Security/Addandeditroles#Search_filter_format)
states that this filter can include any of the following search terms:
* `source=`
* `host=`
* `index=`
* `eventtype=`
* `sourcetype=`
* search fields
* wildcards
* use `OR` to use multiple terms, or `AND` to make searches more restrictive

The search terms cannot include:
* saved searches
* time operators
* regular expressions
* any fields or modifiers Splunk Web can overwrite

The following is a motivating example of where search filters could be used,
some limitations 

## Example

Consider a global enterprise with multiple departments. There could be
restrictions around which regions can access what indexes and sourcetypes, as
well as restrictions stemming from the department.

|  Region  | Allowed Indexes | Allowed Sourcetypes |
|:--------:|:---------------:|:-------------------:|
|  Africa  |                 |                     |
| Americas |                 |                     |
|   Asia   |                 |                     |
|  Europe  |                 |                     |
|  Oceania |                 |                     |

| Department | Allowed Indexes | Allowed Sourcetypes |
|:----------:|:---------------:|:-------------------:|
|            |                 |                     |

The naïve approach to implementing this is to  create a role for each
region/department pairing, 
assign a search filter to each
role. 

There are also some limitations when it comes to search filters operating over
multiple roles.


## Solution

We utilise a lookup to map splunk roles to search terms

```
role, email_domain
can_delete, @splunk.com
user, @google.com
user, @gmail.com
```

We also create a macro in Splunk to determine all the roles a user belongs to 

If the lookup doesn't have any matches, we assume that the user should not have
any access. To "short circuit" this Splunk query, we just throw in a ridiculous
search term that won't match any events.

```
index=exchange to=$to$ from=$from$ [ |rest /services/authentication/current-context | fields roles | mvexpand roles | rename roles AS role | lookup role_to_domains role
| eval sender="$from$" | eval recipient="$to$"
| mvexpand email_domain
| eval email_domain = "%"+email_domain
| eval valid_search=if(like(sender,email_domain),1,if(like(recipient,email_domain),1,0))
| stats sum(valid_search) as valid_search | eval search=if(valid_search&gt;0,"","ThisLongStringShouldBeFairlyRandomAndIsNotLikelyToOccurInAnyRealEventThereforeSplunkShouldNotBeAbleToFindAnyMatchingEventsContainingThisStringInAdditionItShouldBeFairlyFastAsTheBloomFilterShouldAlsoIgnoreThis") | fields search ]
```

This approach works great for restricting users who are using forms, but won't
work at all when a user has normal search access to Splunk (as they can simply
not include the macro when they do a search). 
