"""Submit address for passport feature tests."""

import json
from unittest.mock import patch

import pytest
from account.models import Account, AccountAPIKey, Community
from django.contrib.auth.models import User
from django.test import Client
from eth_account.messages import encode_defunct
from pytest_bdd import given, scenario, then, when
from registry.models import Passport, Score, Stamp
from registry.test.test_passport_submission import mock_passport
from web3 import Web3

web3 = Web3()
web3.eth.account.enable_unaudited_hdwallet_features()

pytestmark = pytest.mark.django_db


@pytest.fixture
def scorer_user():
    user = User.objects.create_user(username="testuser-1", password="12345")
    print("scorer_user user", user)
    return user


@pytest.fixture
def scorer_account(scorer_user):
    # TODO: load mnemonic from env
    my_mnemonic = (
        "chief loud snack trend chief net field husband vote message decide replace"
    )
    web3_account = web3.eth.account.from_mnemonic(
        my_mnemonic, account_path="m/44'/60'/0'/0/0"
    )

    print("scorer_user", scorer_user)
    print("web3_account.address", web3_account.address)
    account = Account.objects.create(user=scorer_user, address=web3_account.address)
    return account


@pytest.fixture
def scorer_api_key(scorer_account):
    (account_api_key, secret) = AccountAPIKey.objects.create_key(
        account=scorer_account, name="Token for user 1"
    )
    return secret


@pytest.fixture
def scorer_passport(scorer_account, scorer_community):
    passport = Passport.objects.create(
        address=scorer_account.address,
        passport={"name": "John Doe"},
        version=1,
        community=scorer_community,
    )
    return passport


@pytest.fixture
def scorer_score(scorer_passport):
    stamp = Score.objects.create(
        passport=scorer_passport,
        score="0.650000000",
    )
    return stamp


@pytest.fixture
def scorer_community(mocker, scorer_account):
    mock_settings = {
        "Google": 1234,
        "Ens": 1000000,
    }
    # Mock gitcoin scoring settings
    mocker.patch(
        "scorer_weighted.models.settings.GITCOIN_PASSPORT_WEIGHTS",
        mock_settings,
    )

    community = Community.objects.create(
        name="My Community",
        description="My Community description",
        account=scorer_account,
    )
    return community


@scenario("features/submit_passport.feature", "Submit passport successfully")
def test_submit_passport_successfully():
    """Submit passport successfully."""


@given(
    "that I'm a Passport developer and have a community ID", target_fixture="community"
)
def _(scorer_community):
    """that I'm a Passport developer and have a community ID."""
    pass


@when(
    "I call the submit-passport API for an Ethereum account under that community ID",
    target_fixture="submit_passport_response",
)
def _(scorer_api_key, scorer_community, mocker):
    """I call the submit-passport API for an Ethereum account under that community ID."""

    mocker.patch("registry.views.get_passport", return_value=mock_passport)
    mocker.patch("registry.views.validate_credential", side_effect=[[], []])
    client = Client()

    my_mnemonic = (
        "chief loud snack trend chief net field husband vote message decide replace"
    )
    web3_account = web3.eth.account.from_mnemonic(
        my_mnemonic, account_path="m/44'/60'/0'/0/0"
    )

    signed_message = web3.eth.account.sign_message(
        encode_defunct(text="I authorize the passport scorer to validate my account"),
        private_key=web3_account.key,
    )

    payload = {
        "community": scorer_community.id,
        "address": scorer_community.account.address,
        "signature": signed_message.signature.hex(),
    }

    response = client.post(
        "/registry/submit-passport",
        json.dumps(payload),
        content_type="application/json",
        HTTP_AUTHORIZATION=f"Token {scorer_api_key}",
    )

    return response


@then(
    "the API logs all of the valid Passport data points (VCs), namely the complete JSON, mapped to that Passport holder within the respective community ID directory"
)
def _(scorer_community, submit_passport_response):
    """the API logs all of the valid Passport data points (VCs), namely the complete JSON, mapped to that Passport holder within the respective community ID directory."""
    assert submit_passport_response.status_code == 200

    assert len(Passport.objects.all()) == 1
    passport = Passport.objects.all()[0]

    assert passport.community.id == scorer_community.id


@then("the API reads all of the Passport data points")
def _():
    """the API reads all of the Passport data points."""
    pass


@scenario(
    "features/submit_passport.feature",
    "As a developer, I want to rely on the Gitcoin Community Scorer scoring settings of the API",
)
def _(
    mocker,
):
    """As a developer, I want to rely on the Gitcoin Community Scorer scoring settings of the API."""
    mock_settings = {
        "Google": 1234,
        "Ens": 1000000,
    }
    # Mock gitcoin scoring settings
    mocker.patch("scorer_weighted.models.settings", return_value=mock_settings)


@given("I have not further configured its settings")
def _():
    """I have not further configured its settings."""
    # Nothingg to do here
    pass


@given("that I have created a community ID")
def _(scorer_community):
    """that I have created a community ID."""
    pass


@then(
    "I want to get a score based on the Gitcoin Community Score and deduplication rules (see default deduplication settings here)"
)
def _(submit_passport_response):
    """I want to get a score based on the Gitcoin Community Score and deduplication rules (see default deduplication settings here)."""

    assert submit_passport_response.status_code == 200
    assert submit_passport_response.json() == [
        {
            "passport_id": 1,
            "address": "0xb81c935d01e734b3d8bb233f5c4e1d72dbc30f6c",
            "score": float(1001234),
        }
    ]


@then(
    "log the score associated with this Passport under the corresponding community ID"
)
def _():
    """log the score associated with this Passport under the corresponding community ID."""
    raise NotImplementedError