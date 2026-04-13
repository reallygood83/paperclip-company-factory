from paperclip_company_factory.bridge import interpret_prompt


def test_interpret_request_detects_template_and_visibility():
    result = interpret_prompt('Create a public AI content studio company for newsletters')
    assert result['template'] == 'content-studio'
    assert result['visibility'] == 'public'
