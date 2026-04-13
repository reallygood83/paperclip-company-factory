from paperclip_company_factory.cli import parser


def test_bootstrap_from_prompt_command_is_registered():
    parsed = parser().parse_args(['bootstrap-from-prompt', 'Create a public AI content studio company'])
    assert parsed.command == 'bootstrap-from-prompt'
