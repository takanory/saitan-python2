import pytest
from survey import AnonymousSurvey


@pytest.fixture
def language_survey():
    """すべてのテスト関数で利用できるアンケート"""
    question = "最初に勉強した言語は何ですか？"
    language_survey = AnonymousSurvey(question)
    return language_survey


def test_store_single_response(language_survey):
    """1件の回答が正しく保存されているかをテストする"""
    language_survey.store_response('英語')
    assert '英語' in language_survey.responses


def test_store_three_responses(language_survey):
    """3件の異なる回答が正しく保存されているかをテストする"""
    responses = ['英語', 'スペイン語', '中国語']
    for response in responses:

        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
