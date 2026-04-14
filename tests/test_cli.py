from paperclip_company_factory.cli import parser


def test_bootstrap_from_prompt_command_is_registered():
    parsed = parser().parse_args(['bootstrap-from-prompt', 'Create a public AI content studio company'])
    assert parsed.command == 'bootstrap-from-prompt'


def test_bootstrap_from_prompt_accepts_text_format():
    parsed = parser().parse_args(['bootstrap-from-prompt', 'Create a public AI content studio company', '--format', 'text'])
    assert parsed.format == 'text'
