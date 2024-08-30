import logging
import pathlib
import re

import anthropic
import jinja2

logger = logging.getLogger(__name__)


def process_markdown_links(markdown_links):
    current_dir = pathlib.Path(__file__).parent
    template_path = current_dir / "templates" / "markdown_links.j2"

    with template_path.open() as file:
        template = jinja2.Template(file.read())

    prompt = template.render(markdown_links=markdown_links)
    prompt = prompt.strip()
    prompt = re.sub(r"\s+", " ", prompt)

    client = anthropic.Anthropic()

    if not client.api_key:
        raise ValueError(
            "No API key found. Please set the ANTHROPIC_API_KEY environment variable."
        )

    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=2000,
        temperature=0,
        messages=[{"role": "user", "content": [{"type": "text", "text": prompt}]}],
    )

    print(
        f"Prompt tokens: {message.usage.input_tokens}, Completion tokens: {message.usage.output_tokens}, Total tokens: {message.usage.input_tokens + message.usage.output_tokens}"
    )

    return message.content
