#!/usr/bin/env python3
"""Check built pages, local links/assets, and accidental source publication offline."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.errors = set(), [], []
        self.h1_count = 0
        self.has_title = self.has_description = self.has_main = self.redirect = False
        self.feed(source)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                self.errors.append('Duplicate ID: ' + attrs['id'])
            self.ids.add(attrs['id'])
        self.h1_count += tag == 'h1'
        self.has_title |= tag == 'title'
        self.has_main |= tag == 'main'
        self.has_description |= tag == 'meta' and attrs.get('name') == 'description' and bool(attrs.get('content'))
        self.redirect |= tag == 'meta' and attrs.get('http-equiv', '').lower() == 'refresh'
        if tag == 'img':
            if 'alt' not in attrs:
                self.errors.append('Image missing alt attribute')
            if not attrs.get('width') or not attrs.get('height'):
                self.errors.append('Image missing explicit dimensions')
        for name in ('href', 'src', 'poster'):
            if name in attrs:
                self.links.append(attrs[name])
        if 'srcset' in attrs:
            self.links.extend(item.strip().split()[0] for item in attrs['srcset'].split(',') if item.strip())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', default='_site', help='Jekyll build output')
    parser.add_argument('--baseurl', default='', help='Repository subpath, e.g. /preview-site')
    args = parser.parse_args()
    root = Path(args.site).resolve()
    prefix = args.baseurl.rstrip('/')
    errors, checked_links = [], 0
    pages = {path: Page(path.read_text()) for path in root.rglob('*.html')}
    if not pages:
        sys.exit('No built HTML found. Run bundle exec jekyll build first.')

    def check_link(source, link):
        nonlocal checked_links
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc:
            return
        checked_links += 1
        if not link or link == '#':
            errors.append(f'{source.relative_to(root)}: empty/placeholder link')
            return
        path = unquote(parsed.path)
        if path.startswith('/'):
            if prefix and path != prefix and not path.startswith(prefix + '/'):
                errors.append(f'{source.relative_to(root)}: link escapes baseurl: {link}')
                return
            target = root / path[len(prefix):].lstrip('/')
        else:
            target = source.parent / path if path else source
        target = target.resolve()
        if target != root and root not in target.parents:
            errors.append(f'{source.relative_to(root)}: link escapes build directory: {link}')
            return
        if target.is_dir():
            target /= 'index.html'
        if not target.is_file():
            errors.append(f'{source.relative_to(root)}: missing target: {link}')
        elif parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:
            errors.append(f'{source.relative_to(root)}: missing fragment: {link}')

    for path, page in pages.items():
        label = str(path.relative_to(root))
        errors.extend(f'{label}: {error}' for error in page.errors)
        if not page.redirect:
            if page.h1_count != 1:
                errors.append(f'{label}: expected one h1, got {page.h1_count}')
            if not (page.has_title and page.has_description and page.has_main):
                errors.append(f'{label}: missing title, description, or main landmark')
            if 'main-content' not in page.ids:
                errors.append(f'{label}: missing skip-link destination')
        source = path.read_text()
        if re.search(r'wpvlhc-aog\.local|wp-content/|\[contact-form|<!-- wp:', source):
            errors.append(f'{label}: WordPress markup or local URL remains')
        for link in page.links:
            check_link(path, link)

    for path in root.rglob('*.css'):
        for link in re.findall(r'url\(\s*[\'\"]?([^\)\'\"]+)', path.read_text()):
            check_link(path, link.strip())
    for name in ('feed.xml', 'sitemap.xml'):
        try:
            ET.parse(root / name)
        except (OSError, ET.ParseError) as error:
            errors.append(f'{name}: {error}')
    for path in root.rglob('*'):
        relative = path.relative_to(root)
        if any(part in {'docs', 'scripts', 'vendor', '.github', '_data', '_drafts'} for part in relative.parts):
            errors.append(f'Authoring source leaked into output: {relative}')
        if path.is_file() and (path.suffix.lower() in {'.php', '.sql', '.rb', '.py', '.md', '.yml', '.yaml'} or path.name in {'Gemfile', 'Gemfile.lock', '.env'}):
            errors.append(f'Non-public source leaked into output: {relative}')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        sys.exit(f'FAILED: {len(errors)} issue(s).')
    print(f'PASS: {len(pages)} HTML pages, {checked_links} local links/assets, XML feeds, and publication boundaries (baseurl={prefix or "/"}).')


if __name__ == '__main__':
    main()
