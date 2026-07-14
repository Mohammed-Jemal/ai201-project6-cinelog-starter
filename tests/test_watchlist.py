import pytest
from services.watchlist_service import add_to_watchlist, FilmNotFoundError

def test_add_to_watchlist_nonexistent_film_raises(app, sample_user):
    with app.app_context():
        #using fake integer_id
        fake_film_id = 99999
        with pytest.raises(FilmNotFoundError):
            add_to_watchlist(user_id=sample_user, film_id=fake_film_id)