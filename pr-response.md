## comment 1 Renaming
What i did: renamed save_to_watchlist to add_to_watchlist in services/watchlist_service.py to match the projects verb_to_noune convention.I updated also the call part in routes/watchlist/watchlist.py
* How i verified: used global search to confirm no other files refernced to save_to_watchlist

## comment 2
What i did: created a class to handle the exception/error with pass. Then inside the add_to_watchlist function, I query to check if the user has already by using user_id and film_id. if the exists, raise exception handler

* how i verified: I ran the pytest tests/ -v and all exsting tests 100% passed.

## comment 3
what i did: created tests/test_watchlist.py and wrote test_add_to_watchlist_nonexistent_film_raises. I moved the shard fixtured fixtures into a new conftest.py file so both test files could use them. I modeled the new test structure after the equvalent test in test_collection.py, but used an integer for the fake_film_id since the watchlist featur is pre refactored.

* How i verified: I ran the pytest tests/ -v and all tests passed.

## Comment 4 — Default visibility
Position: I chose to keep the default visibility as public=True.
Reasoning: CineLog is a social and  community-driven platform. Making it public watchlists encourages user engagement and makes it easier for friends to share movie recommendations.

Trade-offs: The privacy-conscious users must take an extra step to explicitly opt-out by setting public=False. However, given the platform's social goals,  giving priority discoverability over strict privacy for movie lists is the default experience and keep it visible.

## Comment 5 — Sort order
Position: I agree with the reviewer and have updated the default sort order to "date added descending".
Reasoning: Returning entries newest-first is consistent with the behavior of get_collection(). It creates a uniform mental model across both lists and optimizes for the primary user behavior of "what should I watch next?" by surfacing their most recent additions at the top.

## comment 6 Rebase
what i did: I rebased successfully feature/watchlist onto main to pull in the team's UUID refactor. I then updated the docstring services/test_watchlist.py from int to UUID to match the new schema.
How i verified: I ran pytest tests/ -v to confirm all 5 tests passed with the new UUID.