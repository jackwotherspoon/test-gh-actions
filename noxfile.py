import nox

@nox.session(python=["3.7", "3.8", "3.9", "3.10"])
def test(session):
    session.install("-r", "requirements.txt")
    # Run py.test against the unit tests.
    session.run(
        "py.test",
        *session.posargs
    )
