import pytest
from modules.api.clients.github import GitHub

ref="ac3f2b1e207cf7f8dd1950aff3466366452504b7"


@pytest.mark.api
def test_user_exists(github_api):
    user=github_api.get_user("macasin")
    assert user['login']=="macasin"


@pytest.mark.api
def test_user_upsent(github_api):
    r=github_api.get_user("macasin1111")
    assert r['message']=="Not Found"


@pytest.mark.api
def test_repo_exist(github_api):
    r= github_api.search_repo("autf")
    assert r['total_count']==50
    assert "AUTFILTERBOT" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_upsent(github_api):
    r=github_api.search_repo("vfvfknvfnvkjfn2213")
    assert r['total_count']==0


@pytest.mark.api 
def test_repoThatIncludeOneChar(github_api):
    r=github_api.search_repo('w')
    assert r['total_count'] !=0


@pytest.mark.api #the test that asset that sha equal to ref
def test_showTheCommitEmail(github_api):
    r=github_api.search_commit("macasin","auto",ref)
    assert r["sha"]== ref


@pytest.mark.api #message validation in commit
def test_messageIsCorrect(github_api): 
    r=github_api.search_commit ("macasin","auto",ref)
    assert r["commit"]["message"]=="Added some new tests on Pytest"

@pytest.mark.api #check if the login is valid
def test_logInCommit(github_api):
    r=github_api.search_commit ("macasin","auto",ref)
    assert r["author"]["login"]=="macasin"









