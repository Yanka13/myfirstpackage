from toto.lib import who_am_i


def test_whoami():

    res = who_am_i()
    print(res)

    assert "Yannis" in res.split()
